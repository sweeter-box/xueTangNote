Scores = {'张小敬':85,'姚汝能':90,'檀棋':95,'李必':100,'徐宾':95}

for i in Scores:
    print(i+':'+str(Scores[i]))

#同学吉温，成绩60，需要把他加入到Scores里

Scores['吉温'] = 60

print(Scores)

print(Scores['张小敬'])