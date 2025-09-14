# исходные данные

# перечень всех документов
documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
]

# перечень полок, на которых хранятся документы
directories = {"1": ["2207 876234", "11-2"], "2": ["10006"], "3": []}

# point 1
# поиск владельца по номеру документа ("p")


def get_owner_by_doc_number(doc_number):
    for doc in documents:
        if doc["number"] == doc_number:
            return doc["name"]
    return None


# point 2
# поиск полки по номеру документа ("s")


def get_shelf_by_doc_number(doc_number):
    for shelf, docs in directories.items():
        if doc_number in docs:
            return shelf
    return None


# point 3
# вывод информации по всем документом ("l")


def list_all_documents():
    result = []
    for doc in documents:
        shelf = get_shelf_by_doc_number(doc["number"])
        result.append(
            f"№: {doc['number']}, тип: {doc['type']}, владелец: {doc['name']}, полка хранения: {shelf}"
        )
    return "\n".join(result)


# point 4
# добавление новой полки ("ads")


def add_shelf(shelf_number):
    if shelf_number in directories:
        return f"Такая полка уже существует. Текущий перечень полок: {', '.join(sorted(directories.keys()))}."
    directories[shelf_number] = []
    return f"Полка добавлена. Текущий перечень полок: {', '.join(sorted(directories.keys()))}."


# point 5
# удаление полки ("ds")


# the main program cycle
def delete_shelf(shelf_number):
    if shelf_number not in directories:
        return f"Такой полки не существует. Текущий перечень полок: {', '.join(sorted(directories.keys()))}."
    if directories[shelf_number]:
        return f"На полке есть документа, удалите их перед удалением полки. Текущий перечень полок: {', '.join(sorted(directories.keys()))}."
    del directories[shelf_number]
    return f"Полка удалена. Текущий перечень полок: {', '.join(sorted(directories.keys()))}."


def main():
    while True:
        command = input("\nВведите команду: ").lower()

        if command == "q":
            break

        elif command == "p":
            doc_number = input("Введите номер документа: ")
            owner = get_owner_by_doc_number(doc_number)
            print(
                f"Владелец документа: {owner}" if owner else "Документ не найден в базе"
            )

        elif command == "s":
            doc_number = input("Введите номер документа: ")
            shelf = get_shelf_by_doc_number(doc_number)
            print(
                f"Документ хранится на полке: {shelf}"
                if shelf
                else "Документ не найден в базе"
            )

        elif command == "l":
            print(list_all_documents())

        elif command == "ads":
            shelf_number = input("Введите номер полки: ")
            print(add_shelf(shelf_number))

        elif command == "ds":
            shelf_number = input("Введите номер полки: ")
            print(delete_shelf(shelf_number))

        else:
            print("Неизвестная команда. Доступные команды: p, s, l, ads, ds, q")


# Запуск программы
main()
