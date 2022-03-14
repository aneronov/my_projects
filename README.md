anton = ['a', 'n', 't', 'o', 'n']
num = int(input())
ref = []
count = 0
count_list = []
for i in range(num):
    ref.append(input())
for j in range(len(ref)):
    strt = 0
    for i in anton:
        for k in range(strt, len(ref[j])):
            if i in ref[j]:
                count += 1
                strt = ref.index(i)
        print(count)
    if count == 5:
        count_list.append(j + 1)
    count = 0
print(*count_list)
