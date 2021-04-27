# Aufgabe 1:

# Schreibe ein Python-Programm, das

# 1) Den Nutzer grüßt

# 2) eine erste Zahl entgegen nimmt

# 3) eine zweite Zahl entgegen nimmt

# 4) die Summe der beiden Zahlen berechnet und ausgibt

# 5) die Differenz der kleineren von der größeren Zahl berechnet und ausgibt (kleinere Zahl von großen abziehen)

# 6) das Produkt der beiden Zahlen berechnet und ausgibt

# 7) den Quotienten kleinerer Zahl durch größere Zahl berechnet und ausgibt (inkl. Nachkommastellen)


Name = input("Geben Sie Ihren Namen ein:")

print("Hallo", Name)
Zahl1_String = input("Erste Zahl eingeben:")
Zahl1 = int(Zahl1_String) 
Zahl2 = float(input("Zweite Zahl eingeben:"))

Summe = Zahl1 + Zahl2

print("Die Summe Ihrer Zahlen ergibt:",Summe )


if Zahl2 < Zahl1: 

    Differenz = Zahl1 - Zahl2

    print("Die Differenz Ihrer Zahlen ergibt:", Differenz )
    

elif Zahl1 < Zahl2:

    Differenz = Zahl2 - Zahl1
    print("Die Differenz Ihrer Zahlen ergibt:", Differenz )

elif Zahl1 == Zahl2:

    Differenz = Zahl1 - Zahl2
    print("Die Differenz Ihrer Zahlen ergibt:", Differenz )



Produkt = Zahl1 * Zahl2

print("Das Produkt Ihrer Zahlen ergibt:", Produkt )


if Zahl2 < Zahl1:

    Quotient = Zahl2 / Zahl1
   

elif Zahl1 < Zahl2:

    Quotient = Zahl1 / Zahl2

else:

    Quotient = Zahl1 / Zahl2

print("Der Quotient Ihrer Zahlen ergibt:", Quotient )



