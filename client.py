import json
import urllib2
import sys
import requests


def get():
    url = 'http://127.0.0.1:5000/chat/'

    response = urllib2.urlopen(url)
    data = json.load(response)

    for item in data["_items"]:
        print(item["name"])
        print(item["message"])
        print


def post(name, message):
    url = 'http://127.0.0.1:5000/chat/'

    data = {
        'name': name,
        'message': message
    }

    req = urllib2.Request(url)
    req.add_header('Content-Type', 'application/json')

    urllib2.urlopen(req, json.dumps(data))


def delete():
    url = "http://127.0.0.1:5000/chat/"
    requests.delete(url)


if sys.argv[1] == "get":
    get()

if sys.argv[1] == "post":
    post(sys.argv[2], sys.argv[3])

if sys.argv[1] == "delete":
    delete()