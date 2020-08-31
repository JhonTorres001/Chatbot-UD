import pystache
from ..files.s3_files import *


class NluProccesor:

    PATH_FILE = "data/nlu.md"

    def __init__(self, stories):
        self.stories = stories

    def proccess(self):

        template = """{{#nlus}}

## {{type_nlu}}:{{name}}
{{#value}}
- {{.}}
{{/value}}
{{/nlus}}
"""
        result = pystache.render(template, {'nlus': self.stories})
        upload_file(NluProccesor.PATH_FILE, result)
        print(result)
