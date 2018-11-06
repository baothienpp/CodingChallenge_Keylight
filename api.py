from flask import Flask
import datetime
import json
import requests

app = Flask(__name__)

link = 'https://api.github.com/search/repositories?q=created:%date%star&sort=stars&order=desc'


@app.route("/", methods=['GET'])
def get_total():
    stars, total = get_stars_watcher()
    return "Found: %d Repositories. Total of : %d stars " % (total, stars)


@app.route("/size/<int:max_size>", methods=['GET'])
def filter_max_size(max_size):
    stars, total = get_stars_watcher(size=max_size)
    return "Found: %d Repositories. Total of : %d stars " % (total, stars)


@app.route("/star/<int:star>", methods=['GET'])
def filter_star(star):
    stars, total = get_stars_watcher(star=star)
    return "Found: %d Repositories. Total of : %d stars " % (total, stars)


@app.route("/size/<int:max_size>/star/<int:star>", methods=['GET'])
def filter_multi_parameter(max_size, star):
    stars, total = get_stars_watcher(size=max_size, star=star)
    return "Found: %d Repositories. Total of : %d stars " % (total, stars)


@app.route("/star/<int:star>/size/<int:max_size>", methods=['GET'])
def filter_multi_parameter_switch(max_size, star):
    stars, total = get_stars_watcher(size=max_size, star=star)
    return "Found: %d Repositories. Total of : %d stars " % (total, stars)


def get_stars_watcher(size=None, star=None):
    link_tmp = link
    one_week_date = datetime.datetime.now() - datetime.timedelta(days=7)
    one_week_date = str(one_week_date.date())
    link_tmp = link_tmp.replace("%date", one_week_date)

    if star:
        link_tmp = link_tmp.replace("%star", "+stars:>=" + str(star))
    else:
        link_tmp = link_tmp.replace("%star", "+stars:>=100")

    data = requests.get(link_tmp).text
    output = json.loads(data)
    item_list = output.get('items')
    if size:
        item_list = item_list[:size]

    stars = 0
    total = len(item_list)
    for item in item_list:
        stars += item.get('stargazers_count')

    return stars, total

if __name__ == '__main__':
    app.run(debug=True)
