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

parser = argparse.ArgumentParser(description='Pastebin with Github Gists.')
parser.add_argument('-r', '--read',help='Read from specific gist', action="store_true")
parser.add_argument('-u','--url', help='Specific to read from or write to')
parser.add_argument('-n', '--name', default='untitled.txt', help='Name for gist')
parser.add_argument('-d', '--desc', default='', help='Description of gist')

def readgist():
    r = requests.get(URL).json()["files"][NAME]["raw_url"]
    data = requests.get(r).text
    print(data)

def paste():
    print("Pasting to url: ", URL)

def geturl():
    print("creating new url")

if __name__ == "__main__":
    args = parser.parse_args()
    NAME = args.name
    DESCRIPTION = args.desc
    if args.url:
        URL = args.url
        if args.read:
            readgist()
    elif args.read:
        print("Please specify the url to the gist")
    else:
        URL = geturl()
        paste()
