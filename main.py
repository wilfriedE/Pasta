#/usr/bin/python3
import argparse
import requests
import json
import sys
#https://api.github.com/gists/5b48d8513dedba8effc8fe6ad09cc418

HOSTNAME = "api.github.com"
URL = ""
NAME = ""
DESCRIPTION = ""
PRIVATE = True

parser = argparse.ArgumentParser(description='Pastebin with Github Gists.')
parser.add_argument('-r', '--read',help='Read from specific gist', action="store_true")
parser.add_argument('-u','--url', help='Specific to read from or write to')
parser.add_argument('-n', '--name', default='untitled.txt', help='Name for gist')
parser.add_argument('-s', '--secret',help='Make the gist private', action="store_true")
parser.add_argument('-d', '--desc', default='', help='Description of gist')

def readgist():
    r = requests.get(URL).json()["files"][NAME]["raw_url"]
    data = requests.get(r).text
    print(data)

def paste():
    data_json = {
      "description": DESCRIPTION,
      "files": {
        NAME: {
          "content": ""
        }
      }
    }
    if not sys.stdin.isatty():
        data = sys.stdin.readlines()
        data_json["files"][NAME]["content"] = json.dumps(' '.join(data))
        sys.stdin = open('/dev/tty')
    else:
        data = input("Input: ")
        data_json["files"][NAME]["content"] = json.dumps(' '.join(data))
    data_json["files"][NAME]["public"] = False if PRIVATE else True
    data_json = json.dumps(data_json)
    r = requests.post(URL, data=data_json)
    print("Your pasta is available at: ", r.json()["html_url"])

def geturl():
    return "https://api.github.com/gists"

if __name__ == "__main__":
    args = parser.parse_args()
    NAME = args.name
    DESCRIPTION = args.desc
    PRIVATE = args.secret
    if args.url:
        URL = args.url
        if args.read:
            readgist()
    elif args.read:
        print("Please specify the url to the gist")
    else:
        URL = geturl()
        paste()
