from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired, NumberRange

class CropYieldForm(FlaskForm):
    nitrogen_pct = FloatField('Nitrogen (%)', validators=[DataRequired(), NumberRange(min=0, max=100)])
    nitrogen_lbs = FloatField('Nitrogen (Pounds/Acre)', validators=[DataRequired()])
    phosphorous_pct = FloatField('Phosphorous (%)', validators=[DataRequired(), NumberRange(min=0, max=100)])
    phosphorous_lbs = FloatField('Phosphorous (Pounds/Acre)', validators=[DataRequired()])
    potash_pct = FloatField('Potash (%)', validators=[DataRequired(), NumberRange(min=0, max=100)])
    potash_lbs = FloatField('Potash (Pounds/Acre)', validators=[DataRequired()])
    area_planted = FloatField('Area Planted (hectares)', validators=[DataRequired()])
    harvested_area = FloatField('Harvested Area (hectares)', validators=[DataRequired()])
    submit = SubmitField('Predict')
