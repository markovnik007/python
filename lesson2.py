# coding : utf-8

import os
import sys
import shutil
import psutil	#сторонний

# Коментарий

print("Калькулятор v0.0.1")
print("Привет программист)")
name = input("Введите ваше имя:")
print (name, ", добро пожаловать в мир Python!")

answer = ""
#PEP-8 Рекомендации по оформлению кода Python
while answer !="q":
	answer = input("Поработаем? (Y/N/q)")
	if answer == "Y":
		print("Чем бы ты хотел(а) заняться", name,"?")
		print("1) Выводим список файлов")
		print("2) Выводим информацию о системе")
		print("3) Выводим список процессов")
		print("4) Продублирую файлы в текущей директории")
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
		elif choice == 4:
			print("Создание бэкапов в текущей директории")
			file_list = os.listdir()
			i = 0
			while i < len(file_list):
				if os.path.isfile(file_list[i]):
					newfile = file_list[i] + ".bak"
					shutil.copy(file_list[i], newfile)
				i = i + 1
		else:
			pass
	else:
		pass
	if answer == "N":
		print("Давай досвидания", name,"!")
	else:
		pass
	
