import spacy
import requests
import json

ADMIN_HOST = "http://3.133.79.171:5000"
#ADMIN_HOST = "http://localhost:5000"

def save_link(link):
    #llamar base de datos
    url = ADMIN_HOST+"/api/v1/link/"
    headers = {'content-type': 'application/json'}
    requestProcessQuestion = {
        "home_page": link['home_page'],
        "title_page": link['title_page'],
        "simple_title_page": link['simple_title_page'],
        "url_page": link['url_page'],
    }

    response = requests.post(url, data=json.dumps(requestProcessQuestion), headers=headers)
    return json.loads(response.text)

def get_questions():
    print("cargando preguntas")

    #llamar base de datos
    url = ADMIN_HOST+"/api/v1/question/"
    headers = {'content-type': 'application/json'}

    response = requests.get(url, headers=headers)
    return json.loads(response.text)

def get_links():
    print("cargando links")

    #llamar base de datos
    url = ADMIN_HOST+"/api/v1/link/"
    headers = {'content-type': 'application/json'}

    response = requests.get(url, headers=headers)
    return json.loads(response.text)



print("cargando modelo")
NLP = spacy.load('es_core_news_md')
ALL_QUESTIONS = get_questions()
ALL_LINKS = get_links()

