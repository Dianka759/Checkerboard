from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def checkerboard():
    return render_template("index.html", times = 8, width = 8, color1 = 'black', color2 = 'blue')

@app.route('/<int:number>')
def checkerboard2(number):
    return render_template("index.html", times = number, width=8, color1 = 'black', color2 = 'blue')

@app.route('/<int:number>/<int:number2>')
def customCheckerboard(number, number2):
    return render_template("index.html", times = number, width = number2, color1 = 'black', color2 = 'blue')

@app.route('/<int:number>/<int:number2>/<string:color1>/<string:color2>')
def colorChange(number, number2, color1, color2):
    return render_template("index.html", times = number, width = number2, color1 = color1, color2 = color2)


# Left it here just because. 
@app.errorhandler(404) # only works for error 404, page not found 404 status explicitly
def page_not_found(e):
    return ('Sorry! No response. Double check your url and try again :)'), 404

if __name__=="__main__":
    app.run(debug=True)