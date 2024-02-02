def calc_pow(x,n):
    '''
    Exponential value calculation using Divide and Conquer technique
    :param x: number
    :param n: power
    :return: multiplication of x and n
    '''
    if(n == 0):
        return 1
    elif n % 2 == 0:
        return calc_pow(x,n/2) * calc_pow(x,n/2)
    else:
        return x * calc_pow(x,n-1)
x,n=12,5
exp_val = calc_pow(x,n)
print(f"{x} to the power of {n} = {exp_val}")