from flask import Flask, request
import datetime
import json
import requests

app = Flask(__name__)

link = 'https://api.github.com/search/repositories?q=created:%date%star&sort=stars&order=desc'


@app.route("/", methods=['GET'])
def get_total():
    stars = request.args.get('stars')
    max_size = request.args.get('max_size')
    stars, total = get_stars_watcher(star=stars, size=max_size)
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
        item_list = item_list[:int(size)]

    stars = 0
    total = len(item_list)
    for item in item_list:
        stars += item.get('stargazers_count')

    return stars, total


if __name__ == '__main__':
    app.run(debug=True)
