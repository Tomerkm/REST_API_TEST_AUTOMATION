import configparser
import sys

import pytest
from definitions import CONFIG_FILE_NAME
import logging

from infra.utils import url_join_between_paths

mapping_logging_level = \
    {
        "NOTSET": logging.NOTSET,
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "ERROR": logging.ERROR,
        "CRITICAL": logging.CRITICAL
    }


@pytest.fixture(scope="function")
def get_config():
    config_obj = configparser.ConfigParser()
    config_obj.read(CONFIG_FILE_NAME)

    return config_obj


@pytest.fixture(scope="function")
def get_test_name(request):
    return request.node.name


@pytest.fixture(scope="function")
def get_logger(get_test_name, get_config):
    logger = logging.getLogger(name=get_test_name)

    log_level = mapping_logging_level[get_config["LOG_CONFIG"]["level"].upper().replace(" ", "")]
    formatter = get_config["LOG_CONFIG"]["formatter"].lower()
    date_formatter = get_config["LOG_CONFIG"]["date_formatter"]

    # Set the threshold logging level of the logger to INFO
    logger.setLevel(level=log_level)
    # Create a stream-based handler that writes the log entries
    # into the standard output stream
    handler = logging.StreamHandler(stream=sys.stdout)
    # Create a formatter for the logs
    formatter = logging.Formatter(fmt=formatter, datefmt=date_formatter)
    # Set the created formatter as the formatter of the handler
    handler.setFormatter(fmt=formatter)
    # Add the created handler to this logger
    logger.addHandler(hdlr=handler)

    return logger


@pytest.fixture(scope="function")
def get_github_api_url(get_config):
    return get_config["ROOT_URL"]["github_api_url"]


@pytest.fixture(scope="function")
def get_github_api_issues_url(get_config):
    repo_owner = get_config["PARAM_INFO"]["repository_owner"]
    repo_name = get_config["PARAM_INFO"]["repository_name"]

    get_issues_url_with_owners_and_name = get_config["GITHUB_METHODS"]["get_issues_url"].format(repo_owner, repo_name)

    return url_join_between_paths(get_config["ROOT_URL"]["github_api_url"], get_issues_url_with_owners_and_name)


@pytest.fixture(scope="function")
def get_github_api_update_issue_url(get_config):
    repo_owner = get_config["PARAM_INFO"]["repository_owner"]
    repo_name = get_config["PARAM_INFO"]["repository_name"]
    issue_number = get_config["PARAM_INFO"]["issue_num"]

    get_update_url_with_params = get_config["GITHUB_METHODS"]["update_issue_url"].format(repo_owner, repo_name,
                                                                                         issue_number)

    return url_join_between_paths(get_config["ROOT_URL"]["github_api_url"], get_update_url_with_params)
