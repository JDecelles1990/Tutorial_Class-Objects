class Vehicule():
    def __init__(self, price, gas, color):
        self.price = price
        self.gas = gas
        self.color = color

    def fillUpTank(self):
        self.gas = 100

        def emptyTank(self):
            self.gas = 0

            def gasLeft(self):
                return self.gas

class Car(Vehicule):
    def __init__(self, price, gas, color):
        super().__init__(price, gas, color)
        self.speed = speed

    def beep(self):
        print('BEEEEEPPPP !!!!!')

class Truck(Vehicule):
    def __init__(self, price, gas, color, tires):
        super().__init__(price, gas, color)
        self.tires = tires

    def beep(self):
        print('HONK HONK !!!!!')


#(258-303) Class&Objects #3 .2