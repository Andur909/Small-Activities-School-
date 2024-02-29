from flask import Flask

app = Flask(__name__)

@app.route("/")

def main():

    data = "Hello, This is the main Program <h1>Hello</h1>"
    data = data + "<h2>Heading 2</h2> <h6>Heading 6</h6> <br> <p>paragraph</p>"
    return data

if __name__ == "__main__":
    app.run()
