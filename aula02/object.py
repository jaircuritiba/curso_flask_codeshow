class Animal:
    planeta = "Terra"

    def nascer(eu_mesmo): # o padrão de nomeação é "self"
        print(f"Oi, eu nasci no planeta {eu_mesmo.planeta}") 

    def comer(self):
        print("Estou comendo... crunch, crunch, crunch")

class Mamifero(Animal):
    def comer(self):
        print("Estou tomando leite...")

class Oviparos(Animal):
    def nascer(self):
        print("Acabei de quebrar o ovo no planeta {self.planeta}")

    