from flask import render_template, flash, redirect, url_for, request
from flask_login import login_required, current_user
from models import User, Feedback
from ext import db
from forms import FeedbackForm, RegisterForm, LoginForm
from flask_login import login_user, logout_user

def register_routes(app):
    @app.route('/')
    def index():
        return render_template('home.html')

    @app.route('/register', methods=['GET', 'POST'])
    def register():
        form = RegisterForm()
        if form.validate_on_submit():
            existing_user = User.query.filter_by(username=form.username.data).first()
            if existing_user:
                flash('Username already exists, please choose a different one.', 'danger')
                return redirect(url_for('register'))

            new_user = User(
                username=form.username.data,
                password=form.password.data,  # Remember to hash the password!
                mail=form.mail.data,
                phone_number=form.phone_number.data
            )

            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful!', 'success')
            return redirect(url_for('login'))

        return render_template('register.html', form=form)

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user and user.password == form.password.data:  # Check hashed password
                login_user(user)
                flash('Login successful!', 'success')
                return redirect(url_for('feedback'))
            else:
                flash('Invalid login credentials. Please try again.', 'danger')
        return render_template('login.html', form=form)

    @app.route('/logout')
    def logout():
        logout_user()
        flash('You have been logged out.', 'info')
        return redirect(url_for('login'))

    @app.route('/feedback', methods=['GET', 'POST'])
    @login_required
    def feedback():
        form = FeedbackForm()
        if form.validate_on_submit():
            new_feedback = Feedback(
                username=form.username.data,
                feedback=form.feedback.data
            )
            db.session.add(new_feedback)
            db.session.commit()
            flash('Feedback submitted successfully!', 'success')
            return redirect(url_for('feedback'))

        feedbacks = Feedback.query.all()
        return render_template('feedback.html', form=form, feedbacks=feedbacks)
    
    @app.route('/achievements')
    def achievements():
        achievements = [
            {
                "theme": "Programming Course",
                "about": "Successfully completed a programming course at the Georgian Innovation Technology Agency.",
                "icon": "&#128187;"  # Icon for a computer/technology
            },
            {
                "theme": "UNDP Spring School",
                "about": "Participated in a Spring School about the 'Rule of Law,' gaining insights into human rights and international law.",
                "icon": "&#128218;"  # Icon for a book
            },
            {
                "theme": "Volunteer Camps",
                "about": "Actively participated in camps focused on volunteering, teamwork, and respecting diverse opinions.",
                "icon": "&#9977;&#65039;"  # Icon for a tent/camping
            }
        ]
        return render_template('achievements.html', achievements=achievements)

    @app.route('/aboutme')
    def about():
        return render_template('aboutme.html')

    @app.route('/contact', methods=['GET', 'POST'])
    @login_required
    def contact():
        if request.method == 'POST':
            name = request.form['name']
            email = request.form['email']
            message = request.form['message']
            flash('Message sent successfully!', 'success')
            return redirect(url_for('contact'))

        return render_template('contact.html')
