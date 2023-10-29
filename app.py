from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<name>', methods=['GET', 'POST'])
def search(name=None):
    names_data = {
        'யுகன்' : {
            'root': 'கலியுகவரதன்',
            'meaning': 'பிரபஞ்சத்தின் பாதுகாவலர்',
            'type': 'M'
        }
    }
    return render_template('search.html', name=name, name_data=names_data.get(name))


if __name__ == '__main__':
    app.run(debug=True)
