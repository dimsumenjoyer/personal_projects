import pandas as pd
import matplotlib.pyplot as plt

def sleep_dataframe():
    columns_needed = ["day", "average_heart_rate", "lowest_heart_rate", "average_hrv", "total_sleep_duration", "time_in_bed"]
    sleep_data_file = pd.read_csv("oura_sleep_2023-10-18T00-30-30.csv", usecols = columns_needed)
    return sleep_data_file

def sleep_data_dates(sleep_data_file):
    unordered_dates = set(sleep_data_file["day"].unique())
    dates = sorted([pd.to_datetime(date) for date in unordered_dates])
    return dates

def find_average_heart_rate(sleep_data_file):
    sleep_data_file["day"] = pd.to_datetime(sleep_data_file["day"])
    average_heart_rate = sleep_data_file.groupby("day")["average_heart_rate"].mean()
    return average_heart_rate

def find_lowest_heart_rate(sleep_data_file):
    lowest_heart_rate = sleep_data_file.groupby("day")["lowest_heart_rate"].mean()
    return lowest_heart_rate

def find_average_hrv(sleep_data_file):
    average_hrv = sleep_data_file.groupby("day")["average_hrv"].mean()
    return average_hrv

def find_total_sleep_duration(sleep_data_file):
    total_sleep_duration = sleep_data_file.groupby("day")["total_sleep_duration"].mean()
    return total_sleep_duration

def find_total_time_in_bed(sleep_data_file):
    total_time_in_bed = sleep_data_file.groupby("day")["time_in_bed"].mean()
    return total_time_in_bed

def plot_sleep_data(dates, average_heart_rate, lowest_heart_rate, average_hrv, total_sleep_duration, time_in_bed):
    plt.title("Victor's Sleep Data")
    plt.xlabel("Time (Y-M)")
    plt.ylabel("Heart Rate (BPM)")
    plt.plot(dates, average_heart_rate, color = "red", label = "Average Heart Rate")
    plt.plot(dates, lowest_heart_rate, color = "blue", label = "Lowest Heart Rate")
    #plt.plot(dates, average_hrv)
    plt.grid()
    plt.legend()
    plt.show()
    return

x = sleep_dataframe()

plot_sleep_data(sleep_data_dates(x), find_average_heart_rate(x), find_lowest_heart_rate(x), find_average_hrv(x), find_total_sleep_duration(x), find_total_time_in_bed(x))