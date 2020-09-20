import logging

logging.basicConfig(level=logging.DEBUG)


def asking():

    choice_number = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
    first_number = input("Podaj pierwszą liczbę ")
    second_number = input("Podaj drugą liczbę ")
    logging.info(f"Pobrano działanie {choice_number} Pierwsza liczba to {first_number} druga liczba to {second_number}")

#Da się zagnieździć funkcje we funkcji ? Jak zagnieździć tutaj całe te ify i elify ?
    if choice_number == 1:
        adding(first_number, second_number)
    elif choice_number == 2:        
        removal(first_number, second_number)

    return choice_number, first_number, second_number

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
result_asking = asking()
print(type(result_asking[1]))
if int(result_asking[0]) == 1:
    adding(result_asking[1], result_asking[2])
elif int(result_asking[0]) == 2:
    removaling(result_asking[1], result_asking[2])
elif int(result_asking[0]) == 3:
    multiplicationing(result_asking[1], result_asking[2])
elif int(result_asking[0]) == 4:
    divisioning(result_asking[1], result_asking[2])








