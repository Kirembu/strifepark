#!/usr/bin/env python

import os.path
import os
from urllib import urlretrieve
import imp

print "starting up, hang with me..."

urlretrieve('https://raw.github.com/facebook/fbconsole/master/src/fbconsole.py',
            '.fbconsole.py')
fbconsole = imp.load_source('fb', '.fbconsole.py')

page_id = raw_input("enter the id of the page:")

page = fbconsole.get('/'+page_id)

dirname = os.path.join(os.path.dirname(__file__), page.get('name'))
if not os.path.exists(dirname):
    os.mkdir(dirname)

albums = fbconsole.get('/'+page_id+'/albums', {'limit':500})
print "Found", len(albums), "albums"

for album in albums.get('data', []):
    album_dirname = os.path.join(dirname, album.get('name'))
    print "Downloading album", album_dirname
    if not os.path.exists(album_dirname):
        os.mkdir(album_dirname)

    photos = fbconsole.get('/'+album['id']+'/photos', {'limit':500})
    for ii, photo in enumerate(photos.get('data', [])):
        photo_name = '%s-%s.jpg' % (album.get('name'), ii)
        photo_path = os.path.join(album_dirname, photo_name)
        if not os.path.exists(photo_path):
            print "Downloading photo", photo_path
            image_url = photo['images'][0]['source']
            urlretrieve(image_url, photo_path)

print "All Done!"
