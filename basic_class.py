

class Person:
    """A simple class to represent a person."""
    
    
    def __init__(self, name: str, age:int) -> None:  #In den Klammern stehen die Parameter, die der Konstruktor erwartet. "-> Type" ist der Rückgabetyp der Methode (gute um Sicherheit und leserlichkeit zu erhöhen). 
            """Initialize the person with a name and age."""
            self.name = name # self ist eine Referenz auf das aktuelle Objekt, das die Methode aufruft.
            self.age = age  # self.name und self.age sind Properties (Variabelen) der Klasse Person.
            
            
    def greet(self) -> str:
        """Return a greeting message."""
        return f"Hello, my name is {self.name} and I am {self.age} years old." # mit f vor dem String kann man Variablen in den String einfügen.
    # f-Strings sind eine einfache und lesbare Möglichkeit, Strings zu formatieren.
    
    
    def have_birthday(self) -> None:
        """Increment the person's age by 1."""
        self.age += 1
        # self.age = self.age + 1 ist die gleiche wie self.age += 1
        
        
Thomas = Person("Thomas", 30) # Instanz der Klasse Person erstellen. Thomas ist ein Objekt der Klasse Person. Du musst die Klasse immer erst instanziieren, bevor du sie verwenden kannst.
print(Thomas.greet()) # Thomas ist ein Objekt der Klasse Person. Du kannst die Methode greet() aufrufen, um eine Begrüßung auszugeben.
Thomas.have_birthday() # Thomas hat Geburtstag.

Michael = Person("Michael", 25) # Das ist eine Neue instanz der Klasse Person. Michael ist ein Objekt der Klasse Person. Du musst die Klasse immer erst instanziieren, bevor du sie verwenden kannst.
print(Michael.greet()) # Michael ist ein Objekt der Klasse Person. Du kannst die Methode greet() aufrufen, um eine Begrüßung auszugeben.
Michael.have_birthday() # Michael hat Geburtstag.


if Michael == Thomas: # In den Variablen sind die Klassen instanzen gespeichert
    print("Michael and Thomas are the same person.")
else:
    print("Michael and Thomas are different people.")
