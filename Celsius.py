

class Celsius:
    def __init__(self,value = 26.0):
        self.value = float(value)

    def __get__(self, instance, owner):
        return  self.value

    def __set__(self, instance, value):
        self.value = float(value)

class Frenhait:
    def __get__(self, instance, owner):
      return  instance.cel *1.8 +32

    def __set__(self, instance, value):
        instance.cel = (float(value) - 32) / 1.8



class Tempertor:
    cel = Celsius()
    fel = Frenhait()

test = Tempertor()

print(test.cel)

test.cel = 30

print(test.fel)

test.fel = 100

print(test.cel)