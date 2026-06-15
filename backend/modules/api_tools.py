import random 

def make_captcha():
    """
    This function creates a capcha challenge.
    Returns an object representing the mathematical expression
    and also returns the result.
    """
    x = random.randint(1, 9)
    y = random.randint(1, 9)
    sign_list = ['-','+','*']
    sign = random.choice(sign_list)
    cAPTCHA = None
    if sign == '+':
        cAPTCHA = x + y
    if sign == '-':
        cAPTCHA = x - y
    if sign == '*':
        cAPTCHA = x * y

    data = {
        'x': x,
        'y': y,
        'sign' : sign
    }
    return data, cAPTCHA