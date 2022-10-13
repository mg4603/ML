from matplotlib import pyplot as plt
from collections import Counter

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

def histogram(vals, bucket_fn, xlabel='', ylabel='', title=''):
    hist_values = Counter(bucket_fn(val) for val in vals)

    plt.bar([x for x in hist_values.keys()],
            hist_values.values(),
            8)
    
    plt.axis([-5, 105, 0, 5])

    plt.xticks([10*i for i in range(11)])
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.show()
    
grades = [83,95,91,87,70,0,85,82,100,67,73,77,0]
decile = lambda grade: grade // 10 * 10

histogram(grades, decile, 'Decile', '# students', 'Distribution of exam grades')

movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

# bar_chart(movies, num_oscars, ylabel='# Academy Awards', title='My Favorite Movies')