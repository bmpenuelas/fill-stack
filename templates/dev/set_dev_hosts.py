try:
    from python_hosts.hosts import Hosts, HostsEntry
except ImportError:
    raise ImportError('Error importing python_hosts, you can install it running: pip install python-hosts')

from argparse import ArgumentParser


###############################################################################
# COMMAND LINE PARAMETERS
###############################################################################

# Command line interface
parser = ArgumentParser(
    description='Set/unset redirection of your domain to your local machine by editing the hosts file.'
)

# Optional arguments
parser.add_argument(
    '-u', '--unset', dest='unset',
    action='store_true',
    help='Unset development host (without this parameter the dev host will be set).'
)
parser.add_argument(
    '-p', '--path_to_hosts_file', dest='path_to_hosts_file',
    help='Path to hosts file, defaults to autodetect.'
)

# Get cli args
args = parser.parse_args()
args_dict = vars(args)


###############################################################################
# SET HOSTS
###############################################################################

hosts = Hosts(path=args_dict['path_to_hosts_file'])

if args_dict['unset']:
    hosts.remove_all_matching(name='{{ FS_DOMAIN }}')
    print('Removed development host.')
else:
    new_entry = HostsEntry(entry_type='ipv4', address='0.0.0.0', names=['www.{{ FS_DOMAIN }}', '{{ FS_DOMAIN }}'])
    hosts.add([new_entry])
    print('Added development host.')
hosts.write()
