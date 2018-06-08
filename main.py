import tornado.ioloop
import tornado.web

import todo
import mpc


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello World")


class TestHandler(tornado.web.RequestHandler):
    def get(self, name):
        self.write("Hello %s" % name)


class MpcPlay(tornado.web.RequestHandler):
    def get(self):
        mpc.play()
        self.write("Done")


class MpcPause(tornado.web.RequestHandler):
    def get(self):
        mpc.pause()
        self.write("Done")


class TodoRemindMe(tornado.web.RequestHandler):
    def post(self):
        message = self.request.body
        todo.task(message)
        self.write("Done")


class TodoRemindMeAtStation(tornado.web.RequestHandler):
    def post(self):
        message = self.request.body
        todo.task_station(message)
        self.write("Done")


class TodoRemindMeAtCity(tornado.web.RequestHandler):
    def post(self):
        message = self.request.body
        todo.task_city(message)
        self.write("Done")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/test/([a-z]+)", TestHandler),
        (r"/mpc/play", MpcPlay),
        (r"/mpc/pause", MpcPause),
        (r"/todo/remind/me", TodoRemindMe),
        (r"/todo/remind/me/at/country", TodoRemindMe),
        (r"/todo/remind/me/at/station", TodoRemindMeAtStation),
        (r"/todo/remind/me/at/city", TodoRemindMeAtCity),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(5000)
    tornado.ioloop.IOLoop.current().start()
