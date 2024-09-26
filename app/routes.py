from flask import render_template, request, jsonify
from app import app
from app.models import predict_yield
from app.forms import CropYieldForm

@app.route('/', methods=['GET', 'POST'])
def index():
    form = CropYieldForm()
    if form.validate_on_submit():
        features = [
            form.nitrogen_pct.data,
            form.nitrogen_lbs.data,
            form.phosphorous_pct.data,
            form.phosphorous_lbs.data,
            form.potash_pct.data,
            form.potash_lbs.data,
            form.area_planted.data,
            form.harvested_area.data
        ]
        prediction = predict_yield(features)
        return render_template('index.html', form=form, prediction=prediction)
    return render_template('index.html', form=form)
