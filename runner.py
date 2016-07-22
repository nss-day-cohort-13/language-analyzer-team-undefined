from main import *

def runner():
    response = input("Please enter behavior search string: ")
    message = Msg(response)
    message.initialize()
    print(message.analysis)

if __name__ == '__main__':
    runner()
