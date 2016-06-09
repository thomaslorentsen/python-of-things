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


class Todo:
    config = False
    api = False

    task_item = False
    project_id = False
    label_id = False

    def __init__(self):
        self.config = TodoConfig()
        self.api = getApi(self.config.get_config('key'))
        todo_config = getConfig(self.api)
        self.project_id = getProject(todo_config)
        self.label_id = getLabel(todo_config)

    def task(self, message):
        self.task_item = self.api.items.add(message, self.project_id,
                                            date_string='Today', labels=[self.label_id], priority=2)

    def add_reminder(self, key='todoist'):
        self.api.reminders.add(self.task_item['id'], service='email', type='location', name=self.config.get_config('location', key),
                          loc_lat=self.config.get_config('lat', key), loc_long=self.config.get_config('lon', key),
                          loc_trigger='on_enter', radius=100)

    def commit(self):
        print self.api.commit()

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


def add_reminder(id, config, key, api):
    api.reminders.add(id, service='email', type='location', name=config.get_config('location', key), loc_lat=config.get_config('lat', key), loc_long=config.get_config('lon', key), loc_trigger='on_enter', radius=100)


def task(message):
    t = Todo()
    t.task(message)
    t.add_reminder('todoist')
    t.commit()


def task_station(message):
    t = Todo()
    t.task(message)
    t.add_reminder('geo_station')
    t.commit()
