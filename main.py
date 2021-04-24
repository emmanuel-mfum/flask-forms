from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


# to tap into the data received from the form, we must use the request object from flask
# Then we can use this object to extract data (dictionary) got from the POST request ".method", ".path", ".form"
# If we want to access the values sent by the form we must use ".form" and braces in which we specify the name of the
# corresponding input in the HTML file as the name attribute identifies the input
@app.route('/login', methods=['POST'])  # we pass a keyword argument in the decorator signalling to accept POST requests
def login():
    user = request.form['username']
    password = request.form['password']
    return f"<h1> {user}, {password} </h1>"


if __name__ == "__main__":
    app.run(debug=True)
