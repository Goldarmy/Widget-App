from flask import render_template, request, redirect, url_for, flash, abort
from new_app import app, db
from new_app.models import Widget
from new_app.forms import WidgetForm


@app.route('/', methods=['GET'])
def index():
    form = WidgetForm()
    widgets = Widget.query.order_by(Widget.id.asc()).all()
    return render_template('index.html', widgets=widgets, form=form)


@app.route('/add', methods=['POST'])
def add():
    form = WidgetForm()
    if request.method == "POST" and form.validate_on_submit():
        new_widget = Widget(name=form.name.data, cost=float(form.cost.data))
        db.session.add(new_widget)
        db.session.commit()
        flash('Widget has been added to the database!', 'success')
    else:
        widgets = Widget.query.order_by(Widget.id.asc()).all()
        return render_template('index.html', widgets=widgets, form=form)
    return redirect(url_for('index'))


@app.route('/delete/<int:widget_id>', methods=['POST'])
def delete(widget_id):
    widget = Widget.query.get_or_404(widget_id)
    db.session.delete(widget)
    db.session.commit()
    flash('Widget has been deleted!', 'success')
    return redirect(url_for('index'))


@app.route('/update/<int:widget_id>', methods=['POST'])
def update(widget_id):
    widget = Widget.query.get_or_404(widget_id)
    widget.name = request.form['widget_name']
    widget.cost = float(request.form['widget_cost'])
    db.session.merge(widget)
    db.session.commit()
    flash('Widget has been updated!'.format(widget_id), 'success')
    return redirect(url_for('index'))


@app.errorhandler(403)
def forbidden(e):
    return render_template('403.html'), 403


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    # test by running abort(404)
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500
