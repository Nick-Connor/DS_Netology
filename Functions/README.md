# Task 1

We need to help the secretary automate the work. To do this, you need to write a program that will execute user commands based on the stored data.  

The source data has the following structure:  

list  
of all documents = [  
{'type': 'passport', 'number': '2207 876234', 'name': 'Vasily Gupkin'},  
{'type': 'invoice', 'number': '11-2', 'name': 'Gennady Pokemonov'},  
{'type': 'insurance', 'number': '10006', 'name': 'Aristarkh Pavlov'}  
]  
a list of shelves where documents are stored (if the document is in documents, then it must be in directories)  
directories = {  
'1': ['2207 876234', '11-2'],  
'2': ['10006'],  
'3': []  
}  
General program requirements:  

the code must be correctly decomposed (each function is responsible for its specific task, duplicated functionality is reused, and its code is not repeated);
there are no global variables in the code (with the exception of documents and directories);
user input is processed in a while loop until the user explicitly terminates the program (by entering the "q" command).  

# Задание 1

Нужно помочь секретарю автоматизировать работу. Для этого нужно написать программу, которая будет на основе хранимых данных исполнять пользовательские команды.  

Исходные данные имеют следующую структуру:  

перечень всех документов  
documents = [  
{'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},  
{'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},  
{'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}  
]  
перечень полок, на которых хранятся документы (если документ есть в documents, то он обязательно должен быть и в directories)  
directories = {  
'1': ['2207 876234', '11-2'],  
'2': ['10006'],  
'3': []  
}  
Общие требования к программе:  

код должен быть грамотно декомпозирован (каждая функция отвечает за свою конкретную задачу, дублирующийся функционал переиспользуется, а его код не повторяется);
в коде отсутствуют глобальные переменные (за исключением documents и directories);
пользовательский ввод обрабатывается в цикле while до тех пор, пока пользователь явно не завершит программу (вводом команды "q").  


# Point 1. The user can use the "p" command to find out the owner of the document by its number.  
Examples of work:  

Enter the command: p  
  
Enter the document number:  
10006  
Result:  
The owner of the document: Aristarkh Pavlov  

Enter the command:  
p  

Enter the document number:  
12345  
Result:  
The document was not found in the database  

# Пункт 1. Пользователь по команде "p" может узнать владельца документа по его номеру  
Примеры работы:  

Введите команду: p  

Введите номер документа:  
10006  
Результат:  
Владелец документа: Аристарх Павлов  

Введите команду:  
p  

Введите номер документа:  
12345  
Результат:  
Документ не найден в базе  

# Point 2. The user can use the "s" command to find out which shelf the document is stored on.
Examples of work:  

Enter the command:  
s  

Enter the document number:  
10006  
Result:  
The document is stored on the shelf: 2  

Enter the command:  
s  
  
Enter the document number:  
12345  
Result:  
The document was not found in the database  

# Пункт 2. Пользователь по команде "s" может по номеру документа узнать на какой полке он хранится
Примеры работы:  

Введите команду:  
s  

Введите номер документа:  
10006  
Результат:  
Документ хранится на полке: 2  

Введите команду:  
s  

Введите номер документа:  
12345  
Результат:  
Документ не найден в базе  

# Point 3. The user can see the full information on all documents by using the "l" command.
Example of work:  

Enter the command:  
l  
Result:  

No.: 2207 876234, type: passport, owner: Vasily Gupkin, storage shelf: 1  
No.: 11-2, type: invoice, owner: Gennady Pokemonov, storage shelf: 1  
No.: 10006, type: insurance, owner: Aristarkh Pavlov, storage shelf: 2  

# Пункт 3. Пользователь по команде "l" может увидеть полную информацию по всем документам
Пример работы:  

Введите команду:  
l  
Результат:  

№: 2207 876234, тип: passport, владелец: Василий Гупкин, полка хранения: 1  
№: 11-2, тип: invoice, владелец: Геннадий Покемонов, полка хранения: 1  
№: 10006, тип: insurance, владелец: Аристарх Павлов, полка хранения: 2  

# Point 4. The user can add a new shelf using the "ads" command
Examples of work:  

Enter the command:
ads  

Enter the shelf number:
10  
Result:
A shelf has been added. The current list of shelves is 1, 2, 3, 10.  

Enter the command:
ads  

Enter the shelf number:
1  
The result:
Such a shelf already exists. The current list of shelves is 1, 2, 3.

# Пункт 4. Пользователь по команде "ads" может добавить новую полку
Примеры работы:  

Введите команду:  
ads  

Введите номер полки:  
10  
Результат:  
Полка добавлена. Текущий перечень полок: 1, 2, 3, 10.  

Введите команду:  
ads  

Введите номер полки:  
1  
Результат:  
Такая полка уже существует. Текущий перечень полок: 1, 2, 3. 

# Point 5. The user can delete an existing shelf from the data by command "ds" (only if it is empty)
Examples of work:  

Enter the command:  
ds  

Enter the shelf number:
3  
Result:
The shelf is removed. Current list of shelves: 1, 2.  

Enter the command:  
ds  
  
Enter the shelf number:
1  
Result:  
There are documents on the shelf, remove them before removing the shelf. The current list of shelves is 1, 2, 3.  

Enter the command:  
ds  

Enter the shelf number:
4  
The result:
There is no such shelf. The current list of shelves is 1, 2, 3.

# Пункт 5. Пользователь по команде "ds" может удалить существующую полку из данных (только если она пустая)
Примеры работы:  

Введите команду:  
ds  

Введите номер полки:  
3  
Результат:  
Полка удалена. Текущий перечень полок: 1, 2.  

Введите команду:  
ds  
  
Введите номер полки:  
1  
Результат:  
На полке есть документа, удалите их перед удалением полки. Текущий перечень полок: 1, 2, 3.  

Введите команду:  
ds  

Введите номер полки:  
4  
Результат:  
Такой полки не существует. Текущий перечень полок: 1, 2, 3.  