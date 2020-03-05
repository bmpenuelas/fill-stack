import re
import json
import string
import random
import subprocess

from   os      import path, mkdir, makedirs
from   os.path import normpath, dirname
from   shutil  import copyfile
from   pathlib import Path
from   jinja2  import Environment, FileSystemLoader, Template, StrictUndefined

from   generator.config_feature_keywords import available_features
from   generator.config_feature_keywords import config_feature_keywords, config_feature_keywords_derived
from   generator.config_feature_paths    import config_feature_paths


# Constants to be used elsewhere

BASE_PATH     = dirname(path.realpath(__file__))
TEMPLATE_PATH = normpath(path.join(BASE_PATH, '..', 'templates'))

ALL_FEATURES  = list(available_features.keys())
ALL_KEYWORDS  = list(config_feature_keywords.keys())
ALL_FILES     = list(config_feature_paths.keys())


# Functions

def randomString(stringLength=10):
    """ Generate a random string of fixed length """

    letters = string.ascii_lowercase + string.digits
    return ''.join(random.choice(letters) for i in range(stringLength))


def run_cmd_command(cmd, get_lines=False):
    ''' Run a command in the shell and return the output. '''

    result = subprocess.run(cmd, stdout=subprocess.PIPE)
    decoded = result.stdout.decode('utf-8')
    return decoded if not get_lines else decoded.split('\n')


def get_required_keywords(selected_features):
    """ Get the keywords that are to be chosen according to the selected features """

    required_features = ['common'] + selected_features

    required_keywords = []
    for keyword in config_feature_keywords:
        for feature_combination in config_feature_keywords[keyword]['features']:
            if all([item in required_features for item in feature_combination]):
                required_keywords.append(keyword)

    return required_keywords


def find_invalid_keywords(selected_keywords):
    """ Find whether any of the chosen keywords does not meet the defined regex """

    return [keyword for keyword, value in selected_keywords.items() if not re.match(config_feature_keywords[keyword]['sanitize'], value)]


def check_required_keywords(selected_features, selected_keywords):
    """ Find whether any of the needed keywords has not been chosen """

    required_keywords = get_required_keywords(selected_features)
    return all([item in selected_keywords.keys() for item in required_keywords])


def find_missing_keywords(selected_features, selected_keywords):
    """ Find which needed keywords have not been chosen """

    required_keywords = get_required_keywords(selected_features)
    return [item for item in required_keywords if not item in selected_keywords.keys()]


def get_required_files(selected_features):
    """ Find which template files are required for the selected features """

    required_features = ['common'] + selected_features

    required_files = []
    for path in config_feature_paths:
        for feature_combination in config_feature_paths[path]['features']:
            if all([item in required_features for item in feature_combination]):
                required_files.append(path)

    return required_files


def get_templated(template, parameters):
    """ Get the given template filled with the chosen keywords """

    template = Template(template)
    return template.render(parameters)


def gen_files(required_files, selected_features, selected_keywords, output_path):
    """Generate templated files for selected features.

    Args:
        required_files (list)
        selected_features (list)
        selected_keywords (dict)
            {
                'FS_KEYWORD': SelectedKeyWordValue,
                'FS_KEYWORD': ...,
            }
        output_path (str)
    """

    if not path.exists(output_path):
        mkdir(output_path)

    file_loader = FileSystemLoader(TEMPLATE_PATH)
    jinja_env = Environment(loader=file_loader, trim_blocks=True, lstrip_blocks=True)
    jinja_env.undefined = StrictUndefined
    selected_keywords.update({k: v(selected_keywords) for k, v in config_feature_keywords_derived.items()})
    template_values = selected_keywords
    template_values['render_features'] = {feature: feature in selected_features for feature in ALL_FEATURES}

    for required_file in required_files:
        required_file_templated_path = get_templated(config_feature_paths[required_file]['template'], template_values)
        new_path = path.join(output_path, required_file_templated_path)
        if (new_path[-1] == '/'):
            if not path.exists(new_path):
                makedirs(new_path)
        elif (config_feature_paths[required_file]['binary']):
            copyfile(path.join(TEMPLATE_PATH, required_file), new_path)
        else:
            with open(new_path, 'w') as output_file:
                template = jinja_env.get_template(required_file)
                templated_file = template.render(template_values)
                output_file.write(templated_file)
