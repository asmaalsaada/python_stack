from flask import Flask, render_template
app=Flask(__name__)
# @app.route('/play')
# def play():
#     return render_template('index.html')
# if __name__=="__main__":   # Ensure this file is being run directly and not from a different module
#     app.run(debug=True)    # Run the app in debug mode.

# @app.route('/play/<x>')
# def play(x):
#     return render_template('index.html', number=int(x))
@app.route('/play/<x>/<y>')
def play(x, y):
    return render_template('index.html', number=int(x), color=y)
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module
    app.run(debug=True)    # Run the app in debug mode.