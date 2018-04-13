from flask import Flask
import os, os.path


app = Flask(__name__)
@app.route('/')
@app.route('/index')

def index():
    files_in_dump = len([name for name in os.listdir('/media/mfrl/dump')])
    return "Hello, world!\nThere are %d files in dump." % files_in_dump

app.run(debug=True)

# feedly sandbox user id:  40855218-bd19-4735-8278-97c6997e8a9e
# feedly cloud user id:   6f8818f5-7a20-469d-8120-1df762d321fc
