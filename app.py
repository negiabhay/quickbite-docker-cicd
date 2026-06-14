from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Quickbite!"

@app.route('/menu')
def menu():
    return "Today's Menu: Burger, Pizza, Pasta"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
