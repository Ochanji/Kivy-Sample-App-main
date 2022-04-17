import requests


def get_characters_count(url: str):
    r = requests.get(url)
    if r.ok:
        return len(r.text)

    return 'Cannot reach given URL'


def url_validated(url: str):
    if url.startswith('http://') or url.startswith('https://'):
        return True