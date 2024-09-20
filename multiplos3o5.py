def solution(number):
    if number < 0:
        return 0
    suma = 0
    for num in range(1,number):
        if num % 3==0 or num % 5==0:
            suma+=num
    return suma
print(solution(15))