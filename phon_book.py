import string

def print_result(result):
     return print(result)
      

def work_with_phonebook():
    choice=show_menu()
    phone_book=read_txt('phon.txt')
    while (choice!=8):
        if choice==1:
            print_result(phone_book)
            return      
        elif choice==2:
            last_name=input('lastname ')
            print(find_by_lastname(phone_book,last_name))
            return
        elif choice==3:
            new_number=input('new  number ')
            print(change_number(phone_book,new_number))
            return
        elif choice==4:
            subscriber = input("введите данные абонента ")
            y = open('phon.txt', 'a', encoding='utf-8')
            y.write('\n')
            y.write(subscriber)
            y.write('\n')
            y.close
            return
            
        elif choice==5:
            save = open('phon_book.txt', 'wt', encoding='utf-8')
            for i in phone_book:
                data = str(i)
                data = data.translate(str.maketrans('', '', string.punctuation))
                save.write('\n')
                save.write(data)
            return
        elif choice==6:
            s = input("Введите нужную строку ")
            s = int(s)
            file = open('phon.txt', 'r', encoding='utf-8')
            file1 = file.readlines()
            x = 1
            for line in file1:
                if x==s:
                    copy_file = open('phon_book.txt', 'a', encoding='utf-8')
                    copy_file.writelines(line)
                    copy_file.close
                    x+=1
                x+=1
            return

            
        elif choice==7:
            return
        choice=show_menu()

def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
		# изменить данные
          "5. Сохранить справочник в текстовом формате\n"
          "6. Скопировать строку из одного файла в другой\n"
          "7. Закончить работу")
    choice = int(input())
    return choice

def read_txt(filename): 
    phone_book=[]
    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open(filename,'r',encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.split(',')))
            phone_book.append(record)	
    return phone_book

def write_txt(filename , phone_book):
    with open(filename,'w',encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s=''
            for v in phone_book[i].values():
                s = s + v + ','
            phout.write(f'{s[:-1]}\n')

def find_by_lastname(x,y):
    for i in range(len(x)):
        if y in x[i].values():
            return(x[i])
    
def change_number(x,y):
    for i in range(len(x)):
        if y in x[i].values():
            return(x[i])

    
work_with_phonebook()