from .spacy_utils import *
from marshmallow import fields, Schema


class SpacyWebPageProcessor:

    # class constructor
    def __init__(self, data):
        """
        Class constructor
        """
        if 'url_page' in data.keys():
            self.url_page = data.get('url_page')

        if 'title' in data.keys():
            self.title = data.get('title')

        self.simple_title = ""
        self.url_page_found = ""
        self.score = 0.0
        self.status = ""

    def process_page(self):
        links_visited = set()
        links_found = list()
        visit_url(self.url_page, links_visited, self.url_page, links_found)
        consolidate_links(links_found)

    def find_similarity_page(self):
        link_nlp = NLP(process_question(self.title))
        answers = list()

        for stored_link in ALL_LINKS:
            stored_link_nlp = NLP(stored_link['simple_title_page'])
            score_found = link_nlp.similarity(stored_link_nlp)
            if score_found > 0.9:
                link_found = dict(stored_link)
                link_found["score"] = score_found
                answers.append(link_found)

        if len(answers) > 0:
            best_answer = max(answers, key=lambda x: x['score'])
            self.status = "FOUND"
            self.simple_title = best_answer['simple_title_page']
            self.title = best_answer['title_page']
            self.url_page = best_answer['url_page']
            self.score = best_answer['score']
        else:
            self.url_page =  ""
            self.status = "NOT_FOUND"

    def __repr(self):
        return '<id {}>'.format(self.title)

    def __repr(self):
        return '<id {}>'.format(self.title)


class SpacyWebPageProcessorSchema(Schema):

    url_page = fields.Str(required=True)


class SpacyWebPageFindProcessorSchema(Schema):

    title = fields.Str(required=True)
    simple_title = fields.Str(dump_only=True)
    url_page = fields.Str(dump_only=True)
    score = fields.Str(dump_only=True)
    status = fields.Str(dump_only=True)
