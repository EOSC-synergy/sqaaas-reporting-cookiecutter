# SQAaaS reporting validator plugin for the {{cookiecutter.tool_name}} tool

[![License](https://img.shields.io/github/license/fzhu2e/GraphEM)](https://opensource.org/licenses/GPL-3.0)

* [Description](#description)
* [Installation](#installation)
* [Testing](#testing)
* [Trying it out](#trying-it-out)
* [Contribution](#contribution)
* [License](#license)


## Description
{{cookiecutter.description}}

## Installation
The plugin can be installed from this repository using `pip`:
```
$ pip install git+https://github.com/EOSC-synergy/sqaaas-reporting-plugins@main#egg=report2sqaaas-plugin-{{cookiecutter.plugin_name}}&subdirectory={{cookiecutter.criterion}}_{{cookiecutter.plugin_name}}
```

Note that you will need to have the
[report2sqaaas](https://github.com/eosc-synergy/sqaaas-reporting) module
deployed in your environment for the plugin to work. To this end, you can
use the [requirements.txt](requirements.txt) file included with this package:
```
$ pip install -r requirements.txt
```

## Testing
Use [pytest](https://pytest.org/) module to run the test cases:
```
$ pytest
```

## Trying it out
The plugin can be readily used through the CLI offered by the
[report2sqaaas](https://github.com/eosc-synergy/sqaaas-reporting) module:
```
$ report2sqaaas {{cookiecutter.plugin_name}} {{cookiecutter.tool_name}}.stdout
```

## Configuration
No additional configuration is needed. The plugin is added to the
`sqaaas.validators` namespace, which is scoped by the
[report2sqaaas](https://github.com/eosc-synergy/sqaaas-reporting) application.

## Contribution
Please check our [guidelines](CONTRIBUTING.md) on how to contribute.

## License
[GNU GENERAL PUBLIC LICENSE v3](LICENSE)
