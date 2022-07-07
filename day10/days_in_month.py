def is_leap(p_year):
    if p_year % 4 == 0:
        if p_year % 100 == 0:
            if p_year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(p_year, p_month):
    """
    This function takes the input of a certain year and month. Then it will return how many days there are during this
    month during this year

    :param p_year: Input year
    :param p_month: Input month
    :return: Days in the input month during the input year
    """
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if p_month == 2 and is_leap(p_year):
        return 29
    else:
        return month_days[p_month - 1]


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)












