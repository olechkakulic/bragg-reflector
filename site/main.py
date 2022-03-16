from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app=Flask(__name__)
Bootstrap(app)

@app.route("/", methods=['GET'])
def get_main():
    return(render_template('main.html'))

@app.route("/second", methods=['GET'])
def get_second():
    return(render_template('second.html'))

@app.route("/other", methods=['GET'])
def get_other():
    return(render_template('other.html'))

if __name__=='__main__':
    app.run(debug=True)