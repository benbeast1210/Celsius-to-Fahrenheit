from unittest import result


celsius = int(input())

def conv(c):
 result = ((9/5) * c) + 32 
 return result
 
fahrenheit = conv(celsius)

print(fahrenheit)