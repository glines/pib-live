#!/usr/bin/env python2

import sys

from lxml import html
import requests

import re

repo_name = sys.argv[1]

cgit_page = requests.get('http://cgit.freedesktop.org/')
tree = html.fromstring(cgit_page.text)

remotes = tree.xpath('//*[@id="cgit"]/div[1]/table/tr/td[1]/a/@href')

# Find all the remotes with the repo name we're looking for
regex = re.compile(r'/{}/$'.format(repo_name))
remotes = [r for r in remotes if regex.search(r)]

# Format the remotes into something we can feed into 'git remote add'
regex = re.compile(r'/~?(.*)/{}/$'.format(repo_name))
for r in remotes:
    match = regex.search(r)
    print '{} git://people.freedesktop.org{}'.format(
        match.group(1) if match else repo_name, r)
