from matplotlib import pyplot as plt

years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]


def line_chart(xvalues, yvalues, color='green', marker='o', 
               linestyle='solid', title='', xlabel='', ylabel=''):
    plt.plot(
        xvalues, yvalues, 
        color=color, 
        marker=marker, 
        linestyle=linestyle
    )

    if title:
        plt.title(title)

    if ylabel:
        plt.ylabel(ylabel)

    if xlabel:
        plt.xlabel(xlabel)

    plt.show()

line_chart(years, gdp, title='Nominal GDP', ylabel='Billions of %')