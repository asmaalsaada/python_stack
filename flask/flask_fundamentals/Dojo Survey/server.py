from flask import Flask, render_template,request, redirect , session
app = Flask(__name__)
app.secret_key = " This's highly calssified"
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/results', methods=['POST'])
def create_user():
    print(request.form)
    session['Your_Name'] = request.form['Your_Name']
    session['Dojo_Loc'] = request.form['Dojo_Loc']
    session['Fav_Lan'] = request.form['Fav_Lan']
    session['comment']= request.form['text_box']
    return redirect('/show')

@app.route('/show')
def show_form():
    print(request.form)
    return render_template("show.html")

if __name__ == "__main__":
    app.run(debug=True)