from flask import Flask

app = Flask(__name__)
app.config.from_object('testapp.config')

db = SQLAlchemy(app)

import testapp.views

