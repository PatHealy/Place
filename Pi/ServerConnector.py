import urllib.request
import json

class Connector:
    def __init__(self, url):
        self.url = url

    def get_dump(self):
        r = urllib.request.urlopen(self.url)
        return json.loads(r.read().decode(r.info().get_param('charset') or 'utf-8'))
