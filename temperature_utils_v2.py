from typing import Iterable, Tuple


def convert_to_celsius(fahrenheit_temp: float) -> float:
    """
    Given a float representing a temperature in fahrenheit, return the corresponding value in celsius.

    :param fahrenheit_temp: A float representing a temperature in fahrenheit
    :return: A float representing the corresponding value of the fahrenheit_temp parameter in celsius
    """
    cel = round(((fahrenheit_temp-32)*5)/9,2)
    return cel


def convert_to_fahrenheit(celsius_temp: float) -> int:
    """
    Given a float representing a temperature in celsius, return the corresponding value in fahrenheit.

    :param celsius_temp: A float representing a temperature in celsius
    :return:  A float representing the corresponding value of the celsius_temp parameter in fahrenheit
    """
    fahr = round(((celsius_temp*9/5)+32),2)
    return fahr

def kelvin_to_celsius(celsius_temp: float) -> float:
    """
    Given a float representing a temperature in celsius returns the corresponding value in celsius
    """
    kelv = round(celsius_temp + 273.15,2)
    return kelv


def temperature_tuple(temperatures: Iterable, input_unit_of_measurement: str) -> Tuple[Tuple[float, float]]:
    """
    Given a tuple or a list of temperatures, this function returns a tuple of tuples.
    Each tuple contains two values. The first is the value of the temperatures parameter. The second is the the value of
    the first converted to the unit of measurement specified in the input_unit_of_measurement parameter.

    :param temperatures: An iterable containing temperatures
    :param input_unit_of_measurement: The unit a measure to use to convert the values in the temperatures parameter
    :return: A tuple of tuples
    """
    lst = []
    if input_unit_of_measurement == "c":
        for i in temperatures:
            x = convert_to_fahrenheit(i)
            y = kelvin_to_celsius(i)
            lst.append((i,x,y))
    elif input_unit_of_measurement == "f":
        for i in temperatures:
            x = convert_to_celsius(i)
            y = kelvin_to_celsius(x)
            lst.append((i,x,y))
    elif input_unit_of_measurement =="k":
        for i in temperatures:
            cel_from_k = i - 273.15
            fahr_from_k = convert_to_fahrenheit(cel_from_k)
            x= round(cel_from_k,2)
            y= round(fahr_from_k)
            lst.append((i, x, y)) 
    else:
        lst = ()  
    
    finallst=tuple(lst)
    return finallst
