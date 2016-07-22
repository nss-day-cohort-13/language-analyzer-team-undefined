import sys
sys.path.append("..")  # Adds higher directory to python modules path.
from main import *
import matplotlib.pyplot as plt


def piePlot():

    response = input("Please enter behavior search string: ")
    message = Msg(response).words

    analyze = Analyze()
    behaviors = analyze.analyze_behavior(message)
    domains = analyze.analyze_domain(message)

    # Behavior
    behavior_entries = list()
    behavior_numbers = list()
    behavior_explode = list()

    # Domain
    domain_entries = list()
    domain_numbers = list()
    domain_explode = list()

    for tup in behaviors:
        behavior_numbers.append(tup[1])
        behavior_entries.append(tup[0].title())

        # make the first element of the list pop out of the chart
        if tup == behaviors[0]:
            behavior_explode.append(0.1)
        else:
            behavior_explode.append(0)

    for tup in domains:
        domain_numbers.append(tup[1])
        domain_entries.append(tup[0].title())

        if tup == domains[0]:
            domain_explode.append(0.1)
        else:
            domain_explode.append(0)

    # Data to plot
    labels = behavior_entries
    sizes = behavior_numbers
    colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'blueviolet',
              'cadetblue', 'turquoise']

    # Behavior Plot
    plt.figure(1)
    plt.pie(sizes, explode=behavior_explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    plt.show()

    labels = domain_entries
    sizes = domain_numbers

    # Domain Plot
    plt.figure(2)
    plt.pie(sizes, explode=domain_explode, labels=labels, colors=colors,
            autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    plt.show()

if __name__ == '__main__':
    piePlot()
