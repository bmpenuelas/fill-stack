import nunjucks from "nunjucks";
import JSZip from "jszip";
import { saveAs } from "file-saver";
import {
  // available_features,
  config_feature_keywords,
  config_feature_paths,
  config_feature_keywords_derived,
  ALL_FEATURES,
  // ALL_KEYWORDS,
  // ALL_FILES,
} from "@/utils";

// Constants to be used elsewhere

export const VERSION = "v0.1.0";

export const TEMPLATES_PATH = "templates";

// Functions

export function get_required_keywords(
  selected_features,
  include_secrets = true
) {
  // Get the keywords that are to be chosen according to the selected features

  let required_features = ["common"].concat(selected_features);
  let required_keywords = [];

  for (let keyword in config_feature_keywords) {
    for (let feature_combination of config_feature_keywords[keyword][
      "features"
    ]) {
      if (
        feature_combination.every((item) => required_features.includes(item))
      ) {
        required_keywords.push(keyword);
      }
    }
  }
  if (!include_secrets) {
    required_keywords = required_keywords.filter(
      (x) => !config_feature_keywords[x]["environment"]
    );
  }
  return required_keywords;
}

export function get_required_env_vars(selected_features) {
  // Get the keywords that are to be chosen according to the selected features

  let required_keywords = get_required_keywords(selected_features);
  let required_env_vars = required_keywords.filter(
    (item) => config_feature_keywords[item]["environment"]
  );
  return required_env_vars;
}

export function find_invalid_keywords(selected_keywords) {
  // Find whether any of the chosen keywords does not meet the defined regex

  return Object.entries(selected_keywords)
    .filter(
      ([keyword, value]) =>
        !value.match(config_feature_keywords[keyword]["sanitize"])
    )
    .map((x) => x[0]);
}

export function check_required_keywords(selected_features, selected_keywords) {
  // Find whether any of the needed keywords has not been chosen

  let required_keywords = get_required_keywords(selected_features);
  return required_keywords
    .filter((x) => !config_feature_keywords[x]["environment"])
    .every((item) => Object.keys(selected_keywords).includes(item));
}

export function find_missing_keywords(selected_features, selected_keywords) {
  // Find which needed keywords have not been chosen

  let required_keywords = get_required_keywords(selected_features, false);
  return required_keywords.filter(
    (item) => !Object.keys(selected_keywords).includes(item)
  );
}

export function get_keyword_info(selected_features) {
  // Get info for the user to choose the keywords
  let keyword_info = {};
  for (let feature of get_required_keywords(selected_features)) {
    let feature_cfg = config_feature_keywords[feature];
    if (feature_cfg["secret"]) {
      continue;
    }
    let new_keyword_info = {
      templateName: feature,
      name: feature_cfg["name"],
      description: feature_cfg["description"],
      default: feature_cfg["default"],
    };
    if (feature_cfg["features"][0][0] in keyword_info) {
      keyword_info[feature_cfg["features"][0][0]][feature] = new_keyword_info;
    } else {
      keyword_info[feature_cfg["features"][0][0]] = {
        [feature]: new_keyword_info,
      };
    }
  }
  return keyword_info;
}

export function get_required_files(selected_features) {
  // Find which template files are required for the selected features

  let required_features = ["common"] + selected_features;

  let required_files = [];
  for (let path in config_feature_paths) {
    for (let feature_combination of config_feature_paths[path]["features"]) {
      if (
        feature_combination.every((item) => required_features.includes(item))
      ) {
        required_files.push(path);
      }
    }
  }
  return required_files;
}

export function get_templated(template, parameters, str = false) {
  // Get the given template filled with the chosen keywords

  let env = nunjucks.configure(TEMPLATES_PATH, {
    autoescape: true,
    throwOnUndefined: true,
    trim_blocks: true,
    lstrip_blocks: true,
  });

  if (str) {
    return env.renderString(template, parameters);
  } else {
    return env.render(template, parameters);
  }
}

export function gen_env_template(selected_features, selected_keywords) {
  // Get the given template filled with the chosen keywords

  let required_env_vars = get_required_env_vars(selected_features);
  let env_template = "";
  for (let env_var of required_env_vars) {
    env_template +=
      env_var.slice(3) +
      "=" +
      (env_var in selected_keywords
        ? selected_keywords[env_var]
        : config_feature_keywords[env_var]["default"]) +
      "\n";
  }
  return env_template;
}

export function gen_files(selected_features, selected_keywords) {
  //Generate templated files for the selected features
  // Args:
  //     selected_features (Array)
  //     selected_keywords (Object)
  //         {
  //             'FS_KEYWORD': SelectedKeyWordValue,
  //             'FS_KEYWORD': ...,
  //         }
  // Returns:
  //     output (Object)
  //         {
  //             'filePath': String,
  //             'fileContents': String,
  //         }

  let output = {};

  // Config used to generate these files
  let config = {
    selected_features: selected_features,
    selected_keywords: selected_keywords,
  };

  config["generator_info"] = {
    previous: {
      selected_features: selected_features,
      selected_keywords: selected_keywords,
      version: VERSION,
    },
  };

  let required_files = get_required_files(selected_features);

  // Create templated versions of the files that are needed
  for (let [k, v] of Object.entries(config_feature_keywords_derived)) {
    selected_keywords[k] = v(selected_keywords);
  }

  let template_values = selected_keywords;
  template_values["render_features"] = {};
  for (let feature of ALL_FEATURES) {
    template_values["render_features"][feature] = selected_features.includes(
      feature
    );
  }

  for (let required_file of required_files) {
    let required_file_templated_path = get_templated(
      config_feature_paths[required_file]["template"],
      template_values,
      true
    );

    output[required_file_templated_path] = {
      directory: false,
      binary: false,
      contents: "",
    };
    if (required_file.endsWith("/")) {
      output[required_file_templated_path].directory = true;
    } else if (config_feature_paths[required_file]["binary"]) {
      output[required_file_templated_path].binary = true;
      output[required_file_templated_path].contents = required_file;
    } else {
      output[required_file_templated_path].contents = get_templated(
        required_file,
        template_values
      );
    }
  }
  return output;
}

export function gen_zip_output(
  output_obj,
  env_file = "",
  zipName = "webapp",
  download = true
) {
  var zip = new JSZip();

  let orderedFiles = Object.keys(output_obj).sort();

  for (let item of orderedFiles) {
    if (output_obj[item].directory) {
      // Skip, using abs paths
    } else if (output_obj[item].binary) {
      // TODO: copy file
    } else {
      zip.file(item, output_obj[item].contents);
    }
  }
  zip.file(".env", env_file);

  if (download) {
    zip.generateAsync({ type: "blob" }).then(function(content) {
      saveAs(content, zipName + ".zip");
    });
  } else {
    return zip;
  }
}
