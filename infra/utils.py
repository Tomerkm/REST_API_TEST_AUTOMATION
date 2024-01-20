import json
from urllib.parse import urljoin
from requests.models import PreparedRequest
import urllib.parse


def convert_text_json_to_dict(data):
    return json.loads(data)


def url_join_between_paths(*paths):
    url_res = None
    for path in paths:
        url_res = urljoin(url_res, path)

    return url_res


def add_params_to_url(url: str, params: dict):
    req = PreparedRequest()
    req.prepare_url(url, params)

    return req.url


def convert_query_params_to_dict(params: str):
    return urllib.parse.parse_qs(params)


def convert_dict_to_string_json(data):
    return json.dumps(data)
