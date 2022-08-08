class Cow:
    def __init__(self, call):
        self.call = call

    def voice(self):
        print(f"Cow said:{Korova.call}")

class Bear:
    def __init__(self, call):
        self.call = call

    def voice(self):
        print(f"Bear said: {Mishka.call}")

class Cat:
    def __init__(self, call):
        self.call = call

    def voice(self):
        print(f"Cat said: {Koshka.call}")

class Dog:
    def __init__(self, call):
        self.call = call

    def voice(self):
        print(f"Dog said: {Sobaka.call}")

Sobaka = Dog("GAV GAV")
Koshka = Cat("MEEEOW")
Mishka = Bear("ROOOAAR")
Korova = Cow("MUU MUU")
Korova.voice()
Mishka.voice()
Koshka.voice()
Sobaka.voice()
