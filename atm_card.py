class ATMCard:
    def __init__(self, defaultPin = 1234, defaultBalance = 10000):
        self.defaultPin = defaultPin
        self.defaultBalance = defaultBalance

    def cekPinAwal(self):
        return self.defaultPin
    def cekSaldoAwal(self):
        return self.defaultBalance
    
