import requests


def get_word(word):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)
    word_response = [response.json()[0]['word'], response.json()[0]['meanings'][0]['definitions'][0]['definition']]
    return word_response


