
# While loop

# Laufen solange wie ein bestimmter Zustand erfüllt ist.

# Unendliche Schleife
count = 0
while True:

    count += 1
    print("Ich bin eine unendliche Schleife")
    if count == 5:
        break
# WICHTIG SETZT IMMER EIN BREAK SONST LÄUFT ES  BIS DER PC CRASHT

# Zähle von 1 bis 10

for i in range(1,11): #Hier wird von 1 bis 10 gezählt. Wieso 11? Weil der letzte Wert nicht mitgezählt wird.
    print(i) 
    
    