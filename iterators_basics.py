class Range:
    # Write your code here.
    """ emulates the range() function with the use of iterators """
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step
        #self.current = 0

    def __iter__(self):
        range_generator = RangeIterator(self.start, self.stop, self.step)
        return range_generator

class RangeIterator:
    def __init__(self, start,stop,step):
        self.current = start - step
        self.start = start
        self.stop = stop
        self.step = step

    def __next__(self):
        if (self.step >0 and (self.stop < self.start) ) or (self.step <0 and (self.stop > self.start)):
            raise StopIteration
        self.current += self.step
        if (self.current>=self.stop and self.stop>0) or (self.current<=self.stop and self.stop<0) or (self.current == self.stop):
            raise StopIteration
        else:  
            return self.current

r = Range(2,35,3)
for each in r:
    print(each)