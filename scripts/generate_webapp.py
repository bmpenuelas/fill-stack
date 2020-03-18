import sys
import json

from   shutil    import copyfile, rmtree
from   os        import chdir, getcwd, path, listdir
from   os.path   import abspath, join, isfile, dirname, exists
from   argparse  import ArgumentParser

root_path = abspath(join(dirname(abspath(__file__)),'..'))
sys.path.append(root_path)
from   generator import generator


###############################################################################
# COMMAND LINE PARAMETERS
###############################################################################

# Command line interface
parser = ArgumentParser(
    description='Generate webapp.'
)

# Optional arguments
parser.add_argument(
    '-s', '--settings', dest='settings',
    default=join(root_path, 'scripts/webapp_settings.json'),
    help='JSON file with the selected settings (features and keywords).'
)
parser.add_argument(
    '-o', '--output', dest='output',
    default=path.join(generator.BASE_PATH, '..', '.generated_webapp'),
    help='Path for the generated output files.'
)
parser.add_argument(
    '-cl', '--clean', dest='clean',
    action='store_true',
    help='Clean all output files.'
)


# Get cli args
args = parser.parse_args()
args_dict = vars(args)


###########################################################################
# CLEAN
###########################################################################
if args_dict['clean']:
    # Clean all generated files
    cmd_clean = ['git', 'clean', '-fdX']
    generator.run_cmd(cmd_clean, True)

else:
    ###########################################################################
    # CONFIG
    ###########################################################################

    with open(args_dict['settings'], 'r') as settings_file:
        settings = json.load(settings_file)
        features = settings['selected_features']
        keywords = settings['selected_keywords']

    missing_keywords = generator.find_missing_keywords(features, keywords)
    for keyword in missing_keywords:
        if not generator.config_feature_keywords[keyword]['environment']:
            raise ValueError('Missing value for ' +  keyword)


    ###########################################################################
    # Generate
    ###########################################################################

    output_path = args_dict['output']
    if path.exists(output_path):
        rmtree(output_path)

    if generator.check_required_keywords(features, keywords):
        generator.gen_files(
            generator.get_required_files(features),
            features,
            keywords,
            output_path,
        )
    else:
        print('Error found when checking the required keywords.')
