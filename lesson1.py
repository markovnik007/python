# coding : utf-8

# Коментарий

print("Калькулятор v0.0.1")
print("Привет программист)")
name = input("Введите ваше имя:")
print (name, ", добро пожаловать в мир Python!")

answer = input("Поработаем? (Y/N)")
#PEP-8 Рекомендации по оформлению кода Python
if answer == "Y":
	print("Чем бы ты хотел(а) заняться", name,"?")
	print("1) Варим борщ")
	print("2) Варим не борщ")
	choice = int(input("Что будем делать?"))
	if choice == 1:
		print("Варю борщ!!! Буль буль...")
	elif choice == 2:
		print("Варю не борщ!")
	else:
		print("Ничего не варю...")
else:
	pass
if answer == "N":
	print("Давай досвидания", name,"!")
else:
	pass
	
