def new_range(start, stop, step):
    """ emulates the range() function with the use of generators """
    iteration = 0
    current = start
    while (not ( ((start<stop) and (step<0 or current>=stop)) or ((start>stop) and (step>0 or current<=stop)) )):
        yield current
        current += step
        iteration += 1
        

r = new_range(2,10,1)
for each in r:
    print(each)
