import random

print('Welcome to Quiz Game!')

start = input('Do you want to play? Yes/No\n')

if start.lower() == 'no':
    print('Goodbye!')
    quit()
elif start.lower() != 'yes':
    print('Incorrect value!')
    quit()
else:
    print("Let's go!")
    totalPoints = 0

    questionsDict = {
        'What language is this program written in?\n': 'python',
        'What is the name of the language of hypertext markup?\n': 'html',
        'What language is used to create styles?\n': 'css',
        'What is the most popular scripting language?\n': 'javascript',
        'What language is used to program the backend?\n': 'php',
        'What language allows you to work with the database?\n': 'sql'
    }

    randomList = []
    for k, v in questionsDict.items():
        randomList.append((k,v))

    random.shuffle(randomList)

    newQuestionsDict = dict()

    for item in randomList:
        newQuestionsDict[item[0]] = item[1]

    for k, v in newQuestionsDict.items():
        answer = input(k)

        if answer.lower() == v:
            totalPoints += 1
            print('Correct!\n')
            print('You points:', totalPoints)
        else:
            print('Incorrect!\n')
            print('You points:', totalPoints)

    print('You finished game! Correct answers:', totalPoints)