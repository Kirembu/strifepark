#!/usr/bin/env python
#
# Copyright 2012 Kirembu.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import os
from google.appengine.ext.webapp import util

from google.appengine.ext import webapp
##from google.appengine.ext.webapp import util

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
from django.core.handlers import wsgi

def main():
    app = wsgi.WSGIHandler()
    util.run_wsgi_app(app)
    

##class MainHandler(webapp.RequestHandler):
##    def get(self):
##        self.response.out.write('Hello world!')
##
##
##def main():
##    application = webapp.WSGIApplication([('/', MainHandler)],
##                                         debug=True)
##    util.run_wsgi_app(application)
##

if __name__ == '__main__':
    main()
