from tornado.web import RequestHandler
from tornado.httpclient import AsyncHTTPClient

class SmokeTestHandler(RequestHandler):
    def get(self):
        self.write({"hello": "world"})

class GetHandler(RequestHandler):
    async def get(self):
        http = AsyncHTTPClient()
        results = await http.fetch("http://py-api-srv:8000/dog")
        self.write(results.body)
 