from flask import render_template, redirect, request, url_for
from flask_login import login_user, logout_user, login_required
from . import auth
from .forms import LoginForm
from ..models import User

@auth.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		print(form.email.data)
		print(form.password.data)
		user = User.query.filter_by(email=form.email.data).first()
		print(user)
		if user is not None and user.verify_password(form.password.data):
			login_user(user, form.remember_me.data)
			return redirect(request.args.get('next') or url_for('main.index'))

		print('Failed to log in')

	return render_template('auth/login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
	logout_user()
	return redirect(url_for('main.index'))