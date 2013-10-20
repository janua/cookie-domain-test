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

@app.route("/redirect")
def redirect_route():
    host = request.headers.get('Host')

    if host == DOMAIN_ONE:
        if request.cookies.get('AlreadySeen') == 'True':
            root_redirect = make_response(redirect('/'))
            root_redirect.set_cookie('AlreadySeen', 'True')
            return root_redirect
        
        else:
            other_domain_redirect = make_response(redirect('http://' + DOMAIN_TWO + '/redirect'))
            other_domain_redirect.set_cookie('AlreadySeen', 'True')
            return other_domain_redirect

    elif host == DOMAIN_TWO:
        bounce_back_redirect = make_response(redirect('http://' + DOMAIN_ONE + '/redirect'))
        bounce_back_redirect.set_cookie('Carry', 'True')
        return bounce_back_redirect

    return make_response('Hosts setup incorrectly')


if __name__ == "__main__":
    app.debug = True
    app.run(port=80)