import os
import json


tags = ['matplotlib','ggplot2','dataframe','numpy','tensorflow','hadoop','machine-learning','json','xml','plot','data-structures','keras','graph','pyspark','scikit-learn','dplyr','deep-learning','pandas','scipy','neural-network','datagrid','statistics','jupyter-notebook','mapreduce','nosql','time-series','dataset']
countQuestions = {}

countAnswered = {}
totalAnswers = {}

totalViewCount = {}

countRegisteredUser = {}
countDeletedUser = {}

f = open('./Data/PythonQuestions.csv', 'r', encoding='UTF-8')
total = 0
for line in f:
    total = total + 1
    if total == 1:
        continue
    question = line.split(',')

    # question[10] Tags
    qTags = question[10].split(';')

    # For each tag in question
    for tag in qTags:

        # If the tag in the list above
        if tag in tags:

            # Check if the tag has already been seen before
            if tag not in countQuestions:
                countQuestions[tag] = 0
                countAnswered[tag] = 0
                totalAnswers[tag] = 0
                totalViewCount[tag] = 0
                countRegisteredUser[tag] = 0
                countDeletedUser[tag] = 0

            if tag in countQuestions:
                countQuestions[tag] = countQuestions[tag] + 1

                # question[5] Is Answered
                if question[5] == 'True':
                    countAnswered[tag] = countAnswered[tag] + 1
                
                # question[8] Number of Answers
                if question[8] != 0:
                    totalAnswers[tag] = totalAnswers[tag] + int(question[8])

                # question[7] Number of Views
                if question[7] != 0:
                    totalViewCount[tag] = totalViewCount[tag] + int(question[7])

                # question[3] User type
                if question[3] == 'registered':
                    countRegisteredUser[tag] = countRegisteredUser[tag] + 1
                if question[3] == 'does_not_exist':
                    countDeletedUser[tag] = countDeletedUser[tag] + 1


f.close()


# print(countQuestions)
# print(countAnswered)
# print(totalAnswers)
# print(totalViewCount)
# print(countRegisteredUser)


f = open('python output.txt','a')
json1 = json.dumps(countQuestions)
f.write('Count of Questions per Tag \n')
f.write(json1)

json2 = json.dumps(countAnswered)
f.write('\nCount of Answered Questions per Tag \n')
f.write(json2)

json3 = json.dumps(totalAnswers)
f.write('\nTotal Number of Answers per Tag \n')
f.write(json3)

json4 = json.dumps(totalViewCount)
f.write('\nTotal Number of Views per Tag \n')
f.write(json4)

json5 = json.dumps(countRegisteredUser)
f.write('\nTotal Number of Questions posted by Registed Users per Tag \n')
f.write(json5)

json6 = json.dumps(countDeletedUser)
f.write('\nTotal Number of Questions posted by Deleted Users per Tag \n')
f.write(json6)

f.close()





countQuestions = {}

countAnswered = {}
totalAnswers = {}

totalViewCount = {}

countRegisteredUser = {}
countDeletedUser = {}
f = open('./Data/RQuestions.csv', 'r', encoding='UTF-8')
total = 0
for line in f:
    total = total + 1
    if total == 1:
        continue
    question = line.split(',')

    # question[10] Tags
    qTags = question[10].split(';')

    # For each tag in question
    for tag in qTags:

        # If the tag in the list above
        if tag in tags:

            # Check if the tag has already been seen before
            if tag not in countQuestions:
                countQuestions[tag] = 0
                countAnswered[tag] = 0
                totalAnswers[tag] = 0
                totalViewCount[tag] = 0
                countRegisteredUser[tag] = 0
                countDeletedUser[tag] = 0

            if tag in countQuestions:
                countQuestions[tag] = countQuestions[tag] + 1

                # question[5] Is Answered
                if question[5] == 'True':
                    countAnswered[tag] = countAnswered[tag] + 1
                
                # question[8] Number of Answers
                if question[8] != 0:
                    totalAnswers[tag] = totalAnswers[tag] + int(question[8])

                # question[7] Number of Views
                if question[7] != 0:
                    totalViewCount[tag] = totalViewCount[tag] + int(question[7])

                # question[3] User type
                if question[3] == 'registered':
                    countRegisteredUser[tag] = countRegisteredUser[tag] + 1
                if question[3] == 'does_not_exist':
                    countDeletedUser[tag] = countDeletedUser[tag] + 1


f.close()


# print(countQuestions)
# print(countAnswered)
# print(totalAnswers)
# print(totalViewCount)
# print(countRegisteredUser)


f = open('r output.txt','a')
json1 = json.dumps(countQuestions)
f.write('Count of Questions per Tag \n')
f.write(json1)

json2 = json.dumps(countAnswered)
f.write('\nCount of Answered Questions per Tag \n')
f.write(json2)

json3 = json.dumps(totalAnswers)
f.write('\nTotal Number of Answers per Tag \n')
f.write(json3)

json4 = json.dumps(totalViewCount)
f.write('\nTotal Number of Views per Tag \n')
f.write(json4)

json5 = json.dumps(countRegisteredUser)
f.write('\nTotal Number of Questions posted by Registed Users per Tag \n')
f.write(json5)

json6 = json.dumps(countDeletedUser)
f.write('\nTotal Number of Questions posted by Deleted Users per Tag \n')
f.write(json6)

f.close()