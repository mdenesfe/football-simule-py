import random
import time

def get_form_factor():
    return random.uniform(0, 1)


def get_age_factor(age):
    age = int(age)
    age_factors = [1, 0.9, 0.8, 0.7]
    if age < 25:
        return age_factors[0]
    elif age < 30:
        return age_factors[1]
    elif age < 35:
        return age_factors[2]
    else:
        return age_factors[3]
