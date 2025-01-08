def month_to_season(month):
    if month in [3, 4, 5]:
       return "Весна"
    if month in [6, 7, 8]:
        return "Лето"
    if month in [9, 10, 11]:
        return "Осень"
    
if __name__ == "__main__":
    month = int(input("Введите номер месяца (1 -12): "))
    season = month_to_season(month)
    print ( f"месяц{month} относится к сезону: {season}")