from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!, testando novo fluxo!"

if __name__ == "__main__":
    app.run()