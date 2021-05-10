from flask import Flask, render_template    # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route("/")          # The "@" decorator associates this route with the function immediately following
# def hello_world():
# def index():
#     return render_template("index.html", phrase="hello" , times=5)
    # return render_template("index.html") 
    # return 'Hello World!'  # Return the string 'Hello World!' as a response
# if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
#     app.run(debug=True)    # Run the app in debug mode.

# import statements, maybe some other routes
    
# Import Flask to allow us to create our app
# app = Flask(__name__)     
@app.route("/") 
def hello(): 
    print("in the hello function")
    return render_template("name.html")
    # return "Hello!"
@app.route("/<name>, <times>") 
def hello_person(name,times): 
    print ("*" * 80)
    print(name)
    print("in the hello_person function")
    return render_template("name.html", some_name=name, num_times=int(times))
    # return f"Hello ,{name}!"
if __name__=="__main__":  
    app.run(debug=True) 
# app.run(debug=True) should be the very last statement! 

