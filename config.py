import pprint
from datetime import datetime
from utils import read_json_file


class Config:

    @property
    def date(self):
        return self._date

    @property
    def config(self):
        return self._config

    def __init__(self, configFile):
        self._date = datetime.now().strftime("%Y-%m-%d-%H%M")
        config = read_json_file(configFile)

        self._config = {
            'git': config['git']['url'].format(**config['git']),
            'uploadsZip': config['uploadsZip'].format(date=self._date),
            'env': {}
        }
        for envKey in config['env']:
            env = config['env'][envKey]
            for fName in config['file']:
                env[fName] = config['file'][fName].format(date=self._date, env=envKey)
            self._config['env'][envKey] = env

    def get(self, key):
        return self._config[key]

    def env(self, key):
        env = dict(self._config['env'][key])
        env['git'] = self._config['git']
        top_dict = dict((i, self._config[i]) for i in self._config if i != 'env')
        return {**env, **top_dict}


# For testing purposes.
if __name__ == "__main__":
    conf = Config('configs/env.example.json')
    print(conf.date)
    print('\nAll config')
    pprint.pprint(conf.config)
