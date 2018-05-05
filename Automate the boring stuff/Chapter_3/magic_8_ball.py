import random
def getAnswer(answerNumber):
    if answerNumber==1:
        return 'It is certain'
    elif answerNumber==2:
        return 'It is decidely'
    elif answerNumber==3:
        return 'yes'
    elif answerNumber==4:
        return 'no'
    elif answerNumber==5:
        return 'Ask again later'
    elif answerNumber==6:
        return 'my reply is no'
    print(getAnswer(random.randint(1,9)))
