def get_array(length,minValue,maxValue):
    if length == 0:
        yield []
    else:
        for i in range(minValue,maxValue + 1):
            for item in get_array(length-1,minValue,maxValue):
                yield [i] + item