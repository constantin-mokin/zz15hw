#сложно понять и условие и как выполнить..
#даже представить не могу в голове шаги решения и ход выполнения простыми словами
#не говоря уже как описать через команды..

def get_divisors_sum(num):
    divisors_sum = 0
    for divisor in range(1, num):
        if num % divisor == 0:
            divisors_sum += divisor
    return divisors_sum

number_list = []
for num in range(200, 300 + 1):
    if num not in number_list:
        divisors_sum = get_divisors_sum(num)
        if 200 < divisors_sum < 300 and != divisors_sum and num == get_divisors_sum(divisors_sum):
            number_list.append(divisors_sum)
            print(num, divisors_sum)