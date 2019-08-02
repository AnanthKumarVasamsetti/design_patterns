"""
Chain of responsibility: In this structural pattern the processing of any given request is handled through a chain of handlers.
                         Request is passed across the chain of handlers until it is fulfilled.
Example : In following example there will be display of processors which would to take the responsibility of respective numbers
"""
import abc

class Chain:
    
    def __init__(self):
        return

    @abc.abstractclassmethod
    def set_next(self, nextInChain):
        pass
    
    @abc.abstractclassmethod
    def process(self, numberToProcess):
        pass

class NegativeProcessor(Chain):
    
    def __init__(self):
        return
    
    def set_next(self, nextInChain):
        self.nextInChain = nextInChain
    
    def process(self, numberToProcess):
        if numberToProcess < 0:
            print("Negative processor: ", numberToProcess)
        else:
            self.nextInChain.process(numberToProcess)

class PositiveProcessor(Chain):

    def __init__(self):
        return
    
    def set_next(self, nextInChain):
        self.nextInChain = nextInChain
    
    def process(self, numberToProcess):
        if numberToProcess > 0:
            print("Positive processor: ", numberToProcess)
        else:
            self.nextInChain.process(numberToProcess)

class ZeroProcessor(Chain):

    def __init__(self):
        return
    
    def set_next(self, nextInChain):
        self.nextInChain = nextInChain
    
    def process(self, numberToProcess):
        if numberToProcess == 0:
            print("Zero processor: ",numberToProcess)
        else:
            self.nextInChain.process(numberToProcess)


if __name__ == "__main__":
    
    c1 = NegativeProcessor()
    c2 = PositiveProcessor()
    c3 = ZeroProcessor()

    c1.set_next(c2)
    c2.set_next(c3)

    c1.process(90)
    c1.process(0)
    c1.process(-20)
    c1.process(50)