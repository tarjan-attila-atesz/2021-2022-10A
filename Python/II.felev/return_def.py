def happy_new_year(wishes=True):
    print("Three...")
    print("Two...")
    print("One...")
    if not wishes:
        return

    print("Happy New Year!")


happy_new_year()


def boring_function():
    return 123


x = boring_function()

print("The boring_function has returned its result. It's:", x)


def liters_100km_to_miles_gallon(liters):
    convert_one_litre_to_gallon = 1 / 3.785411784
    total_gallon = convert_one_litre_to_gallon * liters
    convert_hundred_km_to_mile = 100/1.609344
    total_miles = convert_hundred_km_to_mile / total_gallon
    return total_miles


def miles_gallon_to_liters_100km(miles):
    convert_one_mile_to_km = 1.609344
    convert_total_miles_to_Km = miles * convert_one_mile_to_km
    one_gallon_to_liters = 3.785411784
    total_liters_in_hundred_Km = 100 * one_gallon_to_liters / convert_total_miles_to_Km
    return total_liters_in_hundred_Km


print(liters_100km_to_miles_gallon(3.9))
print(liters_100km_to_miles_gallon(7.5))
print(liters_100km_to_miles_gallon(10.))
print(miles_gallon_to_liters_100km(60.3))
print(miles_gallon_to_liters_100km(31.4))
print(miles_gallon_to_liters_100km(23.5))


def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b


def is_a_right_triangle(a, b, c):
    if not is_a_triangle(a, b, c):
        return False
    if c > a and c > b:
        return c ** 2 == a ** 2 + b ** 2
    if a > b and a > c:
        return a ** 2 == b ** 2 + c ** 2


print(is_a_right_triangle(5, 3, 4))
print(is_a_right_triangle(1, 3, 4))
