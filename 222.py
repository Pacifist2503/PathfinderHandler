# a = 'Лест. марш между: Помещение26 "Коридор 1" (Эт.1) - Помещение39 Коридор 2 (Эт.1) (Эт.1)'
a = 'Помещение323  Лестничная площадка -2,500'
aa = 'Помещение'
aaa = '1-Помещение45'
aaaa = 'Помещение26'


def delete_simb(all_str):
    new_list = []
    all_str = all_str.split(' ')
    for i in all_str:
        if i == '':
            pass
        elif i[0] or i[-1] == '"':
            i = i.replace('"', '')
            new_list.append(i)
    return ' '.join(new_list)


print(delete_simb(a))

