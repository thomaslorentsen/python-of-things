import todoist
import ConfigParser


class TodoConfig:
    config = False

    def __init__(self):
        self.config = self.__load_config()

    def __load_config(self):
        config = ConfigParser.ConfigParser()
        config.read('config/config.conf')
        return config

    def get_config(self, option, config = 'todoist'):
        return self.config.get(config, option)


def getApi(key):
    return todoist.TodoistAPI(key)


def getConfig(api):
    return api.sync(resource_types=['projects', 'labels'])


def getProject(config, projectName = 'Home'):
    for project in config['Projects']:
        if project['name'] == projectName:
            return project['id']


def getLabel(config, labelName = 'low_energy'):
    for label in config['Labels']:
        if label['name'] == labelName:
            return label['id']


def todo():
    config = TodoConfig()
    api = getApi(config.get_config('key'))
    todoconfig = getConfig(api)
    projectId = getProject(todoconfig)
    labelId = getLabel(todoconfig)
    item = api.items.add('Empty the washing machine', projectId, date_string='Today', labels=[labelId], priority=2)
    reminder = api.reminders.add(item['id'], service='email', type='location', name=config.get_config('location'), loc_lat=config.get_config('lat'), loc_long=config.get_config('lon'), loc_trigger='on_enter', radius=100)
    print api.commit()

def task(message):
    config = TodoConfig()
    api = getApi(config.get_config('key'))
    todoconfig = getConfig(api)
    projectId = getProject(todoconfig)
    labelId = getLabel(todoconfig)
    item = api.items.add(message, projectId, date_string='Today', labels=[labelId], priority=2)
    reminder = api.reminders.add(item['id'], service='email', type='location', name=config.get_config('location'), loc_lat=config.get_config('lat'), loc_long=config.get_config('lon'), loc_trigger='on_enter', radius=100)
    print api.commit()

def task_station(message):
    config = TodoConfig()
    api = getApi(config.get_config('key'))
    todoconfig = getConfig(api)
    projectId = getProject(todoconfig)
    labelId = getLabel(todoconfig)
    item = api.items.add(message, projectId, date_string='Today', labels=[labelId], priority=2)
    reminder = api.reminders.add(item['id'], service='email', type='location', name=config.get_config('location', 'geo_station'), loc_lat=config.get_config('lat', 'geo_station'), loc_long=config.get_config('lon', 'geo_station'), loc_trigger='on_enter', radius=100)
    print api.commit()