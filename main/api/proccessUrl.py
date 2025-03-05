import requests as r


def get_request(url, authorization):
    return r.get(url, headers={"Authorization": f"Bearer {authorization}"})
