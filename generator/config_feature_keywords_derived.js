// CONFIG_FEATURE_KEYWORDS_DERIVED
// Keywords derived from the user input.

const config_feature_keywords_derived = {
  FS_DJANGO_APP_NAME_CONFIG: (selected_keywords) =>
    selected_keywords["FS_DJANGO_APP_NAME"][0].toUpperCase() +
    selected_keywords["FS_DJANGO_APP_NAME"].slice(1) +
    "Config",
};

export default config_feature_keywords_derived;
