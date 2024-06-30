
"""
Flask web application for Kondor Plus.
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """
    Flask web application for Kondor Plus.
    """
    return render_template('index.html')

@app.route('/projects')
def projects():
    """
    Projects
    """
    return render_template('projects.html')

@app.route('/about')
def about():
    """
    about
    """
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
