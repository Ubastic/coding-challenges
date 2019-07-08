def multiTable(number):
    return "\n".join("{} * {} = {}".format(i,number,i * number) for i in range(1,11))