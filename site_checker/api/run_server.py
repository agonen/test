import flask
from flask import jsonify, request

from site_checker.api.site_checker import site_checker

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/api/v1/check_url/', methods=['GET'])
def url_checker():
    url = request.args.get('url')
    if url is None:
        return "Error: No Url field provided. Please specify an url."

    results = site_checker(url)
    return jsonify(results)


def run_server():
    app.run()
