from main import *

def runner():
    response = input("Please enter behavior search string: ")
    message = Msg(response)
    print(message.create_analysis_output())

if __name__ == '__main__':
    runner()
