
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, RadioField, BooleanField
from wtforms.validators import DataRequired

class FinderForm(FlaskForm):
  finder =  StringField("Finder", validators=[DataRequired()])
  save = BooleanField("Save", validators=[DataRequired()])
  submit = SubmitField("Add description for Finder")
  '''
  recipe_type = RadioField("Type", choices=recipe_categories)
  description = StringField("Description")
  ingredients = TextAreaField("Ingredients")
  instructions = TextAreaField("Instructions")
  '''

class VisualiserForm(FlaskForm):
  comment =  StringField("Comment", validators=[DataRequired()])
  submit = SubmitField("Add Comment")
