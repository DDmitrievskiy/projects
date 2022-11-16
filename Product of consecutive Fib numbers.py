#Дается число prod, нужно найти такие подряд идущие два числа в последовательности фибоначчи, которые при произведении дадут prod.


def productFib(prod):
    
    number = prod
    
    f_prev = 0

    f_last = 1


    fibonacci_list = [0, 1, ]

    while(f_prev * f_last < number):
        f_sum = f_prev + f_last
        f_prev = f_last
        f_last = f_sum
        fibonacci_list.append(f_last)

    if fibonacci_list[len(fibonacci_list)-1] * fibonacci_list [len(fibonacci_list)-2] == number:
        return [fibonacci_list [len(fibonacci_list)-2], fibonacci_list[len(fibonacci_list)-1], True]
    else:
        return [fibonacci_list [len(fibonacci_list)-2], fibonacci_list[len(fibonacci_list)-1], False]