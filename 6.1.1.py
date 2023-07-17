import sys


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def check_date(date):
    day, month, year = map(int, date.split('.'))
    

    if year < 1 or year > 9999:
        return False
    

    if month < 1 or month > 12:
        return False
    

    if month in [1, 3, 5, 7, 8, 10, 12]:
        max_day = 31
    elif month in [4, 6, 9, 11]:
        max_day = 30
    else:
        if is_leap_year(year):
            max_day = 29
        else:
            max_day = 28
    
    if day < 1 or day > max_day:
        return False
    
    return True


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Пожалуйста, укажите дату в формате DD.MM.YYYY в качестве аргумента командной строки.")
    else:
        date_to_check = sys.argv[1]
        if check_date(date_to_check):
            print("Дата может существовать.")
        else:
            print("Дата невозможна.")