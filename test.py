def validation_number(number):
    while True:
        type_number = type(number)
        template_type_num = type(1)
        if type_number ==  template_type_num:
            return number
            break
        else:
            print("Podaj liczbę nie stringa :) ")
            break
#<class 'int'>

validation_number("te")