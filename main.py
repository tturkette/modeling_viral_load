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
        popt, pcov = curve_fit(bi_exponential_decay, time_data, viral_load_data, p0=initial_guess)
    except RuntimeError as e:
        print(f"Error in curve fitting: {e}")
        raise
    except Exception as e:
        print(f"Unexpected error in curve fitting: {e}")
        raise
    return popt

def plot_results(time_data, viral_load_data, popt):
    try:
        plt.figure(figsize=(10, 6))
        plt.scatter(time_data, viral_load_data, label='Data')
        plt.plot(time_data, bi_exponential_decay(time_data, *popt), label='Fitted Curve', color='red')
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
    data = load_data(data_url)
    time_data = data["time_in_days"].values
    viral_load_data = data["viral_load"].values
    popt = fit_model(time_data, viral_load_data)
    print(f"A: {popt[0]}, alpha: {popt[1]}, B: {popt[2]}, beta: {popt[3]}")
    plot_results(time_data, viral_load_data, popt)
