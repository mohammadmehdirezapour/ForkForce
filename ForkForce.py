# اگر این کامنت رو میبینی یعنی ریپازیتوری رو کلون کردی روی ادیتورت.
#  n حالا این زیر 👇🏻 یک تابع بنویس که یک عدد ورودی
#  بگیره و یک عملیات ریاضی به دلخواه روش انجام بده و مقدار نهایی رو برگردونه.
#MohammadmahdiRezapour
def A_B(n):
    if n >= 0:
        return n
    else:

        return n
    
#defined by Shokoohi
def power_of_three(n):
    return n**4


# Defined by Asle Falah
def power_if_prime(n):

    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    if count == 2:
        return n ** 2
    else:
        return n

# Defined by Mahdi Dolati Zadeh
def IsEven(Number):
    if Number % 2 == 0:
        return True
    else:
        return False

# Defined by Mahdi Safarzadeh
def exp(x):
    f = 1
    if x < 0:
        x = (-1) * x
        f = -1
    xs = 1
    nm = 1
    ex = 1
    for i in range(1, x * 18):
        xs *= x
        nm *= i
        ex += (xs / nm)
    if f == -1:
        ex = 1 / ex
    return ex


# defined by Abolfazl
def powerOfTwo(n):
    return 2**n


# defined by ali,kamalpour
def logarithm(n, base=10):
    if n <= 0:
        return None
    result = 0
    current = n
    while current >= base:
        current /= base
        result += 1
    return result



# Defined by ali ebrahimi
def absolute_value(n):
    if n >= 0:
        return n
    else:

        return n
    
#defined by Shokoohi
def power_of_three(n):
    return n**3



      
# defined by Ali Mirahmadi
def sin(x):
    n=10
    s = x
    for i in range(2, n+1):
        k = 2*i-1
        f = 1
        for j in range(1, k+1):
            f = f * j
        if i % 2 == 0:
            s = s-(x**k)/f
        else:
            s = s+(x**k)/f
        return s


# defined by seyed mehdi banaroie
def factoriel(n):
    s=1
    for i in range(1,n+1):
        s=s*i
    return s


# defiend by Ilia parkan

def power(a,n):
    a=a**n
    return a


#defined by alireza adl gostar

def is_odd(n):
    if n%2!=0:
        return n
    else:
        return n+1


# Defiend By <Ali Negintaj>
def lengh(x):
    tedad = 0
    for i in x:
        tedad+=1
    return tedad    


# Defined by Amir Ansari
def custom_math_operation(number):
    if number % 2 == 0:
        return number * 2
    else:
        return number * 3

    
#defined by MohammadHossein Homayunfar
def doubleplus(n):
    n=j(n*2)+2
    return n


    

    
# Defined by mohammad alipour
def trangle (a):
    if a%2==0:
        return a**2
    else:
        return round(a**(1/2))


#Defined By Emad Ahmadi
def fibonacci_sequence(n):
    if not isinstance(n, int):
        return "Error: Input must be an integer"
    if n <= 0:
        return "Error: Input must be a positive integer"
    
    fib_list = [0, 1] if n > 1 else [0] if n == 1 else []
    
    for i in range(2, n):
        next_fib = fib_list[i-1] + fib_list[i-2]
        fib_list.append(next_fib)
    
    sequence_sum = sum(fib_list)
    
    return f"Fibonacci sequence of {n} terms: {fib_list}, Sum: {sequence_sum}"
