import todoist
import ConfigParser
import re


class TodoConfig:
    config = False

    def __init__(self):
        self.config = self.__load_config()

    @staticmethod
    def __load_config():
        config = ConfigParser.ConfigParser()
        config.read('config/config.ini')
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
            if project['name'] == project_name.lstrip('#'):
                return project['id']

    def __get_label(self, label_name='ifttt'):
        for label in self.todo_config['Labels']:
            if label['name'] == label_name.lstrip('@'):
                return label['id']

    def task(self, message):
        message, labels = self.parse_labels(message)
        labels += [self.label_id]
        message, project = self.parse_project(message)
        task_tuple = {'date_string': 'Today',
                'labels': labels,
                'priority': 2}
        self.task_item = self.api.items.add(message, project, **task_tuple)

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

    def parse_project(self, message):
        """
        Parse project from message and returns id
        """
        matches = re.findall('#[A-Za-z_]+', message)
        for match in matches:
            project = self.__get_project(match)
            if project is not None:
                message = ''.join(re.split(match + ' ?', message))
                return message, project
        return message, self.project_id

    def parse_labels(self, message):
        """
        Parses labels from message and returns an array of ids
        """
        matches = re.findall('@[a-z_]+', message)
        labels = []
        for match in matches:
            label_id = self.__get_label(match)
            if label_id is not None:
                message = ''.join(re.split(match + ' ?', message))
                labels.append(label_id)
        return message, labels


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


def task_city(message):
    t = Todo()
    t.task(message)
    t.add_reminder('geo_city')
    t.commit()
