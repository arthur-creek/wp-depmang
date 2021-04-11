import json
import pprint
import configs


class BashCommands:

    @property
    def date(self):
        return self._date

    @property
    def config(self):
        return self._config

    def __init__(self):
        self._config = configs('config.json')
        pprint(self._config)
        with open('configs/commands.json', "r") as read_file:
            commands = json.load('config.commands.json')

        self._commands = {
            'w': commands['restoreDB']
        }

    def get(self, key):
        return self._commands[key]

    # def env(self, key):
    #     env = dict(self._config['env'][key])
    #     env['git'] = self._config['git']
    #     top_dict = dict((i, self._config[i]) for i in self._config if i != 'env')
    #     return {**env, **top_dict}


# print((' '.join(commands['cmd']['backupDB'])).format(config['prod']))


# For testing purposes.
if __name__ == "__main__":
    cmd = BashCommands()
    pprint.pprint(cmd.config)
