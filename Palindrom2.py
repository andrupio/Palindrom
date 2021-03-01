def palindrom(w):
    w = ''.join(c for c in w if c.isalnum())
    w = w.lower()
    print(w)
    z = len(w)
    for i in range(z - 1):
        if w[i] != w[z-1-i]:
            return False
    return True
print("Podaj tekst do sprawdzenia")
x = input()
print("Podany tekst " + ("jest " if(palindrom(x)) else "nie jest ") + "palindromem")