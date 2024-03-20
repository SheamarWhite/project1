"""
Flask Documentation:     https://flask.palletsprojects.com/
Jinja2 Documentation:    https://jinja.palletsprojects.com/
Werkzeug Documentation:  https://werkzeug.palletsprojects.com/
This file contains the routes for your application.
"""

from app import app, db
from flask import render_template, request, redirect, url_for, flash, send_from_directory

from app import Flask
from app.forms import PropertyForm
import random
from app.models import Property
from werkzeug.utils import secure_filename
import os
###
# Routing for your application.
###



@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name="Mary Jane")

@app.route('/create', methods=['GET', 'POST'])
def create():
    form = PropertyForm()

    if form.validate_on_submit():
        title = request.form['title']
        numOfBeds = form.numOfBeds.data
        numOfBaths = form.numOfBaths.data
        location = form.location.data
        price = form.price.data
        type = form.type.data
        description = form.description.data
        photo = form.photo.data
        filename = secure_filename(photo.filename)

        f = form.photo.data
        filename = secure_filename(f.filename)
        f.save(os.path.join('uploads', filename))

        House = Property(title=title, numOfBeds=numOfBeds, numOfBaths=numOfBaths, 
                         location=location, price=price, type=type, description=description, 
                         photo=filename)
        if House is not None:
            db.session.add(House)
            db.session.commit()

            flash('File Saved')
            return render_template('properties.html')


    return render_template('create.html', form=form)

@app.route('/properties', methods=['GET', 'POST'])
def properties():
    name = db.session.query(Property).all()
    root_dir = os.getcwd
    img = send_from_directory(os.path.join(root_dir, app.config['UPLOAD_FOLDER']), filename)
    for result in name:
        return render_template('properties.html', name=name, filename=img)
    return render_template('properties.html')

@app.route('/propertyid')
def propertyid():
    return render_template('propertyid.html')

###
# The functions below should be applicable to all Flask apps.
###

# Display Flask WTF errors as Flash messages
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also tell the browser not to cache the rendered page. If we wanted
    to we could change max-age to 600 seconds which would be 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404
