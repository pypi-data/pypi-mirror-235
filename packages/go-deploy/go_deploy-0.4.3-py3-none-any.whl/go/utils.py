import logging
import os

logger = logging.getLogger('go.utils')

_LOGGER_SETUP = False


def init_logger(name):
    if not _LOGGER_SETUP:
        setup_logging()

    return logging.getLogger(name)


def _get_default_level():
    return os.environ.get('GO_LOG_LEVEL', logging.INFO)


def setup_logging(level=None):
    level = level or _get_default_level()

    config_dict = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'concise': {
                'format': '[%(levelname)s] %(name)s :: %(message)s'
            },
            'detailed': {
                'format': '%(asctime)s :: %(name)s :: %(levelname)s :: %(funcName)s :: %(message)s'
            }
        },
        'handlers': {
            'console': {
                'level': level,
                'class': 'logging.StreamHandler',
                'formatter': 'detailed',
            }
        },
        'loggers': {
            'go': {
                'handlers': ['console'],
                'level': level,
                'propagate': True
            }
        }
    }

    import logging.config as config

    config.dictConfig(config_dict)

    global _LOGGER_SETUP

    _LOGGER_SETUP = True


def create_parser(usage='%(prog)s [options]',
                  description='', 
                  formatter_class=None):
    from argparse import ArgumentParser, RawDescriptionHelpFormatter

    formatter_class = formatter_class or RawDescriptionHelpFormatter
    return ArgumentParser(usage=usage, description=description, formatter_class=formatter_class)


def build_parser():
    description = (
           'Provision using yaml config file'
           '\n'
           '\n'
           'Example:'
           '\n'
           "      go-provision -c config.yaml"
           '\n'
    )

    parser = create_parser(description=description)
    parser.add_argument('-init', action='store_true', default=False, help='initialize terraform working directory')
    parser.add_argument('-c', '--conf', type=str, default=None, help='yaml config file', required=False)
    parser.add_argument('-d', '--working-directory', type=str, default='aws',
                        help='terraform working directory', required=False)
    parser.add_argument('-w', '--workspace', type=str, default=None, help='terraform workspace', required=False)
    parser.add_argument('-list-workspaces', action='store_true', default=False, help='list terraform workspaces',)
    parser.add_argument('-verbose', action='store_true', default=False, help='verbose')
    parser.add_argument('-dry-run', action='store_true', default=False, help='dry-run')
    parser.add_argument('-destroy', action='store_true', default=False, help='destroy terraform state and workspace')
    parser.add_argument('-show', action='store_true', default=False, help='show terraform state')
    parser.add_argument('-output', action='store_true', default=False, help='show terraform output')
    return parser


def read_config(conf_file):
    import yaml

    with open(conf_file, 'r') as file:
        config = yaml.safe_load(file)
        return config


def inventory_string(host, user, port, private_key_path):
    host_string = '{} ansible_connection=ssh ansible_user={} ansible_port={} ansible_ssh_private_key_file={}'
    return host_string.format(host, user, port, private_key_path)


def write_inventory_file(file_path, host_string):
    with open(file_path, 'w') as outfile:
        outfile.write('[aws]\n')
        outfile.write(host_string)
        outfile.write('\n')


def write_ns_to_json_file(ns, file_path):
    import json

    json_string = json.dumps(ns, default=lambda o: o.__dict__, sort_keys=True, indent=4)
    with open(file_path, 'w') as outfile:
        outfile.write(json_string)


def check_ssh_keys(ssh_keys):
    def check_if_exists(path_to_file):
        from pathlib import Path

        path = Path(path_to_file).expanduser().absolute()
        return os.path.exists(path) and os.path.isfile(path)

    return check_if_exists(ssh_keys.public) and check_if_exists(ssh_keys.private)


# noinspection PyBroadException
def test_ssh_connection_using_paramiko(ip, username, private_key_path, port=22, max_tries=30):
    from .ssh_helper import SshHelper

    helper = SshHelper(ip, username, private_key_path, port)
    num_tries = 1

    logger.info(f'Checking if ssh port to host {ip} is ready.')
    while num_tries <= max_tries:
        try:
            logger.info(f'Checking ssh attempt:{num_tries} out of {max_tries}')
            helper.connect()
            logger.info(f'OK, ssh port is READY on host {ip}: num_tries:' + str(num_tries))
            return
        except Exception:
            helper.close_quietly()
            num_tries += 1
            import time
            time.sleep(2)

    logger.warning(f'Looks like ssh port is not ready on host {ip}. Please check ssh and/or try again ...')


def test_ssh_connection(ip, port=22, max_tries=100):
    cmd = 'nc -z -G 1 ' + ip + ' ' + str(port)
    num_tries = 1

    logger.info(f'testing if ssh port is ready on {ip}:{cmd}')
    while num_tries <= max_tries:
        logger.info('testing ssh num_tries:' + str(num_tries))
        code = os.system(cmd)

        if code == 0:
            return

        num_tries += 1

    logger.warning('ssh port is not ready')


def execute_and_stream_output(cmd):
    import subprocess

    if isinstance(cmd, str):
        logger.info('Executing:' + cmd)
        command = cmd.split()
    else:
        logger.info('Executing:' + ' '.join(cmd))
        command = cmd

    result = subprocess.run(command, stderr=subprocess.PIPE)
    code = result.returncode

    if code != 0:
        raise Exception('command failed:code={}:{}:reason={}'.format(
            code,
            subprocess.list2cmdline(command),
            result.stderr.decode('utf-8')))


def execute(cmd):
    import subprocess

    if isinstance(cmd, str):
        logger.info('Executing:' + cmd)
        command = cmd.split()
    else:
        logger.info('Executing:' + ' '.join(cmd))
        command = cmd

    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    code = result.returncode

    if code != 0:
        raise Exception('command failed:code={}:{}:reason={}'.format(
            code,
            subprocess.list2cmdline(command),
            result.stdout.decode('utf-8') + "\n" + result.stderr.decode('utf-8')))

    logger.info(f"Status=OK:command={' '.join(command)}")
    return result.stdout.decode('utf-8')
