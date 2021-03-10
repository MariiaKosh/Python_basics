tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена', "Tom", "Eva", "Mary"]
classes = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

cl = {i: classes[i] for i in range(len(classes))}
#for i in range(len(tutors)):
#    res = tuple([tutors[i]] + [cl.get(i)])
#    print(res)

result = (tuple([tutors[i]] + [cl.get(i)]) for i in range(len(tutors)))
print("result: ", *result)
print("result_type: ", type(result))




