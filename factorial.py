import time
import psutil


print("Программа выводит расчетное время факторизации числа. Частота процессора ", psutil.cpu_freq().current, " Гц")
def factor(n):
    ans = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            ans.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        ans.append(n)
    return ans

for j in range(11):
    f = 10 ** (j*2+1) + 1
    start = time.time()
    fact = factor(f)
    size = len(fact)
    solve_time = time.time() - start
    print(f"{j+1}. Множители числа {f:30} в количестве {size} штук это {fact}")
    print(f"Расчетное время: {solve_time}")
    start = time.time()
    mul = 1
    for i in range(len(fact)):
        mul = mul * fact[i]
    solve_time = time.time() - start
    print(f"Время перемножения: {solve_time}")
print("Расчеты завершены")
