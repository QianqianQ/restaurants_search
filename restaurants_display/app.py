from flask import Flask, render_template
import json
app = Flask(__name__, template_folder='templates')


@app.route("/", methods=["GET"])
def index():
    with open("restaurants.json") as f:
        data = json.load(f)

    return render_template('index.html', restaurants=data['restaurants'])


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
