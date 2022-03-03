new_list = [10, 7, 5, 4, 3]
while True:
    new_one = input('Введите новый элемент рейтинга: ')
    if new_one.isalpha():
        print('ошибочка!')
        continue
    if int(new_one) <= 0:
        print('ошибочка!')
        continue
    new_one = int(new_one)
    break
for i in range(len(new_list) - 1, -1, -1):
    if new_list[i] >= new_one:
        new_list.insert(i + 1, new_one)
        break
if new_list[0] < new_one:
    new_list.insert(0, new_one)
print(new_list)
