import random
import matplotlib.pyplot as plt

def main():
    boolean_values1 = generateBooleanValues(500)
    boolean_values2 = generateBooleanValues(500)
    plotBooleanValues(boolean_values1, boolean_values2)
    return

def generateBooleanValue():
    n = random.randint(1,  1000)
    boolean = int(((1-(-1)**n))/2)
    return boolean

def generateBooleanValues(n):
    if n == 0:
        return []
    else:
        return [generateBooleanValue()] + generateBooleanValues(n - 1)

def plotBooleanValues(boolean_values1, boolean_values2):
    plt.title("Boolean Values")
    plt.xlabel("Iterations")
    plt.ylabel("Boolean Value")
    plt.plot(boolean_values1, color = "red", label = "Set 1")
    plt.plot(boolean_values2, color = "blue", label = "Set 2")
    plt.legend()
    plt.show()
    return

main()