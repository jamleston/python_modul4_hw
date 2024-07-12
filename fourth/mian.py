# 1. Команда "hello", тут можна обійтись поки без функції та використати звичайний print:

# Введення: "hello"
# Вивід: "How can I help you?"
# 2. Команда "add [ім'я] [номер телефону]". Для цієї команди зробимо функцію add_contact:

# Введення: "add John 1234567890"
# Вивід: "Contact added."
# 3. Команда "change [ім'я] [новий номер телефону]". Для цієї команди зробимо функцію change_contact:

# Введення: "change John 0987654321"
# Вивід: "Contact updated." або повідомлення про помилку, якщо ім'я не знайдено
# 4. Команда "phone [ім'я]". Для цієї команди зробимо функцію show_phone:

# Введення: "phone John"
# Вивід: [номер телефону] або повідомлення про помилку, якщо ім'я не знайдено
# 5. Команда "all". Для цієї команди зробимо функцію show_all:

# Введення: "all"
# Вивід: усі збережені контакти з номерами телефонів
# 6. Команда "close" або "exit". Оскільки тут треба перервати виконання програми, можна поки обійтись без функції для цих команд:

# Введення: будь-яке з цих слів
# Вивід: "Good bye!" та завершення роботи бота


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact updated."

def show_phone(arg, contacts):
    result = contacts[arg]
    return result

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == 'change':
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()