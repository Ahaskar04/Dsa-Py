#Ask for total number of days -> Take max temp of all days -> Find how many days above the avg temp

temp_list = []
total = 0
days = input("Enter the total number of days: ")
for i in range(0, int(days)):
    temp = input("Enter the temperature: ")
    temp_list.append(float(temp))
avg_temp = sum(temp_list) / len(temp_list)
for i in temp_list:
    if i > avg_temp:
        total += 1
print("Number of days above average temperature: ", total)