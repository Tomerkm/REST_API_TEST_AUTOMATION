import requests
from infra.utils import convert_text_json_to_dict


def generate_issue(**kwargs):

    return {
        "title": kwargs.get("title", ),
        "body": kwargs.get("body", ),
        "assignees": kwargs.get("assignees", ),
        "labels": kwargs.get("labels", )
    }




def get_list_of_issues(url, token, logger):
    logger.info(f"\n\n URL GET: {url} \n\n")
    res = requests.get(url, headers={'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(token)})
    logger.info(f"\n\n status code = {res.status_code} \n\n")

    convert_to_dict_res = convert_text_json_to_dict(res.text)
    logger.info(f"\n\n Got Result {convert_to_dict_res} \n\n")

    logger.info(f"\n\n The number of returned issues are {len(convert_to_dict_res)} \n\n")

    return res.status_code, res.ok, convert_to_dict_res


def create_issue(url, token, logger, **kwargs):
    logger.info(f"\n\n URL POST: {url} \n\n")
    res = requests.post(url, headers={'Content-Type': 'application/json', 'Authorization': 'Bearer {}'.format(token)})
    logger.info(f"\n\n status code = {res.status_code} \n\n")

    convert_to_dict_res = convert_text_json_to_dict(res.text)
    logger.info(f"\n\n Got Result {convert_to_dict_res} \n\n")

    logger.info(f"\n\n The number of returned issues are {len(convert_to_dict_res)} \n\n")

    return res.status_code, res.ok, convert_to_dict_res