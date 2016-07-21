from main import *

def runner():
    response = input("Please enter behavior search string: ")
    message = Msg(response)
    message.output_analysis()

if __name__ == '__main__':
    runner()
