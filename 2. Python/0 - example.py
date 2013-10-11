# An example of a web application
# This is how easy it is to start creating your web application!
# It's just 7 lines - isn't that amazing!
# It'll get alot easier soon don't you worry!

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()