# Beliebtes Programmierproblem 

# Regeln:
# - Zahlen von 1 bis 100 ausgeben
# - Bei Vielfachen von 3 "Fizz" ausgeben
# - Bei Vielfachen von 5 "Buzz" ausgeben
# - Bei Vielfachen von 3 und 5 "FizzBuzz" ausgeben
# - Sonst die Zahl selbst ausgeben

# Anforderung: 
# - Schreibe eine Funktion, die die oben genannten Regeln implementiert
# - Die Funktion soll skalierbar und erweiterbar sein


def fizz_buzz(n): 
    """Gibt die FizzBuzz """
    
    keys = {
        3: "Fizz",
        5: "Buzz",
    }
    
    for i in range(1, n + 1):
        output = ""
        for key, value in keys.items():
            if i % key == 0:
                output += value
        if not output:
            output = str(i)
        print(output)   
        
# Test der Funktion
if __name__ == "__main__": # Wird nur ausgeführt, wenn die Datei direkt aufgerufen wird und nicht beim Import
    fizz_buzz(100)
    
    
# Breakdown 
# def fizz_buzz(n): # n dient als Parameter für die Anzahl der zu druckenden Zahlen
#     """Gibt die FizzBuzz """
    
#     keys = { # Hier definiere ich welche vielfachen ich ersetzten möchte
#         3: "Fizz",
#         5: "Buzz",
#     }
    
#     for i in range(1, n + 1): # Das ist ein for loop. Siehe loop.py. 
#         output = "" # Hier speichere ich den Output. Aktuell ist er ein leerer String.
#         for key, value in keys.items(): #für jede Zahl loope ich einmal über die keys
#             if i % key == 0: # Hier prüfe ich ob die Zahl i restlos durch die Zahl key teilbar ist.
#                 # Wenn ja, das gebe ich den Wert des keys aus und füge ihn zu Output hinzu.
#                 output += value
#         if not output: # Wenn der Output immernoch leer ist, dann gabs keine restlose Teilung und ich kann die Zahl i ausgeben.
#             output = str(i) # str(i) wandelt die Zahl i, die ein Integer ist in einen String um.
#         print(output)   # Printe den Output