new_list = []

while True:
    input_data = input('Введите элемент списка(для завершения введите - break): ')
    if input_data == 'break':
        break
    new_list.append(input_data)

for i in range(0, len(new_list) - 1, 2):
    new_list[i], new_list[i + 1] = new_list[i + 1], new_list[i]

print(new_list)
