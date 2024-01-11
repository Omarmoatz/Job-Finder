import random

def genrate_code(length=8):
    num = '123456789QWERTYUIOPLKJHGFDSAZXCVBNM'
    code = ''.join(random.choice(num) for _ in range(length))
    return code