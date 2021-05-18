

import os

from tornado.websocket import WebSocketHandler
from tornado.web import RequestHandler, StaticFileHandler, Application, url
from tornado.httpclient import AsyncHTTPClient
from tornado.httputil import url_concat
from tornado.escape import json_decode
from tornado import ioloop

from rx import operators as ops
from rx.subject import Subject
from rx.scheduler.eventloop import IOLoopScheduler

scheduler = IOLoopScheduler(ioloop.IOLoop.current())


def search_wikipedia(term):
    url = 'http://en.wikipedia.org/w/api.php'

    params = {
        "action": 'opensearch',
        "search": term,
        "format": 'json'
    }
    user_agent = "RxPY/3.0 (https://github.com/dbrattli/RxPY; dag@brattli.net) Tornado/4.0.1"

    url = url_concat(url, params)

    http_client = AsyncHTTPClient()
    return http_client.fetch(url, method='GET', user_agent=user_agent)


class WSHandler(WebSocketHandler):
    def open(self):
        print("WebSocket opened")


        self.stream = Subject()

        searcher = self.stream.pipe(
            ops.map(lambda x: x["term"]),
            ops.filter(lambda text: len(text) > 2),  
            ops.debounce(0.750),                     
            ops.distinct_until_changed(),           
            ops.flat_map_latest(search_wikipedia)
        )

        def send_response(x):
            self.write_message(x.body)

        def on_error(ex):
            print(ex)

        searcher.subscribe(send_response, on_error, scheduler=scheduler)

    def on_message(self, message):
        obj = json_decode(message)
        self.stream.on_next(obj)

    def on_close(self):
        print("WebSocket closed")


class MainHandler(RequestHandler):
    def get(self):
        self.render("index.html")


def main():
    port = os.environ.get("PORT", 8080)
    app = Application([
        url(r"/", MainHandler),
        (r'/ws', WSHandler),
        (r'/static/(.*)', StaticFileHandler, {'path': "."})
    ])
    print("Starting server at port: %s" % port)
    app.listen(port)
    ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
