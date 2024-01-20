from infra.utils import convert_query_params_to_dict, add_params_to_url
from logic.imp_github_api_requests import get_list_of_issues


def test_issues_api(get_github_api_url, get_config, get_logger, get_test_name, get_github_api_issues_url):
    # PART ONE

    NUMBER_OF_ISSUES = 3
    status_code, is_success, response = get_list_of_issues(url=get_github_api_issues_url,
                                                           token=get_config["TOKEN_INFO"]["token_val"],
                                                           logger=get_logger)

    assert is_success, f"status code is invalid, its should be equal to 2xx, and not to {status_code}"
    assert len(response) == NUMBER_OF_ISSUES, f"There are exactly {NUMBER_OF_ISSUES} issues"

    # PART TWO

    NUMBER_OF_ISSUES_FOR_LABEL = 1
    LABEL_NAME = "practice1"

    params_as_dict = convert_query_params_to_dict(get_config["PARAM_INFO"]["query_param_for_list_of_issues"])
    api_issues_url_with_query = add_params_to_url(get_github_api_issues_url, params_as_dict)

    status_code, is_success, response = get_list_of_issues(url=api_issues_url_with_query,
                                                           token=get_config["TOKEN_INFO"]["token_val"],
                                                           logger=get_logger)

    assert is_success, f"status code is invalid, its should be equal to 2xx, and not to {status_code}"
    assert len(response) == NUMBER_OF_ISSUES_FOR_LABEL, f"There is exactly {NUMBER_OF_ISSUES_FOR_LABEL} issue for label {LABEL_NAME}"
    assert response[0]["labels"][0]["name"] == LABEL_NAME, f"label name should be {LABEL_NAME}"

    # PART THREE
