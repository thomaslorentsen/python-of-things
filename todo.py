import todoist
import ConfigParser


class TodoConfig:
    config = False

    def __init__(self):
        self.config = self.__load_config()

    @staticmethod
    def __load_config():
        config = ConfigParser.ConfigParser()
        config.read('config/config.conf')
        return config

    def get_config(self, option, config='todoist'):
        return self.config.get(config, option)


class Todo:
    config = False
    api = False

    todo_config = False

    task_item = False
    project_id = False
    label_id = False

    def __init__(self):
        self.config = TodoConfig()
        self.api = self.__get_api(self.config.get_config('key'))
        self.todo_config = self.__get_config()
        self.project_id = self.__get_project(self.config.get_config('project'))
        self.label_id = self.__get_label()

    @staticmethod
    def __get_api(key):
        return todoist.TodoistAPI(key)

    def __get_config(self):
        return self.api.sync(resource_types=['projects', 'labels'])

    def __get_project(self, project_name='Personal'):
        for project in self.todo_config['Projects']:
            if project['name'] == project_name:
                return project['id']

    def __get_label(self, label_name='low_energy'):
        for label in self.todo_config['Labels']:
            if label['name'] == label_name:
                return label['id']

    def task(self, message):
        task_tuple = {'date_string': 'Today',
                'labels': [self.label_id],
                'priority': 2}
        self.task_item = self.api.items.add(message, self.project_id, **task_tuple)

    def add_reminder(self, key='todoist'):
        reminder_tuple = {'service': 'email',
                    'type': 'location',
                    'name': self.config.get_config('location', key),
                    'loc_lat': self.config.get_config('lat', key),
                    'loc_long': self.config.get_config('lon', key),
                    'loc_trigger': 'on_enter',
                    'radius': 100}
        self.api.reminders.add(self.task_item['id'], **reminder_tuple)

    def commit(self):
        print self.api.commit()


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
