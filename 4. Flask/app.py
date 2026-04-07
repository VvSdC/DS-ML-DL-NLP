from flask import Flask, render_template, request

'''
This creates an instance of the Flask class,
which will be the WSGI (Web Server Gateway Interface) application
'''
# WSGI application
app = Flask(__name__)


@app.route("/")
def welcome():
    """Route handler for the root URL.

    Flask functionality: the `@app.route` decorator registers this
    function as the view for the `/` URL. Flask will call this
    function when an HTTP request targets `/` and expects a response
    (a string, Response object, or template rendering).
    """
    return "Welcome to introduction to flask"


'''
The render_templates will redirect to the provided html file name inside the templates folder.
So, it is important to place the required html files in templates folder before using render_templates
'''
@app.route("/index")
def welcome_index():
    """Render a template from the `templates/` folder.

    Flask functionality: `render_template` looks up `index.html` inside
    the `templates` directory, renders it with Jinja2, and returns a
    Response object with the rendered HTML and proper headers.
    """
    return render_template('index.html')


@app.route("/about")
def about():
    """Simple template view.

    Flask functionality: same as above — maps `/about` to this view
    and returns the rendered template as the HTTP response.
    """
    return render_template('about.html')

@app.route("/details",methods = ['GET','POST'])
def get_details():
    """Handle form submission using Flask's `request` object.

    Flask functionality: `methods=['GET','POST']` tells Flask to allow
    both GET and POST requests for this route. The `request` proxy
    provides access to incoming request data (querystring, form data,
    files, headers). Returning a string or `render_template` becomes the
    HTTP response sent back to the client.
    """
    if request.method == 'POST':
        name = request.form.get('name', '')
        return f'Hello!! {name}'
    return render_template("form.html")
    

'''
Keeping debug as True will refresh server when there are any changes made.
This is useful during development
'''
if __name__ == "__main__":
    # `debug=True` starts the built-in development server with the
    # reloader and interactive debugger enabled; do NOT use in
    # production. `app.run` is a convenience for development; in
    # production a WSGI server (gunicorn, uWSGI, etc.) should be used.
    app.run(debug = True)