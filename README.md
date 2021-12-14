### Generate the Python module for the validator plugin
If not already in your environment, install 
[cookiecutter](https://cookiecutter.readthedocs.io/) executable:
```
$ pip install cookiecutter
```

Now you are ready to create the validator plugin module:
```
$ cookiecutter https://github.com/EOSC-synergy/sqaaas-reporting-cookiecutter
```

### The module structure
The following folder structure is created by cookiecutter:
```
└── {{cookiecutter.criterion}}_{{cookiecutter.plugin_name}}
    ├── CONTRIBUTING.md
    ├── LICENSE
    ├── README.md
    ├── report2sqaaas_plugins_{{cookiecutter.plugin_name}}
    │   ├── __init__.py
    │   ├── main.py
    ├── requirements.txt
    ├── setup.cfg
    ├── setup.py
    ├── test-requirements.txt
    └── tests
        └── test_validator.py
```

### A note about testing
A test-driven development (TDD) approach is followed in order to make sure that
the main validator class, `validate()`, has been defined. Thus, the generated 
module provides two test cases out of the box:
- `validate()` method has been implemented.
- `validate()` method returns a dictionary with the `valid` flag.

*Note: the plugin developer needs to provide a sample output of the tool* (within the
fixture `<tool_name>_stdout`)
