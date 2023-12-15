import pandas as pd
import matplotlib.pyplot as plt

# Courtesy of Victor Van

def file():
    data = pd.read_csv("solar spectra.csv").drop(list(range(48))) # Your data is a damn mess.
    data = data.iloc[:-1]
    return data

def define_data(data):
    data = data.rename(columns = {data.columns[0]: "Wavelength (Nanometers)", data.columns[1]: "Power Density (Watts/Meter^3)"})
    data["Wavelength (Nanometers)"] = pd.to_numeric(data["Wavelength (Nanometers)"], errors = "coerce")
    data["Power Density (Watts/Meter^3)"] = pd.to_numeric(data["Power Density (Watts/Meter^3)"], errors = "coerce")
    data = data[data["Wavelength (Nanometers)"] % 2 == 0]
    stuff = data.groupby("Wavelength (Nanometers)")["Power Density (Watts/Meter^3)"].max()
    return stuff

def plot_data(stuff):
    plt.title("Spectra of the Sun")
    plt.scatter(stuff.index, stuff.values)
    plt.xlabel("Wavelength (Nanometers)")
    plt.ylabel("Power Density (Watts/Meter^3)")
    y = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
    x = [300, 350, 400, 450, 500, 550, 600, 650, 700, 750]
    plt.xticks(x)
    plt.yticks(y)
    plt.grid()
    plt.show()
    return

x = file()
stuff = define_data(x)
plot_data(stuff)