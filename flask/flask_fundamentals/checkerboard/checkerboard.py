from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'
    
@app.route('/dojo')
def hello_dojo():
    return 'dojo!'

@app.route('/say/<name>')
def hello_dojo2(name):
    return 'Hi, ' + name    

@app.route('/repeat/35/hello')
def repeat_hello():
    return int("35")* "hello \n"
if __name__=="__main__":
    app.run(debug=True)
    
    

