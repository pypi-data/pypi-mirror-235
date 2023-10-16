from typing import Union

import requests

from .auth import get_token


def get_group(
    group_id: str = None,
    select: Union[list, str] = None,
    filter: str = None,
    search: str = None,
    orderby: Union[list, str] = None,
    top: int = None,
    all: bool = False,
) -> Union[list[dict], dict]:
    """ """

    MAX_PAGE_SIZE = 999

    def ensure_list(value):
        return [value] if isinstance(value, str) else value

    if group_id and (filter or search):
        raise ValueError(
            "Parameters group_id and filter|search are mutually exclusive."
        )

    headers = {
        "Authorization": f"Bearer {get_token()}",
        "ConsistencyLevel": "eventual" if filter or search or orderby else None,
    }

    params = {
        "$select": ",".join(ensure_list(select)) if select else None,
        "$filter": filter,
        "$search": f'"{search}"' if search else None,
        "$orderby": ",".join(ensure_list(orderby)) if orderby else None,
        "$top": top if top is not None else (MAX_PAGE_SIZE if all else None),
        "$count": "true" if filter or search or orderby else None,
    }

    data = []
    url = "https://graph.microsoft.com/v1.0/groups"

    if group_id:
        url += f"/{group_id}"

    while True:
        response = requests.get(url, headers=headers, params=params)

        if response.status_code != 200:
            error_message = response.json().get("error", {}).get("message")
            raise ConnectionError(
                f"Request failed ({response.status_code} {response.reason}):\n"
                f"{error_message}"
            )

        data.extend(response.json().get("value", [response.json()]))
        next_link = response.json().get("@odata.nextLink")

        if next_link and (all and top is None):
            params["$skiptoken"] = next_link.split("$skiptoken=")[1]
        else:
            break

    return data[0] if group_id else data


def list_group_members(
    group_id: str,
    select: Union[list, str] = None,
    filter: str = None,
    search: str = None,
    orderby: Union[list, str] = None,
    top: int = None,
    all: bool = False,
) -> Union[list[dict], dict]:
    """ """

    MAX_PAGE_SIZE = 999

    def ensure_list(value):
        return [value] if isinstance(value, str) else value

    headers = {
        "Authorization": f"Bearer {get_token()}",
        "ConsistencyLevel": "eventual" if filter or search or orderby else None,
    }

    params = {
        "$select": ",".join(ensure_list(select)) if select else None,
        "$filter": filter,
        "$search": f'"{search}"' if search else None,
        "$orderby": ",".join(ensure_list(orderby)) if orderby else None,
        "$top": top if top is not None else (MAX_PAGE_SIZE if all else None),
        "$count": "true" if filter or search or orderby else None,
    }

    data = []
    url = f"https://graph.microsoft.com/v1.0/groups/{group_id}/members"

    while True:
        response = requests.get(url, headers=headers, params=params)

        if response.status_code != 200:
            error_message = response.json().get("error", {}).get("message")
            raise ConnectionError(
                f"Request failed ({response.status_code} {response.reason}):\n"
                f"{error_message}"
            )

        data.extend(response.json().get("value"))
        next_link = response.json().get("@odata.nextLink")

        if next_link and (all and top is None):
            params["$skiptoken"] = next_link.split("$skiptoken=")[1]
        else:
            break

    return data


def add_group_member(group_id: str, member_id: str) -> bool:
    """ """

    response = requests.post(
        url=f"https://graph.microsoft.com/v1.0/groups/{group_id}/members/$ref",
        headers={"Authorization": f"Bearer {get_token()}"},
        json={
            "@odata.id": f"https://graph.microsoft.com/v1.0/directoryObjects/{member_id}"
        },
    )

    if response.status_code != 204:
        error_message = response.json().get("error", {}).get("message")
        raise ConnectionError(
            f"Request failed ({response.status_code} {response.reason}):\n"
            f"{error_message}"
        )

    return True


def remove_group_member(group_id: str, member_id: str) -> bool:
    """ """

    response = requests.delete(
        url=f"https://graph.microsoft.com/v1.0/groups/{group_id}/members/{member_id}/$ref",
        headers={"Authorization": f"Bearer {get_token()}"},
    )

    if response.status_code != 204:
        error_message = response.json().get("error", {}).get("message")
        raise ConnectionError(
            f"Request failed ({response.status_code} {response.reason}):\n"
            f"{error_message}"
        )

    return True
