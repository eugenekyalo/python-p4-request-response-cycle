# server/app.py

import os
from flask import Flask, request, current_app, g, make_response, redirect, abort

app = Flask(__name__)

@app.before_request
def app_path():
    """Store the application's path in the g object for the duration of the request."""
    g.path = os.path.abspath(os.getcwd())

@app.route('/')
def index():
    """Return the index page with host, app name, and app path."""
    host = request.headers.get('Host')
    appname = current_app.name
    response_body = f'''
        <h1>The host for this page is {host}</h1>
        <h2>The name of this application is {appname}</h2>
        <h3>The path of this application on the user's device is {g.path}</h3>
    '''
    status_code = 200
    headers = {}
    
    return make_response(response_body, status_code, headers)

@app.route('/reginald-kenneth-dwight')
def redirect_example():
    """Redirect example that sends the user to a different URL."""
    return redirect('https://names.com/elton-john')

@app.route('/<stage_name>')
def get_name(stage_name):
    """Return a response based on the stage name provided in the URL."""
    # This is a placeholder. You should replace the following line with your actual database query logic.
    match = False  # Simulate the logic for checking if the stage name exists
    
    if not match:
        abort(404)  # Abort with a 404 error if the stage name does not exist
    
    return make_response(f'<h1>{stage_name} is an existing stage name!</h1>')

if __name__ == '__main__':
    app.run(port=5555, debug=True)
