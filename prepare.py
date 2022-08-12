import pandas as pd
from datetime import timedelta, datetime
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import warnings
warnings.filterwarnings("ignore")

import acquire 


def prep_overall_sales():
    # retrive data
    df = acquire.get_overall_sales_data()
    # Reassign the sale_date column to be a datetime type
    df.sale_date = pd.to_datetime(df.sale_date)
    # Sort rows by the date and then set the index as that date
    df = df.set_index("sale_date").sort_index()
    # Add month and day columns
    df['month_name'] = df.index.month_name()
    df['day_name'] = df.index.day_name()
    # Create sales total column
    df['sales_total'] = df.sale_amount * df.item_price
    return df

# Plot distribution of variables in data
def sales_hist_enum():
    df = acquire.get_overall_sales_data()
    col = df[['sale_amount', 'item_price']]
    
    plt.figure(figsize=(16, 3))
    for i, col in enumerate(col):
        # i starts at 0, but plot nos should start at 1
        plot_number = i + 1
        # Create subplot.
        # plt.subplot(row X col, where?)
        plt.subplot(1,4,plot_number)
        # Title with column name.
        plt.title(col)
        # Display histogram for column.
        df[col].hist(bins=5, edgecolor='black')
        # Hide gridlines.
        plt.grid(False)
    return

def prep_power():
    # Retrive the data
    power = acquire.get_power()
    # Reassign the sale_date column to be a datetime type
    power.Date = pd.to_datetime(power.Date)
    # Sort rows by the date and then set the index as that date
    power = power.set_index("Date").sort_index()
    # Create moth and year columns
    power['month_name'] = power.index.month_name()
    power['year'] = power.index.year
    # Fill in null values
    power = power.fillna(0)
    return power

# Plot distribution of variables in data
def power_hist_enum():
    #power = acquire.get_power()
    col = power[['Wind', 'Solar', 'Wind+Solar']]
    
    plt.figure(figsize=(16, 3))
    for i, col in enumerate(col):
        # i starts at 0, but plot nos should start at 1
        plot_number = i + 1
        # Create subplot.
        # plt.subplot(row X col, where?)
        plt.subplot(1,4,plot_number)
        # Title with column name.
        plt.title(col)
        # Display histogram for column.
        power[col].hist(bins=5, edgecolor='black')
        # Hide gridlines.
        plt.grid(False)
    return
