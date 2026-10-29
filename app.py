from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Cloud Computing Lab!"

@app.route('/about')
def about():
    return "This is my Flask web application."

if __name__ == '__main__':
    app.run(debug=True)