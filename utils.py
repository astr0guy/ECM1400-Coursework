def sumvalues(values:list):
    """This function adds all of the values in a list or array of numbers called values together into one variable called sum, then returns it.
    If one of the encountered values is non-numerical, an exception will be thrown, and a string describing the situation will be returned."""
    try:
        sum = 0
        for i in range (len(values)):
            sum = sum + values[i]
        return sum
    except TypeError:
        return "A non-numereical value has been encountered, and the sum of the list could not be found"

def maxvalues(values:list):
    """This function sets a variable called max to the first variable in a list or array called values.
    It then checks every value in values and checks if its value is more than that of max.
    If it is, max is replaced by this value.
    If one of the encountered values is non-numerical, an exception will be thrown, and a string describing the situation will be returned.
    Once the all of values has been checked, the counter is returned."""
    try:
        max = values[0]
        for i in range (len(values)):
             if values[i] > max:
                max = values[i]
        return max
    except TypeError:
        return "A non-numereical value has been encountered, and the sum of the list could not be found"

def minvalues(values:list):
    """This function sets a variable called min to the first variable in a list or array called values.
    It then checks every value in values and checks if its value is less than that of min.
    If it is, min is replaced by this value.
    If one of the encountered values is non-numerical, an exception will be thrown, and a string describing the situation will be returned.
    Once the all of values has been checked, the counter is returned."""
    try:
        min = values[0]
        for i in range (len(values)):
             if values[i] < min:
                min = values[i]
        return min
    except TypeError:
        return "A non-numerical value has been encountered, and the sum of the list could not be found"

def meannvalues(values:list):
    """This function checks every value in a list or array and checks if it's equal to the a particular value.
    If it is, a counter increments from zero. 
    If one of the encountered values is non-numerical, an exception will be thrown, and a string describing the situation will be returned.
    Once the entire list or array has been checked, the counter is returned."""
    try:
        sum = 0.0
        for i in range (0, len(values)):
            sum = sum + values[i]
        if len(values) > 0:
            return (sum / len(values))
        else:
            return "No data"
    except TypeError:
        return "A non-numerical value has been encountered, and the sum of the list could not be found"

def countvalues(values:list, xw):
    """This function checks every value in a list or array called values and checks if it's equal to a particular value stored by a variable called xw.
    If it is, a counter called increments from zero. 
    Once the entire list or array has been checked, xw is returned."""
    xcount = 0
    for i in range (len(values)):
        if values[i] == xw:
            xcount += 1
    return xcount


