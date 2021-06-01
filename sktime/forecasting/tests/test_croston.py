# -*- coding: utf-8 -*-
from sktime.forecasting.croston import Croston
from sktime.datasets import load_PBS_dataset
import pytest
import numpy as np

# test the Croston's Method against the R package


@pytest.mark.parametrize(
    "fh, r_forecast",
    [
        (10, 0.8688921),
    ],
)
def test_Croston_against_r_implementation(fh, r_forecast):
    """
    Testing forecasted values estimated by the R package of the Croston's method
    https://github.com/robjhyndman/forecast/blob/master/R/guerrero.R
    against the Croston method in sktime.
    R code to generate the hardcoded value for fh=10:
    ('PBS_dataset.csv' contains the data from 'load_PBS_dataset()'):

        PBS_file <- read.csv(file = '/content/PBS_dataset.csv')[,c('Scripts')]
        y <- ts(PBS_file)
        demand=ts(y)
        forecast <- croston(y,h = 10)
    Output:
        0.8688921
    """
    y = load_PBS_dataset()
    forecaster = Croston(smoothing=0.1)
    forecaster.fit(y)
    y_pred = forecaster.predict(fh=fh)
    np.testing.assert_almost_equal(y_pred.item(), r_forecast, decimal=4)
