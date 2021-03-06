# Copyright 2016 Google Inc.
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

import webapp2
import os
import jinja2

#remember, you can get this by searching for jinja2 google app engine
the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=[ 'jinja2.ext.autoescape'],
    autoescape=True)

class CssiPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/html'
        self.respone.write('<h1>GoodBye, World!</h1>')


class MainPage(webapp2.RequestHandler):
    def get(self):
        welcome_template = the_jinja_env.get_template('templates/welcome.html')

        template_disc = {"country": "usa",
                        "region_name": "north east",
                        "region_num": 121,
                        "url":"https://coworker.imgix.net/pictures/C45/edit/nagoya-resize.jpg", 
                        "city": ["new york" ,"boston", "philadelphia"],
                    "message": "welcome to: "
                        }

        self.response.write(welcome_template.render(template_disc))

class ShowMemeHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write("Hello from ShowMemeHandler")
    def post(self):
        results_template = the_jinja_env.get_template('templates/results.html')
        firstname = self.request.get('alsofirstname')
        lastname = self.request.get('last name')

        webform_dict = {"fn": firstname, "ln": lastname}
        self.response.write(results_template.render(webform_dict))
        # self.response.write(firstname)

app = webapp2.WSGIApplication([
        ('/', MainPage),
        ('/showresults', ShowMemeHandler),
        ('cssi', CssiPage)],
        debug=True)
