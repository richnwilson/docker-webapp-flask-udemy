import os
from flask import Flask, render_template
app = Flask(__name__)

color = os.environ.get('APP_COLOR')

@app.route("/")
def main():
    return render_template('about.html', label="Welcome!", color=color)

@app.route('/how are you')
def hello():
    return render_template('about.html', label='I am good, how about you?', color=color)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
