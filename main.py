import tornado.ioloop
import tornado.web

import todo
import mpc


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")


class TestHandler(tornado.web.RequestHandler):
    def get(self, name):
        self.write("Hello %s" % name)


class WashingHandler(tornado.web.RequestHandler):
    def get(self):
        todo.todo()
        self.write("Success")


class WashingMpcPlay(tornado.web.RequestHandler):
    def get(self):
        mpc.play()
        self.write("Success")


class WashingMpcPause(tornado.web.RequestHandler):
    def get(self):
        mpc.pause()
        self.write("Success")

class TodoRemindMe(tornado.web.RequestHandler):
    def post(self):
        message = self.request.body
        todo.task(message)
        self.write("Success")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
        (r"/test/([a-z]+)", TestHandler),
        (r"/washing", WashingHandler),
        (r"/mpc/play", WashingMpcPlay),
        (r"/mpc/pause", WashingMpcPause),
        (r"/todo/remind/me", TodoRemindMe),
    ])


if __name__ == "__main__":
    app = make_app()
    app.listen(5000)
    tornado.ioloop.IOLoop.current().start()
