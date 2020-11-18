from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods = ['GET'] )
def home():
    return render_template("terms.html", message = "hello whats up, welcome to my page")

if __name__ == '__main__':
    app.run(port=9000, debug=False)
    