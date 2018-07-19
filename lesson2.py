# coding : utf-8

import os
import sys
import psutil	#сторонний

# Коментарий

print("Калькулятор v0.0.1")
print("Привет программист)")
name = input("Введите ваше имя:")
print (name, ", добро пожаловать в мир Python!")

answer = input("Поработаем? (Y/N)")
#PEP-8 Рекомендации по оформлению кода Python
if answer == "Y":
	print("Чем бы ты хотел(а) заняться", name,"?")
	print("1) Выводим список файлов")
	print("2) Выводим информацию о системе")
	print("3) Выводим список процессов")
	choice = int(input("Что будем делать?"))
	
	if choice == 1:
		print(os.listdir())
	elif choice == 2:
		print("Информация о пользователе:", os.getlogin())
		print("Текущая директория", os.getcwd())
		print("Платформа ОС:", sys.platform)
		print("Количество CPU:", os.cpu_count())
	elif choice == 3:
		print(psutil.pids())
	else:
		pass
else:
	pass
if answer == "N":
	print("Давай досвидания", name,"!")
else:
	pass
	
