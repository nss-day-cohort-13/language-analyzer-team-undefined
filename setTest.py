from messages import messages

# def code():

uniqueSet = set()


def chopMessages():
    for entry in messages:
        word = entry["message"].split()
        
        if word != ',' and word != '.':
            uniqueSet.update(word)

    print(uniqueSet)


if __name__ == '__main__':
    chopMessages()

# import code
# code.interact(local=locals())