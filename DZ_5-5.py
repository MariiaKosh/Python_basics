src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
#result = [23, 1, 3, 10, 4, 11]
result_st = set()
tmp = set()
for i in src:
    if i not in tmp:
        result_st.add(i)
    else:
        result_st.discard(i)
    tmp.add(i)
result = [i for i in src if i in result_st]
print(result)
