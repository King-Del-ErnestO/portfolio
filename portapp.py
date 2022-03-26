from flask import Flask, redirect, url_for, request, render_template


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('del-port.html')


if __name__ == '__main__':
    app.run(debug = True)