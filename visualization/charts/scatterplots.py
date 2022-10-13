from matplotlib import pyplot as plt

def scatterplot(*args, **kwargs):
    """
    args: 
        xvals - array like obj
        yvals - array like obj
        labels - array like obj
        xlabel - string
        ylabel - string
        title - strign
    """
    if len(args) == 2:
        xvals, yvals = args
    elif len(args) == 3:
        xvals, yvals, labels = args
    else:
        print("Invalid args")

    if 'xvals' in kwargs:
        xvals = kwargs['xvals']
    

    if 'yvals' in kwargs:
        yvals = kwargs['yvals']

    if 'labels' in kwargs:
        labels = kwargs['labels']

    if 'title' in kwargs:
        title = kwargs['title']

    if 'xlabel' in kwargs:
        xlabel = kwargs['xlabel']

    if 'ylabel' in kwargs:
        ylabel = kwargs['ylabel']


    plt.scatter(xvals, yvals)

    if kwargs.get('labels', None):
        for label, xval, yval in zip(labels, xvals, yvals):
            plt.annotate(label,
                        xy=(xval, yval),
                        xytext=(5, -5),
                        textcoords='offset points')

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

# Scatter plot of relationship between friends and minutes 
# spent on networking site

# friends = [ 70, 65, 72, 63, 71, 64, 60, 64, 67]
# minutes = [175, 170, 205, 120, 220, 130, 105, 145, 190]
# labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
# scatterplot(friends, minutes, labels, xlabel='# friends',
            #  ylabel='daily minutes spent on the site',
            #  title='Daily minutes vs. Number of Friends')


test_1_grades = [ 99, 90, 85, 97, 80]
test_2_grades = [100, 85, 60, 90, 70]
scatterplot(test_1_grades, test_2_grades, 
            xlabel='test 1 grades', 
            ylabel='test 2 grades',
            title='Axes aren\'t comparable')