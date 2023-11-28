from flask import Flask, render_template, request
from web_scrapping import get_json
from client_from_json import generate_python_class

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    python_class = None
    link = None

    if request.method == 'POST':
        link = request.form['link']
        swagger_content = get_json(link)
        python_class = generate_python_class(swagger_content)

    return render_template('index.html', python_class=python_class, link=link)


if __name__ == '__main__':
    app.run(debug=True)
