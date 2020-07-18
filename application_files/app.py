from flask import (
    Flask,
    render_template,
    jsonify)

from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import create_engine



app = Flask(__name__)


@app.route("/")
def home():
    """Render Home Page."""
    return render_template("index.html")



if __name__ == '__main__':
    app.run(debug=True)

