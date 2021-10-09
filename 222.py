a = 'Лест. марш между: Помещение26 Коридор 1 (Эт.1) - Помещение39 Коридор 2 (Эт.1) (Эт.1)'
aa = 'Помещение'
aaa = '1-Помещение45'
aaaa = 'Помещение26'


def delete_str(all_str, delete_str):
    new_list = []
    all_str = all_str.split(' ')
    for i in all_str:
        if delete_str not in i:
            new_list.append(i)
        elif delete_str in i:
            if len(i) > len(delete_str):
                i = i.replace(i[i.find(delete_str):], '')
                if i != '':
                    new_list.append(i)
            else:
                new_list.append(i)
    return ' '.join(new_list)


print(delete_str(a, aa))

