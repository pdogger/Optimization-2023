from math import sqrt


def f(x):
    return 2*pow(x,2)-7*x+1


def y(a, b):
    return a+(3-sqrt(5))/2*(b-a)


def z(a, b):
    return a+(sqrt(5)-1)/2*(b-a)


a = int(input("a="))
b = int(input("b="))

k = int(input("k="))

a_array = [a]*(k+1)
b_array = [b]*(k+1)
k_array = [1]*(k+1)
 
y_i = y(a_array[1], b_array[1])
z_i = z(a_array[1], b_array[1])
for i in range(1,k):
    f_y = f(y_i)
    f_z = f(z_i)
    print(f"\nk={i}\na{i}={a_array[i]}\nb{i}={b_array[i]}\ny{i}={y_i}\nz{i}={z_i}\nf(y{i})={f_y}\nf(z{i})={f_z}\n")
    if f_y <= f_z:
        a_array[i+1] = a_array[i]
        b_array[i+1] = z_i
        z_i = y_i
        y_i = y(a_array[i+1], b_array[i+1])
    else:
        a_array[i+1] = y_i
        b_array[i+1] = b_array[i]
        y_i = z_i
        z_i = z(a_array[i+1], b_array[i+1])
