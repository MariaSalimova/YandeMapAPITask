from io import BytesIO

import requests
from PIL import Image

API_KEY_GEOCODER = "40d1649f-0493-4b70-98ba-98533de7710b"
API_KEY_SEARCH = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"


def geocode(address):
    geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

    geocoder_params = {
        "apikey": API_KEY_GEOCODER,
        "geocode": address,
        "format": "json"}

    response = requests.get(geocoder_api_server, params=geocoder_params)

    if not response:
        raise f"""Ошибка выполнения запроса: {response.url}
HTTP статус: {response.status_code}({response.reason})"""

    json_response = response.json()
    return json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]


def get_ll_spn(address):
    toponym = geocode(address)
    toponym_coodrinates = toponym["Point"]["pos"]
    # Долгота и широта:
    toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")
    ll = ','.join((toponym_longitude, toponym_lattitude))

    envelope = toponym["boundedBy"]['Envelope']
    l, b = envelope['lowerCorner'].split(' ')
    r, t = envelope["upperCorner"].split(' ')
    dx, dy = str(abs(float(l) - float(r)) / 2), str(abs(float(b) - float(t)) / 2)
    spn = ','.join((dx, dy))
    return ll, spn


def show_map(ll, z, map_type="map", add_params=None):
    map_params = {
        "ll": ll,
        "z": z,
        "l": map_type
    }

    if isinstance(add_params, dict):
        map_params.update(add_params)

    map_api_server = "http://static-maps.yandex.ru/1.x/"
    response = requests.get(map_api_server, params=map_params)
    # print(response.status_code)
    # Image.open(BytesIO(response.content)).show()
    return response.content


def find_organization(ll, request, lang="ru_RU"):
    search_api_server = "https://search-maps.yandex.ru/v1/"
    search_param = {
        "apikey": API_KEY_SEARCH,
        "text": request,
        "ll": ll,
        "lang": lang
    }
    response = requests.get(search_api_server, search_param)
    if not response:
        raise f"""Ошибка выполнения запроса: {response.url}
    HTTP статус: {response.status_code}({response.reason})"""
    response = response.json()
    organization = response["features"]
    return organization


def find_nearst_organization(ll, request, lang="ru_RU"):
    organization = find_organization(ll, request, lang=lang)
    if len(organization):
        return organization[0]
