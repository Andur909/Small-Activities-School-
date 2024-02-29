from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    #Set the lines
    line_1 = "<h4>Welcome to Python Programming Using Flask</h4>"
    line_2 = "I am an advanced programmer in developing web sites"
    line_3 = "Make sure to stay tuned for some more fun using Flask"

    #Combine Lines with breaks
    return line_1 + "<br>" + line_2 + "<br>" + line_3

if __name__ == "__main__":
    app.run()
