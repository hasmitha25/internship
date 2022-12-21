# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask
 
# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)
# app = Flask("My First App")
 
# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
@app.route('/')
# ‘/’ URL is bound with hello_world() function.
def hello_world():
    return 'Hello World'
 
# Following route returns a simple html script that browser can easily parse and display
@app.route("/v1/pages/1")
def simple_html():
    return '''<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Flask Tutorial</title>
  </head>
  <body>
    <h1> My First Try Using Flask </h1>
    <p> I returned html script </p>
  </body>
</html>''' 
# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application
    # on the local development server.
    print("open http://localhost:8888/v1/pages/1")
    app.run(port=8888)
