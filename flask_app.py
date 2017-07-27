from flask import Flask, render_template, request


# create the application object
app = Flask(__name__)
@app.route('/')
def welcome():
    return render_template('main.html')  # render a template


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run()