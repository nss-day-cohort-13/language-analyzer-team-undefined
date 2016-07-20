
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
    
if __name__ == '__main__':
    piePlot()

