def storage(value):
    return value


a = 10
a2 = storage(10)

a = 2
a = storage(a2+a)

print(a, a2)