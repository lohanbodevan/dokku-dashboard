from pytocli import (CommandBuilder, Option, SubCommand,
                     NoValueOption, SubCommandBuilder)


class DokkuSubCommand(SubCommandBuilder):
    @property
    def dokku(self):
        return self.parent_cmd


class Apps(DokkuSubCommand):
    name = 'apps:list'


class Dokku(CommandBuilder):
    name = 'dokku'

    # Options
    quiet = Option(NoValueOption, '--quiet', 'Quiet mode')

    # SubCommands
    apps = SubCommand(Apps)
