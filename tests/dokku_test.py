import unittest

from dokku_dashboard.dokku import get_apps, format_stdout


class DokkuTest(unittest.TestCase):
    def test_get_apps_should_return_dokku_cmd(self):
        cmd = get_apps()

        assert cmd == 'dokku --quiet apps:list'

    def test_format_stdout_should_return_striped_list(self):
        stdout = """nice_app
        good_app"""

        apps_list = format_stdout(stdout)

        assert apps_list == ['nice_app', 'good_app']

