import logging

logging.basicConfig(level=logging.DEBUG)


def asking():

    choice_number = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")
    first_number = input("Podaj pierwszą liczbę ")
    second_number = input("Podaj drugą liczbę ")
    logging.info(f"Pobrano działanie {choice_number} Pierwsza liczba to {first_number} druga liczba to {second_number}")


asking()