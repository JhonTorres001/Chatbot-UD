import pystache
from ..files.s3_files import *


class StoryProccesor:

    PATH_FILE = "data/stories.md"

    def __init__(self, stories):
        self.stories = stories

    def proccess(self):

        template = """
{{#stories}}

## {{name_story}}
{{content_story}}

{{/stories}}
        """
        result = pystache.render(template, {'stories': self.stories})
        upload_file(StoryProccesor.PATH_FILE, result)
        print(result)





