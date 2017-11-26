import os
import unittest

from dokku_dashboard.dokku import get_list_apps_command, format_stdout


class DokkuTest(unittest.TestCase):
    def test_get_list_apps_command_should_return_dokku_cmd(self):
        cmd = get_list_apps_command()

        assert cmd == 'dokku --quiet apps:list'

    def test_format_stdout_should_return_striped_list(self):
        stdout = b"""nice_app
        good_app"""

        apps_list = format_stdout(stdout)

        assert apps_list == ['nice_app', 'good_app']

    def test_format_stdout_should_return_striped_one_item_list(self):
        stdout = b"""nice_app
        """

        apps_list = format_stdout(stdout)

        assert apps_list == ['nice_app']

    def test_format_stdout_should_not_return_dokku_dashboard_app_default_name(self):
        stdout = b"""nice_app
        dokku-dashboard"""

        apps_list = format_stdout(stdout)

        assert apps_list == ['nice_app']

    def test_given_env_var_setted_format_stdout_should_not_return_dokku_dashboard_name(self):
        os.environ['APP_NAME'] = 'great_dashboard'

        stdout = b"""nice_app
        great_dashboard"""

        apps_list = format_stdout(stdout)

        assert apps_list == ['nice_app']
