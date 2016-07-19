#/usr/bin/python3
import argparse
import requests
import json
import sys

HOSTNAME = "api.github.com"
URL = ""
NAME = ""
DESCRIPTION = ""
PRIVATE = True

parser = argparse.ArgumentParser(description='Pastebin with Github Gists.')
parser.add_argument('-r', '--read',help='Read from specific gist', action="store_true")
parser.add_argument('-u','--url', help='Specific to read from')  #updating not supported at the moment
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
    return "https://" + HOSTNAME +"/gists"

def getapiurl(raw_url):
    gist_id = raw_url.rpartition('/')[-1]
    return "https://" + HOSTNAME +"/gists/" + gist_id

if __name__ == "__main__":
    args = parser.parse_args()
    NAME = args.name
    DESCRIPTION = args.desc
    PRIVATE = args.secret
    if args.url:
        URL = getapiurl(args.url)
        print(URL)
        #if args.read:
        #reads by default for now
        readgist()
    elif args.read:
        print("Please specify the url to the gist")
    else:
        URL = geturl()
        paste()
