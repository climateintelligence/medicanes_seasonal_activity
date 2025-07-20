import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


def plot_timeseries_results(y_true, y_pred, model_name, start='1980-01', end='2020-01'):

    # Generate the datetime index from January 1980 to December 2019
    date_range = pd.date_range(start=start, end=end, freq="M")

    plt.figure(figsize=(15, 5))
    plt.plot(date_range, y_true.flatten(), label='Observed ACE', linewidth=2, color='#0f52ba')
    plt.plot(date_range, y_pred.flatten(), label=f'{model_name}-predicted ACE', linewidth=2.1, linestyle='--', color='#ED820E')

    # Formatting x-axis
    plt.xlabel('Year', fontsize=22)
    plt.ylabel('ACE', fontsize=22)
    plt.legend(fontsize=20)

    # Set major x-axis locator to yearly intervals
    plt.gca().xaxis.set_major_locator(mdates.YearLocator(5))  # Show a label every 5 years
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y'))  # Display only the year

    plt.xticks(rotation=45, fontsize=18)  # Rotate labels for better readability
    plt.yticks(fontsize=18)
    plt.show()