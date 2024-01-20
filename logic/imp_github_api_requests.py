import random

import requests
from infra.utils import convert_text_json_to_dict, convert_dict_to_string_json

from faker import Faker

fake = Faker()


def generate_issue_create_body(**kwargs):
    return {
        "title": kwargs.get("title", fake.sentence()),
        "body": kwargs.get("body", fake.sentence()),
        "assignees": kwargs.get("assignees", [fake.name() for _ in range(10)]),
        "labels": kwargs.get("labels", [fake.name() for _ in range(10)])
    }


def generate_issue_update_body(**kwargs):
    body_res = generate_issue_create_body(**kwargs)

    return {
        **body_res,
        "state": kwargs.get("state", random.choice(["open", "closed"])),
        "state_reason": kwargs.get("state_reason", random.choice(["completed", "not_planned", "reopened", None])),
    }


def get_list_of_issues(url, token, logger):
    logger.info(f"\n\n URL GET: {url} \n\n")
    res = requests.get(url=url)
    logger.info(f"\n\n status code = {res.status_code} \n\n")

    convert_to_dict_res = convert_text_json_to_dict(res.text)
    logger.info(f"\n\n Got Result {convert_to_dict_res} \n\n")

    logger.info(f"\n\n The number of returned issues are {len(convert_to_dict_res)} \n\n")

    return res.status_code, res.ok, convert_to_dict_res


def create_issue(url, token, logger, **kwargs):
    logger.info(f"\n\n Create Issue \n\n")
    logger.info(f"\n\n URL POST: {url} \n\n")

    body = generate_issue_create_body(**kwargs)
    logger.info(f"\n\n Generated body request: \n {body} \n\n")

    res = requests.post(url=url, json=convert_dict_to_string_json(body))
    logger.info(f"\n\n status code = {res.status_code} \n\n")

    convert_to_dict_res = convert_text_json_to_dict(res.text)
    logger.info(f"\n\n Got Result {convert_to_dict_res} \n\n")

    logger.info(f"\n\n The number of returned issues are {len(convert_to_dict_res)} \n\n")

    return res.status_code, res.ok, convert_to_dict_res


def update_issue(url, token, logger, **kwargs):
    logger.info(f"\n\n Update Issue \n\n")
    logger.info(f"\n\n URL PATCH: {url} \n\n")

    body = generate_issue_update_body(**kwargs)
    logger.info(f"\n\n Generated body request: \n {body} \n\n")

    res = requests.patch(url=url, json=convert_dict_to_string_json(body))
    logger.info(f"\n\n status code = {res.status_code} \n\n")

    convert_to_dict_res = convert_text_json_to_dict(res.text)
    logger.info(f"\n\n Got Result {convert_to_dict_res} \n\n")

    logger.info(f"\n\n The number of returned issues are {len(convert_to_dict_res)} \n\n")

    return res.status_code, res.ok, convert_to_dict_res