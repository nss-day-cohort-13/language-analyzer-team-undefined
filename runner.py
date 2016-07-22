import argparse
from main import *

def runner():

    parser = argparse.ArgumentParser(description='analyze a block of text to generate sentiment, behavior, and domain, analysis')
    parser.add_argument('-p', metavar='<file path>', type=str, help='path to target input file')
    args = parser.parse_args()
    file_path = args.p
    user_input = str()
    if file_path != None:
        user_input = open(file_path, 'r').read()
        # user_input = file.read()
    else:
        usr_input = input("Please enter behavior search string: ")

    message = Msg(user_input)
    message.initialize()
    print(message.analysis)

if __name__ == '__main__':
    runner()
