def triangle(a, b, c): 
    return a + b > c and b + c > a and c + a > b 

def heron(a, b, c): 
    p = (a + b + c) / 2 
    return (p * (p - a) * (p - b) * (p - c)) ** 0.5 

def area_triangle(a, b, c): 
    if not triangle(a, b, c): 
        return None 
    return heron(a, b, c) 

print(area_triangle(1., 1., 2. ** .5))
