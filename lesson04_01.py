from sys import argv
def zp(hours, time_rate, bonus):
    return hours * time_rate + bonus


try:
    file_name, hours, time_rate, bonus = argv
    hours = float(hours)
    time_rate = float(time_rate)
    bonus = float(bonus)
    print(f'ЗП согласно отработанным часам - ({hours}) и премии в размере {bonus} рублей составляет -', zp(hours, time_rate, bonus), 'рублей', end='\n\n\n')
except ValueError:
    print('ошибка ввода - после имени файла по расчету ЗП в командой строке введите кол-во отработанных часов, ставку за час работы и премию через пробел.', end='\n\n\n')

