import enum
from matplotlib import pyplot as plt

movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

def bar_chart(xvals, yvals, xlabel='', ylabel='', title=''):
    xs = [i for i, _ in enumerate(xvals)]
    plt.bar(xs, yvals)
    
    if xlabel:
        plt.xlabel(xlabel)

    if ylabel:
        plt.ylabel(ylabel)
    
    if title:
        plt.title(title)

    plt.xticks([i for i, _ in enumerate(xvals)], xvals)
    plt.show()

bar_chart(movies, num_oscars, ylabel='# Academy Awards', title='My Favorite Movies')