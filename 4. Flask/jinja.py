from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)

@app.route('/')
def home_content():
    """Root view showing a simple string response.

    Flask functionality: maps `/` to this view using `@app.route`.
    Returning a string will be sent as an HTTP response with a
    `200 OK` status and `text/html` content type by default.
    """
    return "Welcome to home page"

# Jinja2 Template engine
'''
{{ }} -> To print a variable in HTML
{%...%} -> For conditions and looping in HTML
{#..#} -> For comments in HTML
'''
# Variable rule
@app.route('/success/<int:score>')
def success(score):
    """Demonstrates a variable URL rule and template rendering.

    Flask functionality: the `<int:score>` part in the route is a
    variable rule — Flask extracts the value from the URL and passes
    it as the `score` argument. `render_template` renders the Jinja2
    template and returns a proper Response object.
    """
    return render_template('score.html',result = 'Passed' if score >= 50 else 'Failed',score = score)

@app.route('/result/<int:score>')
def result(score):
    """Build a context dictionary and render it into a template.

    Flask functionality: view functions can build context data
    (plain Python objects) and pass them to `render_template`. Jinja2
    templates access these variables when rendering the HTML.
    """
    result = {
        'score' : score,
        'result': 'Passed' if score >= 50 else 'Failed'
    }
    return render_template('result.html',results = result)


@app.route('/result_if/<int:score>')
def result_if(score):
    """Render a template that demonstrates Jinja conditional logic.

    Flask functionality: `render_template` will hand off rendering to
    Jinja2; template syntax like `{% if %}` and `{% for %}` are handled
    inside the template, keeping view logic separated from presentation.
    """
    return render_template('result_if.html',score = score)


@app.route('/submit_results',methods = ['GET','POST'])
def submit_results():
    """Handle form POST and redirect using Flask helpers.

    Flask functionality: when receiving POST data, `request.form`
    provides access to submitted form fields. `redirect` produces a
    302 redirect response and `url_for` builds URLs for view
    functions based on their endpoint name (avoids hardcoding paths).
    """
    if request.method == "POST":
        total_score = 0
        math = int(request.form.get('Math'))
        physics = int(request.form.get('Physics'))
        chemistry = int(request.form.get('Chemistry'))
        total_score = math + physics + chemistry
        print(f"Total score is : {total_score}")
        return redirect(url_for("result_if",score = total_score))
    if request.method == "GET":
        return render_template("results_form.html")


if __name__ == "__main__":
    app.run(debug = True)