datenliste = ["Hans", "Flo", "Elke", "Sonja", "Kai"]
print(dir(datenliste))
""" durch dir() sehen wir die verfügbaren Methoden. Listen sind Objekte"""

print(datenliste)
print(datenliste.pop())
""" methode pop() wirft letztes element aus der liste"""
print(datenliste)


class Jogger(list):
    """klasse für das verwalten von gelaufenen zeiten,
     die klasse jogger wird durch (list) ein kindelement von list, wodurch
     neben zeiterfassen() alle methoden von list zur verfügung stehen."""

    def __init__(self, altersklasse, zeit=[]):
        self.altersklasse = altersklasse
        self.gelaufene_zeiten = zeit

    def zeiterfassen(self, zeiten):
        self.gelaufene_zeiten += zeiten


Laeufer_Hans = Jogger("M40")
Laeufer_Hans.zeiterfassen(["2:30"])
Laeufer_Hans.zeiterfassen(["2:40", "3:00"])

print()
print("vor pop:")
print(Laeufer_Hans.gelaufene_zeiten)
print("pop:")
print(Laeufer_Hans.gelaufene_zeiten.pop())
print("nach pop:")
print(Laeufer_Hans.gelaufene_zeiten)
