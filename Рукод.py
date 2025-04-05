'''
      =:=--=.=                            =-*+++.=    
     =:+@@@@++-.=                      -+:++@@@@+ #   
     @ @@@@@@@@+.+= =-:.+@%%%%%%@+ :-+:+@@@@@@@@@@-   
      :+@@@@@@@@@++*+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@%   
      %+@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=   
       # @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    
        # @@@@@@@@@*=.-=          ===@@@@@@@@@@@@     
       :*@@@@@@@*+-                    =@@@@@@@@@@=   
      *+@@@@@@#:        =--:--=   =------=@@@@@@@@#=  
     +@@@@@@+*      -+#*+@@@@@+*#+=@@@@@@#==@@@@@@@#= 
    *+@@@@@.-     --+@@@@@@@@@@@@@@@@@@@@#   @@@@@@@= 
   =+@@@@@*=     ++@@@@@@@@@@@@@@@@@@@@@@#   @@@@@@@+=
   =@@@@@@#     *+@@@@@@@@@===@@@@@@@@@@@#    @@@@@@@@
   .@@@@@.     =+@@@@@@@=       =@@@@@@@@#    @@@@@@@@
  @+@@@@@=     @@@@@@@@=         =@@@@@@@#    @@@@@@@@
  @@@@@@@=     @@@@@@@@           @@@@@@@#    @@@@@@@@
  = @@@@@-     @@@@@@@@=         @@@@@@@@#   @@@@@@@@=
   :@@@@@+=    =@@@@@@@@=       =@@@@@@@@# =@@@@@@@@@ 
   *@@@@@@=     @@@@@@@@@@=====@@@@@@@@@@@@@@@@@@@@=  
   =:@@@@@+*    =@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=   
    -*@@@@@++=    =@@@@@@@@@@@@@@@@@@@@@@@@@@@@@=     
     %*@@@@@@#:    =@@@@@@@@@@@@@@@@@@@@@@@@==        
      =:@@@@@@+#:=     ========   =====@#=*=          
       =++@@@@@@@*=:=               =:=*@@@:-         
         ==+@@@@@@@@+*%=..::-:::.=%*+@@@@@@@+==       
           =*#+@@@@@@@@@@@@@@@@@@@@@@@@@@@@*+-        
              -+%+@@@@@@@@@@@@@@@@@@@@@+#+-           
                   +@++@+@@@@@@@++@@+   -             

                    Всем привет!
    Я тут решил переделать рукод под питон. Сразу говорю версия не стабильная!
    Список команд Рукод:
    help
    бу!
    print
    logo
    open
    count
    searh
    openrucodefile
    readfile
                    Приятного использования!
'''

import webbrowser as wb
import re

def load(): # Эта функция отвечает за загрузку ресурорсов кода
    global logo
    global version
    global comands
    with open('код языка\ресурсы\logo.txt', 'r', encoding='utf-8') as file:
        logo = file.read()
        
        
    with open('код языка\ресурсы\настройки.txt', 'r', encoding='utf-8') as filee:
        version = filee.read()
        
        #print(data2)

    with open('код языка\ресурсы\команды.txt', 'r', encoding='utf-8') as fileee:
        comands = fileee.read()
        #global comands
        #print(data2)
        
def open_code(file_path):# Эта функция отвечает за выполнения кода из файла
    with open(file_path, 'r', encoding='utf-8') as ffile:
        for line in ffile:
            if "@" in line:
                parts = line.split('@')  # Разделяем строку по точке
            
                after_dot = parts[1]  # Берем часть строки после первой точки
                #print(after_dot)  # Выводим: com
                result = line.split('@')[0]
                #print(result)  # Вывод: "пример"
                command(result,after_dot)
            else:
                #print("Точка не найдена")
                #text = "пример.текст"
                command(line.split(),0)

def command(comand,i): # Эта функция отвечает за исполнение комманд
    if comand in comands:
        if comand == "help":
            print(comands)
        if comand == "бу!":
            print("бу!")
        if comand == "logo":
            print(logo)
        if comand == "print":
            if i == 0:
                rint = input("Введите текст:")
                print(rint)
            else:
                print(i)
        if comand == "open":
            path = input("Введите путь к файлу:")
            if not ".txt" in path:
                print("Формат файла должен быть только .txt!")
            else:
                print("Фаил успешно прочтён!")
                with open(path, 'r', encoding='utf-8') as userfile:
                    global readfile
                    readfile = userfile.read()
        if comand == "readfile":
                print(readfile)
        if comand == "count":
            print("Ответ:", eval(input('Введите пример:')))
        if comand == "if":
            print(eval(i))
        if comand == "searh":
            wb.open(input("Что вы хотели найти:"))
        if comand == "openrucodefile":
            open_code(input("Введите путь к файлу:"))
        
    else:
        print("Ошибка! Введена команда:", comand, ", не верный синтаксис")
    

global userfile
load()
print(logo)
print(version)
while True:
    #command = input("Команда:")
    command(input("Команда:"),0)
    
        
        
