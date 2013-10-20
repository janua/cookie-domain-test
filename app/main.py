from flask import Flask
from flask import render_template, make_response, request, redirect
app = Flask(__name__)

USER_AGENTS = dict()

DOMAIN_ONE = 'www.newdomain.com'
DOMAIN_TWO = 'www.olddomain.com'

@app.route("/")
def index():
    user_agents = "User Agents:<br/>{0}".format("<br/>".join([str(x) for x in USER_AGENTS.items()]))
    cookies = "Cookies: {0}".format(str(request.cookies))
    query_params = "Query Params: {0}".format(str(request.args.items()))
    response_string = "{0}<br/>{1}<br/>{2}".format(user_agents, cookies, query_params)

    user_agent = request.headers.get('User-Agent')
    host = request.headers.get('Host')

    response = make_response(response_string)
    return response


if __name__ == "__main__":
    app.debug = True
    app.run(port=80)