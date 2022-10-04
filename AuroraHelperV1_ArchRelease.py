import os
print("Select your Language\nВыберите ваш язык\n1.English\n2.Русский\n3.Azərbaycanca\n4.Україньска\nСделано с <3 от @Winduzyatka\nMade with <3 by @Winduzyatka\n@Winduzyatka tərəfindən <3 hazirlanib")
language=int(input())
if language == 1:
    print("Welcome to Aurora Helper!\nWhat you want to do?\n1.Show information about your OS and computer\n2.Full upgrade your system\n3.Free up disk space\n4.Exit")
elif language == 2:
    print("Добро пожаловать в Помощник Aurora!\nЧто вы хотите сделать?\n1.Показать информацию вашей ОС и компьютера\n2.Полностью обновить вашу систему\n3.Освободить место на диске\n4.Выход")
elif language == 3:
    print("Aurora köməkçi-yə xoş gəlmisiniz!\nNə etmək istəyirsiniz?\n1.Sistem və kompüter məlumatlarinizi göstərin\n2.Sisteminizi tamamilə yeniləyin\n3.Disk yerini boşaltin\n4.Çix")
elif language == 4:
    print("Вітаємо в Помічник Aurora!\nЩо ви хочете зробити?\n1.Показати інформацію про ПЗ та компьютера\n2.Повністью оновити вашу систему\n3.Звільнити місце на дискі\n4.Вийти")
action = int(input())
while action != 4:
        if action == 1:
            os.system("neofetch")
        if action == 2:
            os.system("sudo pacman -Syyu")
        if action == 3:
            os.system("sudo pacman -Scc") and os.system("sudo pacman -Rns $(pacman -Qtdq)") and os.system("rm -rf ~/.cache/*")
        if language == 1:
            print("What you want to do?\n1.Show information about your OS and computer\n2.Full upgrade your system\n3.Free up disk space\n4.Exit") 
        if language == 2:
            print("Что вы хотите сделать?\n1.Показать информацию вашей ОС и компьютера\n2.Полностью обновить вашу систему\n3.Освободить место на диске\n4.Выход")
        if language == 3:
            print("Nə etmək istəyirsiniz?\n1.Sistem və kompüter məlumatlarinizi göstərin\n2.Sisteminizi tamamilə yeniləyin\n3.Disk yerini boşaltin\n4.Çix")
        if language == 4:
            print("Що ви хочете зробити?\n1.Показати інформацію про вашу ОС та компьютера\n2.Повністью оновити вашу систему\n3.Звільнити місце на дискі\n4.Вийти")
        action = int(input())
        if action == 4 and language == 1:
            print("Goodbye!")
            break
        if action == 4 and language == 2:
            print("Пока!")
            break
        elif action == 4 and language == 3:
            print("Gulə gulə!")
            break
        elif action == 4 and language == 4:
            print("До побачення!")
            break
        

