def calculator(dzialanie, a, b):
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        print('Wprowadziłeś złą wartość')
        return None

    try:
        if dzialanie == 'dodawanie':
            return a + b
        elif dzialanie == 'odejmowanie':
            return a - b
        elif dzialanie == 'mnozenie':
            return a * b
        elif dzialanie == 'dzielenie':
            try:
                return a / b
            except ZeroDivisionError:
                print('Nie można dzielić przez zero')
                return None
        else:
            print('Nieprawidłowe działanie')
            return None
    except ValueError:
        print('Wprowadź poprawną liczbę')
        return None

dzialanie = input('Wybierz spośród wymienionych działań, jakie chcesz wykonać: dodawanie, odejmowanie, mnożenie, dzielenie: ')
print('Wprowadź swoje liczby: ')
a = input('Podaj liczbę a = ')
b = input('Podaj liczbę b = ')

wynik_dzialania = calculator(dzialanie, a, b)
if wynik_dzialania is not None:
    print('Wynik Twojego działania to:', wynik_dzialania)
