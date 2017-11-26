import subprocess

from dokku_dashboard.dokku_cmds import Dokku


def get_list_apps_command():
    apps = Dokku().apps
    apps.parent_cmd.quiet()
    return str(apps)


def format_stdout(stdout):
    decoded = stdout.decode('utf-8')
    return [i.strip() for i in decoded.split('\n')]


def list_apps():
    cmd = get_list_apps_command()
    result = subprocess.run(cmd.split(), stdout=subprocess.PIPE)
    return format_stdout(result.stdout)
