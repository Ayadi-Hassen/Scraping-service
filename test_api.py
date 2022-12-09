import requests
import json

def test_fb_posts():

    url = "http://0.0.0.0:80/fb/posts"

    # Additional headers.
    headers = {
    'Content-Type': 'application/json'
    }

    #body
    payload = json.dumps({
    "page_name": "nintendo",
    "pages": "2"
    })

    response = requests.request("POST", url, headers=headers, data=payload)

    # Validate response headers and body contents, e.g. status code.
    assert response.status_code == 200
