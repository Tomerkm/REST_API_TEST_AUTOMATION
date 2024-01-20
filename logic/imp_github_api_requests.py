import requests
from infra.utils import convert_text_json_to_dict, convert_dict_to_string_json

from faker import Faker
fake = Faker()

def generate_issue(**kwargs):

    return {
        "title": kwargs.get("title", fake.sentence()),
        "body": kwargs.get("body", fake.sentence()),
        "assignees": kwargs.get("assignees", [fake.name() for _ in range(10)]),
        "labels": kwargs.get("labels", [fake.name() for _ in range(10)])
    }


# headers={'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(token)}

def get_list_of_issues(url, token, logger):
    logger.info(f"\n\n URL GET: {url} \n\n")
    res = requests.get(url=url)
    logger.info(f"\n\n status code = {res.status_code} \n\n")

    convert_to_dict_res = convert_text_json_to_dict(res.text)
    logger.info(f"\n\n Got Result {convert_to_dict_res} \n\n")

    logger.info(f"\n\n The number of returned issues are {len(convert_to_dict_res)} \n\n")

    return res.status_code, res.ok, convert_to_dict_res


def create_issue(url, token, logger, **kwargs):

    logger.info(f"\n\n URL POST: {url} \n\n")

    body = generate_issue(**kwargs)

    res = requests.post(url=url, json=convert_dict_to_string_json(body))
    logger.info(f"\n\n status code = {res.status_code} \n\n")

    convert_to_dict_res = convert_text_json_to_dict(res.text)
    logger.info(f"\n\n Got Result {convert_to_dict_res} \n\n")

    logger.info(f"\n\n The number of returned issues are {len(convert_to_dict_res)} \n\n")

    return res.status_code, res.ok, convert_to_dict_res