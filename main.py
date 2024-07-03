from datetime import datetime


def get_user_birthday():
    day = int(input("Введите день вашего рождения (дд): "))
    month = int(input("Введите месяц вашего рождения (мм): "))
    year = int(input("Введите год вашего рождения (гггг): "))
    return day, month, year


def get_day_of_week(day, month, year):
    date = datetime(year, month, day)
    days_of_week = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    return days_of_week[date.weekday()]


def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False


def calculate_age(day, month, year):
    today = datetime.today()
    birth_date = datetime(year, month, day)
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age


def display_birthday_as_stars(day, month, year):
    digit_to_stars = {
        '0': [" *** ", "*   *", "*   *", "*   *", " *** "],
        '1': ["  *  ", " **  ", "  *  ", "  *  ", " *** "],
        '2': [" *** ", "*   *", "   * ", "  *  ", "*****"],
        '3': [" *** ", "*   *", "  ** ", "*   *", " *** "],
        '4': ["*  * ", "*  * ", "*****", "   * ", "   * "],
        '5': ["*****", "*    ", "**** ", "    *", "**** "],
        '6': [" *** ", "*    ", "**** ", "*   *", " *** "],
        '7': ["*****", "   * ", "  *  ", " *   ", " *   "],
        '8': [" *** ", "*   *", " *** ", "*   *", " *** "],
        '9': [" *** ", "*   *", " ****", "    *", " *** "]
    }

    date_str = f"{day:02d} {month:02d} {year}"
    for i in range(5):
        line = ""
        for char in date_str:
            if char in digit_to_stars:
                line += digit_to_stars[char][i] + "  "
            else:
                line += "     "
        print(line)


def main():
    day, month, year = get_user_birthday()

    day_of_week = get_day_of_week(day, month, year)
    leap_year = is_leap_year(year)
    age = calculate_age(day, month, year)

    print(f"Вы родились {day_of_week}.")
    print(f"{'Это был високосный год.' if leap_year else 'Это не был високосный год.'}")
    print(f"Вам {age} лет.")
    print("Ваша дата рождения в формате дд мм гггг, где цифры прорисованы звёздочками:")
    display_birthday_as_stars(day, month, year)


if __name__ == "__main__":
    main()