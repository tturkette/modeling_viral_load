import pytest
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from main import bi_exponential_decay, load_data, fit_model

# Define the URL for data loading
data_url = "https://raw.githubusercontent.com/ComputationalModeling/IPML-Data/master/01HIVseries/HIVseries.csv"

def test_load_data():
    # Test that data is loaded correctly
    data_frame = load_data(data_url)
    assert not data_frame.empty, "Data should not be empty"
    assert "time_in_days" in data_frame.columns, "Data should contain 'time_in_days' column"
    assert "viral_load" in data_frame.columns, "Data should contain 'viral_load' column"

def test_curve_fitting():
    # Load the data for fitting
    data_frame = load_data(data_url)
    time_series = data_frame["time_in_days"].values
    viral_load_series = data_frame["viral_load"].values

    # Fit the model to the data
    fitted_params, pcov = fit_model(time_series, viral_load_series)

    # Check that the fitted parameters are reasonable
    assert len(fitted_params) == 4, "There should be 4 fitted parameters"
    assert np.all(np.isfinite(fitted_params)), "All fitted parameters should be finite"

if __name__ == "__main__":
    pytest.main()
