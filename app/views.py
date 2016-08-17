from flask import render_template
from flask_login import login_required
from app import app, db, models

@app.route('/')
@app.route('/index')
@login_required
def index():
	return 'Index'