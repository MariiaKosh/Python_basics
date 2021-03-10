def num_gen():
    user_in = int(input("Укажите число:  "))
    for i in range(1, user_in + 1, 2):
        yield i


for num in num_gen():
    print(num)


