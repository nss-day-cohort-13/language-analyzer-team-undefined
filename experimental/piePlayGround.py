
import sys
sys.path.append("..")  # Adds higher directory to python modules path.
from main import *


def piePlot():

    response = input("Please enter behavior search string: ")
    message = Msg(response).words

    analyze = Analyze()
    behaviors = analyze.analyze_behavior(message)
    print(behaviors)

    domains = analyze.analyze_domain(message)
    print(domains)

    for tup in behaviors:
        print(tup[1])
if __name__ == '__main__':
    piePlot()

