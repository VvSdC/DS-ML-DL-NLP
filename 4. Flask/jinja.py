from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)

@app.route('/')
def home_content():
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
    return render_template('score.html',result = 'Passed' if score >= 50 else 'Failed',score = score)

@app.route('/result/<int:score>')
def result(score):
    result = {
        'score' : score,
        'result': 'Passed' if score >= 50 else 'Failed'
    }
    return render_template('result.html',results = result)


@app.route('/result_if/<int:score>')
def result_if(score):
    return render_template('result_if.html',score = score)


@app.route('/submit_results',methods = ['GET','POST'])
def submit_results():
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