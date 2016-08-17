from flask import render_template
from app import app, db, models

@app.route('/')
@app.route('/index')
def index():
	return 'Index'