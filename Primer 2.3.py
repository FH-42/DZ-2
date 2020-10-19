a = int(input())
count_natural_number = 0
for i in range(1, a + 1):
    if(a % i == 0):
        count_natural_number+=1
print("количество натуральных делителей ", count_natural_number)