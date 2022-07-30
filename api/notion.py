import requests
import urllib.request
import json

from vars.public_vars import NOTION_DATABASES_BASE_URL, NOTION_PAGES_BASE_URL, NOTION_SECRET_KEY, NOTION_TEST_DATABASE_ID


notion_query_url = NOTION_DATABASES_BASE_URL + NOTION_TEST_DATABASE_ID + "/query"

notion_headers = {
    "Accept": "application/json",
    'Notion-Version': '2022-02-22',
    'Authorization': 'Bearer ' + NOTION_SECRET_KEY,
    "Content-Type": "application/json"
}

def query_test_database(name: str):
    data = {
        "filter": {
            "property": "Name",
            "rich_text": {
                "equals": name
            }
        }
    }
    r = requests.post(notion_query_url, headers=notion_headers, json=data)
    return r.json()


def create_test_database(name: str, tel: str):
    payload = {
        "parent": {
            "database_id": NOTION_TEST_DATABASE_ID
        },
        "properties": {
            "Name": {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {
                            "content": name
                        }
                    }
                ]
            },
            "Tel": {
                "rich_text": [
                    {
                        "type": "text",
                        "text": {
                            "content": tel
                        }
                    }
                ]
            }
        }
    }

    res = urllib.request.Request(url=NOTION_PAGES_BASE_URL, data=bytes(json.dumps(payload), encoding="utf-8"),
                                 headers=notion_headers, method="POST")
    res = urllib.request.urlopen(res)
    if res.getcode() == 200:
        return 200
    else:
        return -1  # 未知错误
