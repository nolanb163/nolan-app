"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from Flask_Test import app

@app.route('/')
@app.route('/home')
@app.route('/boneprison')
def home():
    return render_template(
        'bone-prison.html',
    )

@app.route('/index')
def index():
    return render_template(
        'index.html',
    )