import file_b # das ist ein absoluter import. Hier legst du den direkten Pfad zu dem Modul fest, das du importieren möchtest.

# Weiter möglichkeiten sind die bennen von Imports:
# import file_b as fb # Hier wird file_b als fb importiert. Du kannst dann fb verwenden, um auf die Funktionen und Klassen in file_b zuzugreifen.

Math = file_b # Hier kann ich sagen das Math die das Modul file_b ist.
    
    
    
# Es ist nützlich so viel wie möglich in Variabeln zu packen, um den Code leserlicher zu machen und skalierbar zu halten.
number1 = 3 
number2 = 5
result = Math.Add(number1, number2) # Hier wird die Funktion Add aus dem Modul file_b aufgerufen.

print (result)