import json

with open('原子回声1091条问答对.json', 'r',encoding='utf-8') as file:
    qas = json.load(file)

from pprint import pprint

pprint(qas)
for qa in qas:
    question = qa.get('questionDetail')
    answer = qa.get('answer').get('answerDetail')
    origin = '原子回声'
    versionTime = qa.get('answer').get('versionTime')
    score = qa.get('answer').get('score')
    type = qa.get('type')

    row = (question, answer, origin, versionTime, score, type)
    print(row)
print(len(qas))
