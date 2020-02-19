distance = float(input("Please enter your distance, km: "))
finish = float(input("Please enter your finish result, km: "))
count_days = 1
while distance < finish:
    distance = distance * 1.1
    count_days += 1
#    print("Дистанция: ", distance)
#    print("количество дней: ", count_days)
print(f"на {count_days}-й день спортсмен достиг результата ​—​ не менее {finish} км")
