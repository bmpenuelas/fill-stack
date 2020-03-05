###############################################################################
#
# WARNING! Run this script from the project root directory.
#
###############################################################################

import sys
import json

from   shutil    import copyfile, rmtree
from   os        import chdir, getcwd, path
from   os.path   import abspath, join, isfile, dirname
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
    '-f', '--features', dest='features',
    default=join(root_path, 'scripts/webapp_features.json'),
    help='JSON file with the selected features.'
)
parser.add_argument(
    '-k', '--keywords', dest='keywords',
    default=join(root_path, 'scripts/webapp_keywords.json'),
    help='JSON file with the keyword values for the selected features.'
)
parser.add_argument(
    '-cl', '--clean', dest='clean',
    action='store_true',
    help='Clean all output files.'
)


# Get cli args
args = parser.parse_args()
args_dict = vars(args)


if args_dict['clean']:
    # Clean all generated files
    cmd_clean = ['git', 'clean', '-fdX']
    generator.run_cmd_command(cmd_clean, True)

else:
    ###########################################################################
    # CONFIG
    ###########################################################################

    with open(args_dict['features'], 'r') as features_file:
        features = json.load(features_file)
        features = [feature for feature in features.keys() if features[feature]]

    with open(args_dict['keywords'], 'r') as keywords_file:
        keywords = json.load(keywords_file)

    missing_keywords = generator.find_missing_keywords(features, keywords)
    for keyword in missing_keywords:
        if generator.config_feature_keywords[keyword]['environment']:
            keywords[keyword] = keyword.lower() + generator.randomString(10)
        else:
            raise ValueError('Invalid value for ' +  keyword)


    ###########################################################################
    # Generate
    ###########################################################################

    output_path = path.normpath(
        path.join(generator.BASE_PATH, '..', '.webapp_generated')
    )
    if path.exists(output_path):
        rmtree(output_path)

    if generator.check_required_keywords(features, keywords):
        generator.gen_files(
            generator.get_required_files(features),
            features,
            keywords,
            output_path
        )
    else:
        print('Error found when checking the required keywords.')
