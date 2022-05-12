import os
from setuptools import find_packages
from setuptools import setup

from urllib3.util import parse_url


def load_requirements():
    """
    Install dependencies from 'requirements.txt'.

    If the file contains a pip-supported git+https' location for the package,
    this method transforms it to setuptools' way. Some code has been taken from
    https://stackoverflow.com/a/53069528
    """
    thelibFolder = os.path.dirname(os.path.realpath(__file__))
    requirementPath = thelibFolder + '/requirements.txt'
    install_requires = []
    if os.path.isfile(requirementPath):
        with open(requirementPath) as f:
            install_requires = f.read().splitlines()
    install_requires_filtered = []
    for req in install_requires:
        if not req.startswith('#'):
            url_parsed = parse_url(req)
            fragment = url_parsed.fragment
            if fragment:
                fragment = fragment.split('=')[-1]
                req = '@'.join([fragment, req])
            install_requires_filtered.append(req)

    return install_requires_filtered


setup(
    name='report2sqaaas-plugin-{{cookiecutter.plugin_name}}',
    version='1.0.0',
    description='Output validator for the {{cookiecutter.tool_name}} tool',
    author='{{cookiecutter.author}}',
    author_email='{{cookiecutter.author_email}}',
    url='https://github.com/eosc-synergy/sqaaas-reporting-plugins',
    # For a list of valid classifiers, see https://pypi.org/classifiers/
    classifiers=[
        'Intended Audience :: Developers',
        ('License :: OSI Approved :: GNU General Public License v3 or later '
         '(GPLv3+)'),
        'Environment :: Plugins',
        'Development Status :: 3 - Alpha',
    ],
    packages=find_packages(),
    install_requires=load_requirements(),
    entry_points={
        'sqaaas.validators': [
            '{{cookiecutter.plugin_name}} = report2sqaaas_plugins_{{cookiecutter.plugin_name}}.main:{{cookiecutter.plugin_class_name}}', # noqa
        ],
    },
)
