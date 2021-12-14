## #1 Generate the SQAaaS reporting plugin's module

### Use cookiecuttter template
If not already in your environment, install 
[cookiecutter](https://cookiecutter.readthedocs.io/) executable:
```console
$ pip install cookiecutter
```

Now you are ready to create the validator plugin module using the 
template from this repository:
```console
$ cookiecutter https://github.com/EOSC-synergy/sqaaas-reporting-cookiecutter
```

### The module structure
The following folder structure is created by cookiecutter:
```console
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

## #2 Implement the validate() method
In order to have a working plugin, the **`validate()` method has to be implemented**
within the generated validator class (within `main.py` file).

The *validate() method must return a dictionary* containing the validation outcome
through the `valid` key, which is a boolean variable that sets the validation as
successful (`True`) or unsuccessful (`False`). As an example, the most simple
definition of the `validate()` method could be:
```python
class FooValidator(BaseValidator):
    valid = False
       
    @staticmethod
    def validate():
       return {'valid': self.valid}
```

A few things to consider:
  - The *validator class* has the following attributes:
    - `name`: validator name (available as `self.name`)
    - `opts`: object that contains the attributes provided when the class is 
      instantiated. Those are the same as the input arguments of the
      [report2sqaaas](https://github.com/eosc-synergy/reporting-sqaaas) module,
      such as `validator` (available as class attribute `self.opts.validator`),
      `stdout` (`self.opts.stdout`) or `threshold` (`self.opts.threshold`).
  - A reminder that the [available test cases](%7B%7Bcookiecutter.criterion%7D%7D_%7B%7Bcookiecutter.plugin_name%7D%7D/tests/test_validator.py) will only be
    successful when both the i) `validate()` method has been implemented and ii) a
    sample output is provided via the pytest fixture `<tool_name_stdout`>.
    
## #3 Contribute to reporting-sqaaas-plugins
Once you have implemented the validate() method and the tests are passing, you should
contribute to the existing set of validator plugins of the SQAaaS reporting component.
To this end, create a pull request to
[reporting-sqaaas-plugins](https://github.com/eosc-synergy/sqaaas-reporting-plugins).

1. Fork https://github.com/eosc-synergy/sqaaas-reporting-plugins and clone it
2. Copy the validator plugin folder (with the structure from step #1) into the cloned repo
3. Add & commit the changes to your fork
4. Create a PR to the upstream repo (from where the fork has been created)
