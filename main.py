import logging

logging.basicConfig(level=logging.DEBUG)


def adding(first_number, second_number):
    #  new_number = sum(int(first_number), int(second_number)) #Dlaczego to nie zadziała ???
    new_number = int(first_number) + int(second_number)
    logging.info(f"Dodaję {first_number} i {second_number}")
    print(new_number)
    return(new_number)

def removaling(first_number, second_number):
    new_number = int(first_number) - int(second_number)
    logging.info(f"Odejmuję {first_number} i {second_number}")
    print(new_number)
    return new_number

def multiplicationing(first_number, second_number):
    new_number = int(first_number) * int(second_number)
    logging.info(f"Mnoze {first_number} i {second_number}")
    print(new_number)
    return new_number

def divisioning(first_number, second_number):
    new_number = int(first_number) / int(second_number)
    logging.INFO(f"Dziele {first_number} i {second_number}")
    print(new_number)
    return new_number


### Czy to wszystko da się przesunąć do funkcji asking ?
# result_asking = asking()
# print(type(result_asking[1]))
# if int(result_asking[0]) == 1:
#     adding(result_asking[1], result_asking[2])
# elif int(result_asking[0]) == 2:
#     removaling(result_asking[1], result_asking[2])
# elif int(result_asking[0]) == 3:
#     multiplicationing(result_asking[1], result_asking[2])
# elif int(result_asking[0]) == 4:
#     divisioning(result_asking[1], result_asking[2])


def input_action():
    while True:
        action = input('Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ')
        if action in '1234':
            return action

def input_number(message):
    number = input(message)
    # TODO sprawdzic czy to liczba
    return number

if __name__ == '__main__':
    while True:
        action = input_action()
        number1 = input_number("Podaj składnik 1.")
        number2 = input_number("Podaj składnik 2.")

        if action == '1':
            adding(number1, number2)
            break
        elif action == '2':
            removaling(number1, number2)
        elif action == "3":
            multiplicationing(number1, number2)
        # number1 = input_number()
        # ...
        # if action == '1':
        #     add(number1, ...)



# >> Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: 1
# Podaj składnik 1. 2.3
# Podaj składnik 2. 5.4
# Dodaję 2.30 i 5.40
# Wynik to 7.70