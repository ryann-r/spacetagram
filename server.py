"""Server for SpaceGram app."""

from flask import Flask, render_template, request, session, redirect, jsonify
import crud


app = Flask(__name__)

app.secret_key = 'APP_SECRET_KEY'

app.jinja_env.undefined = StrictUndefined

@app.route('/')
def index():
    """View homepage."""

    return render_template('main.html')




if __name__ == '__main__':
    connect_to_db(app)
    app.run(debug=True, host='0.0.0.0')