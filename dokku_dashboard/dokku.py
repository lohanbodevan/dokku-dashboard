import subprocess

from dokku_dashboard.dokku_cmds import Dokku


def get_apps():
    apps = Dokku().apps
    apps.parent_cmd.quiet()
    return str(apps)


def format_stdout(stdout):
    return [i.strip() for i in stdout.split('\n')]


def list_apps():
    apps = get_apps()
    result = subprocess.run([apps], stdout=subprocess.PIPE)
    return format_stdout(result.stdout)
