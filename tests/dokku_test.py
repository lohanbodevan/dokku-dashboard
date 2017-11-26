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

