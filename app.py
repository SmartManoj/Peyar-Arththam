from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<name>', methods=['GET', 'POST'])
def search(name=None):
    names_data = {
        'யுகன்' : {
            'variant': 'யுகநந்தனா',
            'meaning': 'இவரால் பிரபஞ்சம் மகிழ்ச்சி அடையும்',
            'type': 'M'
        }
    }
    return render_template('search.html', name=name, name_data=names_data.get(name))


if __name__ == '__main__':
    app.run(debug=True)
