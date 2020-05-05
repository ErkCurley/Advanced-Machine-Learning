import json
import os

f = open("./Data/RQuestionsAll.txt","r", encoding="utf-8")
f1 = open("./Data/RQuestions.csv","w", encoding="utf-8")

f1.write("question_id,title,ower_rep,user_type,accept_rate,is_answered,answer_id,view_count,answer_count,score,tags,created_date,edited_date,activity_date,closed_date,closed_reason")

count = 0
for i in f:
    data = json.loads(i)
    for j in data['items']:
        count = count + 1
        print(count)
        string = ''
        
        question = j
        
        string = string + str(question['question_id']) + ","
        string = string +'"'+ question['title'].replace('"','') + '",'

        if 'reputation' in question['owner']:
            string = string + str(question['owner']['reputation']) + ","
        else:
            string = string + ','
        
        string = string + question['owner']['user_type'] + ","
        
        if 'accept_rate' in question['owner']:        
            string = string + str(question['owner']['accept_rate']) + ","
        else:
            string = string + ","

        string = string + str(question['is_answered']) + ","

        if 'accepted_answer_id' in question:
            string = string + str(question['accepted_answer_id']) + ","
        else:
            string = string + ","
        
        string = string + str(question['view_count']) + ","
        string = string + str(question['answer_count']) + ","
        string = string + str(question['score']) + ","

        for k in question['tags']:
            string = string + k + ';'
        string = string + ","
        
        string = string + str(question['creation_date']) + ","
        
        if 'last_edit_date' in question:
            string = string + str(question['last_edit_date']) + ","
        else:
            string = string + ","

        if 'last_activity_date' in question:
            string = string + str(question['last_activity_date']) + ","
        else:
            string = string + ","

        if 'closed_date' in question:
            string = string + str(question['closed_date']) + ","
            string = string +'"'+ str(question['closed_reason']).replace('"','') + '",'
        else:
            string = string + ",,"
    
        string = string + '\n'

        f1.write(string)
   
f.close()
f1.close()