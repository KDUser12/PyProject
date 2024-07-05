import requests


def get_latest_version(repository, current_version):
    """Get the latest version of the repository from GitHub.

    :param repository:          Name of the GitHub repository.
    :param current_version:     Current version of the application.

    :return:                    Returns a potential update or possible error."""
    url = "https://api.github.com/repos/KDUser12/{}/releases/latest".format(repository)

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        latest_version = data["tag_name"]
    except requests.exceptions.RequestException as error:
        return error
    return get_result_version(current_version, latest_version)


def get_result_version(current_version, latest_version):
    """Check if a new version is available.

    :param current_version:     Current version of the application.
    :param latest_version:      Latest version fetched from GitHub.

    :return:                    Returns a potential update."""
    if current_version != latest_version:
        return latest_version
    return False
