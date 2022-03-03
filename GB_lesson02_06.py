product = []

for j in range(3):
    print('Введите информацию о товаре:')
    name = input('наименование: ')
    if name.isdigit():
        name = int(name)
    price = input('цена: ')
    if price.isdigit():
        price = int(price)
    q_ty = input('кол-во: ')
    if q_ty.isdigit():
        q_ty = int(q_ty)
    unit = input('ед: ')
    if unit.isdigit():
        unit = int(unit)
    c = dict(наименование = name, цена = price, количество = q_ty, ед = unit)
    d = (j + 1, c)
    product.append(d)

print(product)
z = []
x = []
y = []
w = {}
for i, j in enumerate(product[0][1]):
    z.append(j)
    for g in range(len(product)):
        x.append(product[g][1].get(z[i]))
    y.append(x)
    x = []
    w[z[i]] = y[i]

print(w)