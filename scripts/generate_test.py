import sys
import json
import subprocess

from   shutil   import copyfile
from   os       import chdir, environ
from   os.path  import abspath, join, isfile, dirname
from   argparse import ArgumentParser

root_path = abspath(join(dirname(abspath(__file__)),'..'))
sys.path.append(root_path)
from   generator.generator import ALL_FEATURES, run_cmd, get_keyword_info
from   generator.tests     import tests


###############################################################################
# COMMAND LINE PARAMETERS
###############################################################################

# Command line interface
parser = ArgumentParser(
    description='Generate templated files.'
)

# Optional arguments
parser.add_argument(
    '-s', '--secret', dest='secret',
    action='store_true',
    help='Take secrets file if exists.'
)
parser.add_argument(
    '-r', '--run', dest='run',
    action='store_true',
    help='Run docker-compose once generated.'
)
parser.add_argument(
    '-d', '--down', dest='down',
    action='store_true',
    help='Run docker-compose down before rebuilding services.'
)
parser.add_argument(
    '-dr', '--down_run', dest='down_run',
    action='store_true',
    help='Equivalent to -d -r.'
)
parser.add_argument(
    '-c', '--code', dest='code',
    action='store_true',
    help='Open VSCode instead of running.'
)
parser.add_argument(
    '-ki', '--kwinfo', dest='kwinfo',
    action='store_true',
    help='Get all keywords info.'
)
parser.add_argument(
    '-cl', '--clean', dest='clean',
    action='store_true',
    help='Clean all output files.'
)

# Get cli args
args = parser.parse_args()
args_dict = vars(args)


###############################################################################
# Generate
###############################################################################

if args_dict['clean']:
    # Clean all generated files
    cmd_clean = ['git', 'clean', '-fdX']
    run_cmd(cmd_clean, True)

elif args_dict['kwinfo']:
    print(json.dumps(get_keyword_info(ALL_FEATURES)))

else:
    # Generate files
    test_results = tests.main()

    if not any([test_results.errors, test_results.failures]):
        templated_path = environ['FS_TEST_OUTPUT_PATH'] if ('FS_TEST_OUTPUT_PATH' in environ) else abspath(join(root_path, '.generated_test'))

        secret_env = join(root_path, 'templates', '.env.secret')
        if isfile(secret_env):
            copyfile(secret_env, join(templated_path, '.env'))

        if args_dict['code']:
            # Open directory in VSCode
            cmd_code = ['code', templated_path]
            run_cmd(cmd_code)

        elif args_dict['down'] or args_dict['down_run'] or args_dict['run']:
            # Optionally run
            chdir(templated_path)
            if args_dict['down'] or args_dict['down_run']:
                cmd_docker_compose_down = ['docker-compose', 'down']
                print(run_cmd(cmd_docker_compose_down))

            if args_dict['run'] or args_dict['down_run']:
                cmd_docker_compose_restart = ['docker-compose', 'up', '-d', '--no-deps', '--build']
                print(run_cmd(cmd_docker_compose_restart))
