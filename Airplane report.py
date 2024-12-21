class Flight:
    def __init__(self,flightnumber,takeofftime,landtime,destinition):
        self.flightnumber=flightnumber
        self.takeofftime=takeofftime
        self.landtime=landtime
        self.destinition=destinition
    def show(self):
        print(f"The flightnumber {self.flightnumber} has takeofftime is {self.takeofftime} and landtime is {self.landtime} is going to the destinition {self.destinition}")
        
Flight1=Flight(1264,"1:00","3:00","patna")
Flight1.show()