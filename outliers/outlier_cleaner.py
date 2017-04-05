#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    square_errors = (net_worths - predictions)**2
    cleaned_data = zip(ages, net_worths, square_errors) 
    cleaned_data.sort(key=lambda datum: datum[2][0])
    length = int(len(predictions) * 0.9)
    return cleaned_data[:length]

