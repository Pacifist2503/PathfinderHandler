import os
import pyautogui
import pyperclip
import time

start = time.time()
# pyautogui.PAUSE = 0.2 # пауза между всеми операциями
pyautogui.FAILSAFE = True  # остановить прогу при наведении в левый верхний угол

dir_pic = r'Pic'

temp_name = ''
level = ''
door_name = ''
room_name = ''
ladder_name = ''
name_elem = ''
stop = False

level_list = set()
room_list = []
door_list = []
ladder_list = []
room_for_door_list = []
room_for_ladder_list = []

count = 0
count_level = 0

img_list_door = os.listdir(dir_pic + '\door')
img_list_ladder = os.listdir(dir_pic + '\ladder')


# приложение на весь экран
def fullApp():
    img_full = pyautogui.locateCenterOnScreen(dir_pic + r'\full.PNG', confidence=0.9)
    if img_full:
        pyautogui.click(pyautogui.moveTo(img_full, duration=1))
        pyautogui.press('down', presses=5, interval=0.1)
        pyautogui.press('enter', interval=0.1)


# открыть приложение
def open_app():
    paht = pyautogui.prompt(text='Введите полный путь к файлу', title='Выбор файла', default='')
    os.startfile(fr'{paht}')
    pyautogui.sleep(20)
    pyautogui.press('esc', interval=0.1)
    pyautogui.sleep(15)


# развернуть всё дерево
def addAll(c_l):
    for i in range(c_l):
        pyautogui.press('left', interval=0.2)
        pyautogui.press('up', interval=0.2)


# сменить клафиши по умолчанию (сортировка по алфавиту и выделение смежных объектов)
def cmena_klav():
    pyautogui.press('tab', interval=0.2)
    pyautogui.press('alt', interval=0.1)
    pyautogui.press('enter', interval=0.1)
    pyautogui.press('down', presses=5, interval=0.1)
    pyautogui.press('enter', interval=0.1)
    pyautogui.press('tab', interval=0.1)
    pyautogui.press('enter', interval=0.5)
    img_clear = pyautogui.locateCenterOnScreen(dir_pic + r'\clear.PNG', confidence=0.9)
    if img_clear:
        pyautogui.click(pyautogui.moveTo(img_clear, duration=0.5))
        pyautogui.press('tab', presses=3, interval=0.2)
    else:
        pyautogui.alert(text='Картинка для сброса не найдена', title='Внимание!', button='OK')
    pyautogui.press('up', interval=0.1)
    pyautogui.press('right', presses=3, interval=0.1)
    pyautogui.press('tab', interval=0.1)
    pyautogui.press('down', interval=0.1)
    pyautogui.press('right', interval=0.1)
    pyautogui.press('down', presses=32, interval=0.3)
    img_activ = pyautogui.locateCenterOnScreen(dir_pic + r'\activ.PNG', confidence=0.9)
    if img_activ:
        pyautogui.moveTo(img_activ, duration=0.5)
        pyautogui.click(pyautogui.moveRel(250, 0, duration=0.5))
        pyautogui.hotkey('shift', 'y', interval=0.1)
    else:
        pyautogui.alert(text='Картинка строки Выделение активного этажа не найдена', title='Внимание!', button='OK')
    img_alfavit = pyautogui.locateCenterOnScreen(dir_pic + r'\ch_button_2.PNG', confidence=0.9)
    if img_alfavit:
        pyautogui.moveTo(img_alfavit, duration=0.5)
        pyautogui.click(pyautogui.moveRel(250, 0, duration=0.5))
        pyautogui.hotkey('shift', 'a', interval=0.1)
    else:
        pyautogui.alert(text='Картинка строки Выделение по алфавиту не найдена', title='Внимание!', button='OK')
    img_vydel = pyautogui.locateCenterOnScreen(dir_pic + r'\ch_button_3.PNG', confidence=0.9)
    if img_vydel:
        pyautogui.click(img_vydel, duration=1)
        img_obch = pyautogui.locateCenterOnScreen(dir_pic + r'\ch_button_4.PNG', confidence=0.9)
        if img_obch:
            pyautogui.moveTo(img_obch, duration=0.5)
            pyautogui.click(pyautogui.moveRel(250, 0, duration=0.5))
            pyautogui.hotkey('shift', 't', interval=0.1)
        else:
            pyautogui.alert(text='Картинка строки Выбрать соединенные компоненты не найдена', title='Внимание!',
                            button='OK')
    else:
        pyautogui.alert(text='Картинка строки Выделение по алфавиту не найдена', title='Внимание!', button='OK')
    img_ok_1 = pyautogui.locateCenterOnScreen(dir_pic + r'\ok_1.PNG', confidence=0.9)
    if img_ok_1:
        pyautogui.click(pyautogui.moveTo(img_ok_1, duration=0.5))
    img_ok_2 = pyautogui.locateCenterOnScreen(dir_pic + r'\ok_2.PNG', confidence=0.9)
    if img_ok_2:
        pyautogui.click(pyautogui.moveTo(img_ok_2, duration=0.5))
    pyautogui.sleep(2)


# поставить курсор на этажи
def upd():
    img_upd = pyautogui.locateCenterOnScreen(dir_pic + r'\upd.PNG', confidence=0.9)
    if img_upd:
        pyautogui.click(pyautogui.moveTo(img_upd, duration=0.1))
        pyautogui.sleep(0.2)
    else:
        pyautogui.alert(text='Картинка обновления положения курсора не найдена', title='Внимание!', button='OK')


# расширение дерева
def toExpand():
    img_expand = pyautogui.locateCenterOnScreen(dir_pic + r'\expand.PNG', confidence=0.9)
    if img_expand:
        pyautogui.moveTo(img_expand, duration=0.1)
        pyautogui.moveRel(-20, 0, duration=0.1)
        temp_pos = pyautogui.position()
        pyautogui.dragTo(temp_pos[0] + 700, temp_pos[1], duration=0.3)
        pyautogui.sleep(0.2)
    else:
        pyautogui.alert(text='Картинка для расширения дерева не найдена', title='Внимание!', button='OK')


# получить имя элемента

def copy_name():
    pyautogui.sleep(0.1)
    pyautogui.press('f2', interval=0.2)
    pyautogui.hotkey('ctrl', 'c', interval=0.2)
    tm = pyperclip.paste()
    return tm


# вставить имя
def paste_name(name):
    pyautogui.sleep(0.1)
    pyperclip.copy(f'{name}')
    pyautogui.hotkey('ctrl', 'v', interval=0.2)
    pyautogui.press('enter', interval=0.2)


# удалить дефолтное наименование
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


# прыжок
def djamp(count_dj):
    if count_dj >= 49:
        if count_dj // 49 > 1:
            pyautogui.press('pagedown', presses=count_dj // 49, interval=0.2)
            pyautogui.press('up', presses=(count_dj // 49) - 1, interval=0.2)
            pyautogui.press('down', presses=count_dj % 49, interval=0.2)
        else:
            pyautogui.press('pagedown', presses=count_dj // 49, interval=0.2)
            pyautogui.press('down', presses=count_dj % 49, interval=0.2)
    else:
        pyautogui.press('down', presses=count_dj, interval=0.2)


doorError = 0


def mainCycle():
    global temp_name, stop, name_elem, doorError, count_level
    pyautogui.press('down', interval=0.1)
    tt = name_elem
    temp_name = copy_name()
    if tt == temp_name:
        stop = True
    if temp_name in door_list:
        pyautogui.alert(text='Ошибка - двери', title='Внимание!', button='OK')
        doorError += 1
        print(f'Количество ошибок с дверями = {doorError}')
        pyautogui.press('esc', interval=0.1)
        pyautogui.press('left', interval=0.1)
        djamp(count)
    elif temp_name[0:4] == 'Этаж':
        processing_level()
        count_level += 1
    elif temp_name[0:5] == 'Дверь':
        processing_door()
    elif temp_name[0:7] == 'Лестниц' or temp_name[0:4] == 'ампа':
        name_elem = temp_name
        pyautogui.press('esc', interval=0.1)
    elif temp_name[0:5] == 'Рампа':
        paste_name(f'1{temp_name}')
    else:
        processing_room(temp_name)


ladderError = 0


def mainCycle1():
    global temp_name, stop, name_elem, count, ladderError
    pyautogui.press('down', interval=0.1)
    tt = name_elem
    temp_name = copy_name()
    if tt == temp_name:
        stop = True
    if temp_name in ladder_list:
        pyautogui.alert(text='Ошибка - лестницы', title='Внимание!', button='OK')
        ladderError += 1
        print(f'Количество ошибок с лестницами = {ladderError}')
        pyautogui.press('esc', interval=0.1)
        pyautogui.press('left', interval=0.1)
        djamp(count)
    elif temp_name[0:4] == 'Этаж':
        processing_level()
    elif temp_name[0:5] == 'Дверь':
        count += 1
        name_elem = temp_name
        pyautogui.press('esc', interval=0.1)
    elif temp_name[0:7] == 'Лестниц' or temp_name[0:4] == '1Рам':
        count += 1
        processing_ladder()
    else:
        count += 1
        name_elem = temp_name
        pyautogui.press('esc', interval=0.1)


def mainCycle2(name_str_delet):
    global temp_name, stop, name_elem, count
    pyautogui.press('down', interval=0.1)
    tt = name_elem
    temp_name = copy_name()
    if tt == temp_name:
        stop = True
    if name_str_delet in temp_name:
        temp_name = delete_str(temp_name, name_str_delet)
    paste_name(temp_name)


def processing_level():
    global level, count, level_list, room_for_door_list, room_list, name_elem
    room_list = []
    room_for_door_list = []
    count = 0
    level = f'{temp_name[:2]}.{temp_name[5:]}'
    level_list.add(level)
    pyautogui.press('esc', interval=0.1)
    pyautogui.hotkey('shift', 'y', interval=0.1)
    pyautogui.press('add', interval=0.1)
    pyautogui.hotkey('shift', 'a', interval=0.1)
    name_elem = level


def processing_door():
    global temp_name, stop, count, door_name, name_elem
    count += 1
    temp_room_for_door_list = []
    pyautogui.press('esc', interval=0.3)
    for i in img_list_door:
        img_door = pyautogui.locateCenterOnScreen(dir_pic + f'/door/{i}', confidence=0.9)
        pyautogui.sleep(0.1)
        if img_door:
            pyautogui.moveTo(img_door, duration=0.1)
            temp_pos = pyautogui.position()
            pyautogui.hotkey('shift', 't', interval=0.1)
            pyautogui.press('enter', interval=0.3)
            pyautogui.dragTo(temp_pos[0] + 5, temp_pos[1], duration=1)
            pyautogui.moveRel(-50, 0, duration=0.3)
            pyautogui.press('down', interval=0.2)
            break
    for _ in range(2):
        pyautogui.press('up', interval=0.2)
        temp_name1 = copy_name()
        if temp_name1 != temp_name:
            nn = processing_room(temp_name1)
            temp_room_for_door_list.append(nn.replace(f' ({level})', ''))
            temp_room_for_door_list.sort()
        else:
            break
    pyautogui.press('up', interval=0.1)
    temp_name = copy_name()
    if len(temp_room_for_door_list) == 2:
        door_name = f'{temp_name[0:5]} между: {temp_room_for_door_list[0]} - {temp_room_for_door_list[1]} ({level})'
        if temp_room_for_door_list in room_for_door_list:
            door_name = f'{temp_name[0:5]} ({room_for_door_list.count(temp_room_for_door_list)}) между: {temp_room_for_door_list[0]} - {temp_room_for_door_list[1]} ({level})'
    else:
        door_name = f'Выход наружу из: {temp_room_for_door_list[0]} ({level})'
        if temp_room_for_door_list in room_for_door_list:
            door_name = f'Выход ({room_for_door_list.count(temp_room_for_door_list)}) наружу из: {temp_room_for_door_list[0]} ({level})'
    room_for_door_list.append(temp_room_for_door_list)
    door_list.append(door_name)
    paste_name(door_name)
    name_elem = door_name
    pyautogui.press('left', interval=0.1)
    pyautogui.hotkey('shift', 'a', interval=0.1)
    djamp(count)


def processing_ladder():
    global temp_name, stop, count, ladder_name, name_elem
    temp_room_for_ladder_list = []
    pyautogui.press('esc', interval=0.3)
    for i in img_list_ladder:
        img_ladder = pyautogui.locateCenterOnScreen(dir_pic + f'/ladder/{i}', confidence=0.9)
        pyautogui.sleep(0.1)
        if img_ladder and i == 'ladder.PNG':
            pyautogui.moveTo(img_ladder, duration=0.1)
            temp_pos = pyautogui.position()
            pyautogui.hotkey('shift', 't', interval=0.1)
            pyautogui.press('enter', interval=0.2)
            pyautogui.dragTo(temp_pos[0] + 5, temp_pos[1], duration=1)
            pyautogui.moveRel(-50, 0, duration=0.2)
            pyautogui.press('down', presses=2, interval=0.2)
            break
        elif img_ladder:
            pyautogui.moveTo(img_ladder, duration=0.1)
            temp_pos = pyautogui.position()
            pyautogui.hotkey('shift', 't', interval=0.1)
            pyautogui.press('enter', interval=0.2)
            pyautogui.dragTo(temp_pos[0] + 5, temp_pos[1], duration=1)
            pyautogui.moveRel(-50, 0, duration=0.2)
            pyautogui.press('up', interval=0.2)
            pyautogui.press('down', interval=0.2)
            break
    for _ in range(2):
        temp_name1 = copy_name()
        pyautogui.press('esc', interval=0.2)
        pyautogui.press('up', interval=0.2)
        if temp_name1 != temp_name:
            temp_room_for_ladder_list.append(temp_name1)
            temp_room_for_ladder_list.sort()
        else:
            break
    pyautogui.hotkey('ctrl', 'z', interval=0.1)
    pyautogui.press('left', interval=0.1)
    djamp(count)
    temp_name = copy_name()
    if temp_name[0:4] == 'Лест':
        ladder_name = f'Лест. марш между: {temp_room_for_ladder_list[0]} - {temp_room_for_ladder_list[1]} ({level})'
        if temp_room_for_ladder_list in room_for_ladder_list:
            ladder_name = f'Лест.марш между: ({room_for_ladder_list.count(temp_room_for_ladder_list)}): {temp_room_for_ladder_list[0]} - {temp_room_for_ladder_list[1]} ({level})'
    elif temp_name[0:4] == '1Рам':
        ladder_name = f'Пандус между: {temp_room_for_ladder_list[0]}-{temp_room_for_ladder_list[1]} ({level})'
        if temp_room_for_ladder_list in room_for_ladder_list:
            ladder_name = f'Пандус ({room_for_ladder_list.count(temp_room_for_ladder_list)}) между: {temp_room_for_ladder_list[0]} - {temp_room_for_ladder_list[1]} ({level})'
    room_for_ladder_list.append(temp_room_for_ladder_list)
    ladder_list.append(ladder_name)
    paste_name(ladder_name)
    name_elem = ladder_name


def processing_room(name):
    global stop, room_list, name_elem
    name1 = name
    if level not in name:
        name1 = f'{name} ({level})'
        if delete_str(name, 'Помещение') in room_list:
            name1 = f'{name} ({room_list.count(delete_str(name, "Помещение"))}) ({level})'
        paste_name(name1)
        room_list.append(delete_str(name, 'Помещение'))
    else:
        paste_name(name1)
    name_elem = name1
    return name1


open_app()
cmena_klav()
upd()
pyautogui.press('down', interval=0.3)
toExpand()
upd()

while True:
    mainCycle()
    if stop:
        pyautogui.press('enter', interval=0.1)
        end = time.time()
        time_delta = end - start
        pyautogui.alert(text=f'Обработка дверей и помещений завершена.\n'
                             f'Затрачено всего времени: {time_delta // 60} мин {round(time_delta % 60)} сек',
                        title='Внимание!', button='OK', timeout=5000)
        break

stop = False
addAll(count_level)

while True:
    mainCycle1()
    if stop:
        pyautogui.press('enter', interval=0.1)
        end = time.time()
        time_delta = end - start
        end_rez = pyautogui.confirm(text=f'Обработка элементов завершена.\n'
                                         f'Затрачено всего времени: {time_delta // 60} мин {round(time_delta % 60)} сек\n'
                                         f'Если хотите удалить часть наименование помещения, нажмите ОК',
                                    title='Внимание!', buttons=['OK', 'Cancel'])
        break

if end_rez == 'OK':
    name_room_delete = pyautogui.prompt(text='Введите наименование', title='Выбор файла', default='')
    stop = False
    addAll(count_level)
    while True:
        mainCycle2(name_room_delete)
        if stop:
            pyautogui.press('enter', interval=0.1)
            end = time.time()
            time_delta = end - start
            pyautogui.alert(
                text=f'Обработка завершена.\nЗатрачено всего времени: {time_delta // 60} мин {round(time_delta % 60)} сек',
                title='Внимание!', button='OK')
            break
