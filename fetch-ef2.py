#!/usr/bin/env python

import http.cookiejar
import requests
import urllib.parse
import os.path
import optparse

def fetch(fname, cookies):
    with open(fname) as f:
        contents = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    contents = [x.strip() for x in contents]

    cj = http.cookiejar.MozillaCookieJar(cookies)
    cj.load()
    for i in  range(len(contents)):
        content = contents[i]
        if content.startswith("http"):
            print(str(len(contents))+"/"+str(i)+" : "+content)
            r = requests.get(content, cookies=cj)
            if r.status_code != 200:
                exit -1
            path = urllib.parse.urlparse(content).path
            path = os.path.split(path);
            file = open( path[len(path) - 1], "wb")
            file.write(r.content)
            file.close()


def main():
    p = optparse.OptionParser()
    p.add_option('--ef2', '-f')
    p.add_option('--cookies', '-c', default="cookies.txt")
    options, arguments = p.parse_args()
    fetch(options.ef2, options.cookies)


if __name__ == '__main__':
    main()


