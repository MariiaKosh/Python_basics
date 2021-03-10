src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

#resoooo = [src[i] if src[i] > src[i-1] else +i for i in range(1, len(src))]
#print(resoooo)

result = []
for i in range(1, len(src)):
    if src[i] > src[i-1]:
        result.append(src[i])
    else:
        i += 1
print(result)
