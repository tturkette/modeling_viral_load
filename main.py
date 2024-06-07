import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Define the bi-exponential decay function
def bi_exponential_decay(t, A, alpha, B, beta):
    return A * np.exp(-alpha * t) + B * np.exp(-beta * t)

def load_data(url):
    try:
        data = pd.read_csv(url, header=None, names=["time_in_days", "viral_load"])
    except Exception as e:
        print(f"Error loading data: {e}")
        raise
    return data

def fit_model(time_data, viral_load_data):
    initial_guess = [1, 0.1, 0.5, 0.05]
    try:
        params, cov_matrix = curve_fit(bi_exponential_decay, time_data, viral_load_data, p0=initial_guess) # pylint: disable=W0632
    except RuntimeError as e:
        print(f"Error in curve fitting: {e}")
        raise
    except Exception as e:
        print(f"Unexpected error in curve fitting: {e}")
        raise
    return params, cov_matrix

def plot_results(time_data, viral_load_data, fitted_params):
    try:
        plt.figure(figsize=(10, 6))
        plt.scatter(time_data, viral_load_data, label='Data')
        plt.plot(time_data, bi_exponential_decay(time_data, *fitted_params), label='Fitted Curve', color='red')
        plt.legend()
        plt.xlabel('Time (t)')
        plt.ylabel('Viral Load (V)')
        plt.title('Bi-Exponential Decay Fit')
        plt.show()
    except Exception as e:
        print(f"Error in plotting: {e}")
        raise

if __name__ == "__main__":
    data_url = "https://raw.githubusercontent.com/ComputationalModeling/IPML-Data/master/01HIVseries/HIVseries.csv"
    data_frame = load_data(data_url)
    time_series = data_frame["time_in_days"].values
    viral_load_series = data_frame["viral_load"].values
    [fitted_a, fitted_alpha, fitted_b, fitted_beta], pcov = fit_model(time_series, viral_load_series)
    print(f"A: {fitted_a}, alpha: {fitted_alpha}, B: {fitted_b}, beta: {fitted_beta}")
    plot_results(time_series, viral_load_series, [fitted_a,fitted_alpha, fitted_b, fitted_beta])
