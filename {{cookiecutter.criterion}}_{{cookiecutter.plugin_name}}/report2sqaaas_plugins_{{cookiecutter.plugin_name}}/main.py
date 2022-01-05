import logging

from report2sqaaas import utils as sqaaas_utils


logger = logging.getLogger('sqaaas.reporting.plugins.{{cookiecutter.plugin_name }}')


class {{cookiecutter.plugin_class_name}}(sqaaas_utils.BaseValidator):
    valid = False

    {%- if cookiecutter.has_threshold == True %}
    @staticmethod
    def populate_parser(parser):
        parser.add_argument(
            '--threshold',
            metavar='NUMBER',
            type=int,
            help=(
                'Optional argument required by some plugins in order to state '
                'whether the validation is successful'
            )
        )

    {%- endif %}
