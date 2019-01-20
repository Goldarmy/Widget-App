from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DecimalField
from wtforms.validators import DataRequired, Length, NumberRange


class WidgetForm(FlaskForm):
    name = StringField('Widget Name:', validators=[DataRequired(message="Name is required!"),
                                                   Length(min=2, message='Name must have more than 2 characters!')])
    cost = DecimalField('Widget Cost:', validators=[DataRequired(message="Cost is required!"),
                                                    NumberRange(min=0,
                                                                message='Cost must be greater than 0!')])
    submit = SubmitField('Add')
