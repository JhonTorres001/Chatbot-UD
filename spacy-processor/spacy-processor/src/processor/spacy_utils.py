import unidecode
from .spacy_constants import *
import uuid

import requests
from bs4 import BeautifulSoup

tokens_excluded = [
    "next",
    "page",
    ">",
    "<",
    "prev",
    "previous",
]

titles_excluded = [
    "Página anterior‹‹",
    "Página anterior‹‹",
    "Next page››",
]


def process_question(question):
    question = unidecode.unidecode(question)
    question_nlp = NLP(question.lower())
    result = []
    for token in question_nlp:
        if token.text in tokens_excluded:
            continue
        if token.text in NLP.Defaults.stop_words:
            continue
        if token.is_punct:
            continue
        if token.lemma_ == '-PRON-':
            continue
        result.append(token.lemma_)
    return " ".join(result)


def is_excluded(title_url):
    for title in titles_excluded:
        if title in title_url:
            return True

    return False


def is_valid_link(initial_url, link):
    if 'href' in link.attrs.keys() \
            and not "#" in link['href'] \
            and not link['href'].endswith(".pdf") \
            and not link['href'].endswith(".mp3") \
            and not link['href'].endswith(".mp4") \
            and not link['href'].endswith(".doc") \
            and not link['href'].endswith(".docx") \
            and not link['href'].endswith("index") \
            and not link['href'] == '/' \
            and (link['href'].startswith(initial_url)
                 or link['href'].startswith("/")):
        return True
    return False


def clean_url(value_url):
    return value_url.replace('\n', '') \
        .replace("Leer más... ", "") \
        .replace("Leer más... de ", "") \
        .strip()


def visit_url(initial_url, links_visited, url, links_found):
    response_url = requests.get(url)
    soup = BeautifulSoup(response_url.text, "html.parser")
    links = soup.findAll('a')

    for link in links:
        if is_valid_link(initial_url, link) and not is_excluded(link.text) and link['href'] not in links_visited:
            links_visited.add(link['href'])
            link_temp = link['href']
            if link['href'].startswith('/'):
                link_temp = initial_url + link['href']
            print((clean_url(link.text), link_temp))

            simple_title_page = process_question(clean_url(link.text))

            if simple_title_page.strip() != "" and len(simple_title_page.strip().split(" ")) > 5:
                # save link
                save_link({
                    "home_page": initial_url,
                    "title_page": clean_url(link.text),
                    "simple_title_page": simple_title_page,
                    "url_page": link_temp,
                })

            visit_url(initial_url, links_visited, link_temp, links_found)


def consolidate_links(links_found):

    res = {}
    for item in links_found:
        res.setdefault(item['simple_title_page'], []).append(item)

    print(res)

    for key in res.keys():
        links = res.get(key)

        if len(links) > 0:
            home_page = links[0]["home_page"]
            title_page = ''
            simple_title_page = key
            url_page = ''

            for link in links:
                title_page += link['title_page']+", "
                url_page += link['title_page'] + " -> " + link['url_page'] + '/n'

            save_link({
                    "home_page": home_page,
                    "title_page": title_page,
                    "simple_title_page": simple_title_page,
                    "url_page": url_page,
                })













