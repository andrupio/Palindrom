def palindrom(wyraz):
    return wyraz == wyraz[::-1]

print(palindrom('kajak'))
print(palindrom('potop'))
print(palindrom('pottop'))
print(palindrom('ppootop'))
print(palindrom('kaajjak'))