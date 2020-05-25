"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from Flask_Test import app

@app.route('/')
@app.route('/home')
def home():
    for i in range(6):
        print(i)
    """Renders the home page."""
    return render_template(
        'home.html',
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

