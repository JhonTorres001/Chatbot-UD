import pystache
from ..files.s3_files import *


class DomainProccesor:

    PATH_FILE = "domain.yml"

    def __init__(self, nlus, templates):
        self.nlus = nlus
        self.templates = templates

    def proccess(self):

        template_yml = """
{{#data}}
intents:
{{#nlus}}
  - {{name}}
{{/nlus}}

actions:
{{#templates}}
- {{tem_name}}
{{/templates}}


templates:
{{#templates}}
  {{tem_name}}:
  {{#items}}
  - {{item_type}}: "{{item_value}}"
  {{/items}}
{{/templates}}

{{/data}}
"""
        result = pystache.render(template_yml, {'data': {
            'nlus' : self.nlus,
            'templates': self.templates}})
        upload_file(DomainProccesor.PATH_FILE, result)
        print(result)


