def polynomial_py(a, x):
    result = 0
    for n, a_n in enumerate(a):
        x_power_n = 1
        for i in range (n):
            x_power_n *= x
        result += a_n * x_power_n
    return result

a = [1,2,0,3]
x = 1.5
print(polynomial_py(a,x))