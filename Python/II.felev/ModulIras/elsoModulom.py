
#! python3 win10-amd64

''' elsoModulum.py - Az első önállóan készített modulom, aminek van 2 nyilvános függvénye'''


from typing import Counter


__counter = 0

def sum1(the_list):
    global __counter
    __counter+=1
    the_sum= 0
    for element in the_list:
        the_sum +=element
    return the_sum

def prod1(the_list):
    global __counter
    __counter+=1
    prod = 1
    for element in the_list:
        prod*=element
    return prod    

if __name__ == "_main__":
    print("I prefer to be a module, but i cant")
    my_list = [i+1 for i in range(5)]
    print(sum1(my_list) == 15)
    print(prod1(my_list)== 120)
