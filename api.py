from flask import Flask
import json
import requests
#
# app = Flask(__name__)
#
#
# @app.route("/")
# def hello():
#     return "Hello World!"
#
# https://api.github.com/search/repositories?q=tetris+language:assembly&sort=stars&order=desc

# Here we print out the retrieved page's HTML to the console
# once we've got this we can start performing some analysis of
# the webpage and do some cooler things.

link = 'https://api.github.com/search/repositories?q=created:2018-11-01+stars:>=100&sort=stars&order=desc'
data = requests.get(link).text
output = json.loads(data)
test = output.get('items')
for key, value in output.get('items'):
    print(output)
