import random

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789' # symbols to be used
length = 16 # desired password length
alpha = 2   # number of alphabetic characters that should be in the generated password
digit = 2   # number of digits that should be in the password
upper = 1   # number of uppercase characters that should be in the password

def check_psw(psw):
    a = 0
    d = 0
    u = 0

    for c in psw:
        if c >= 'a' and c <= 'z':
            a += 1
        elif c >= 'A' and c <= 'Z':
            a += 1
            u += 1
        elif c >= '0' and c <= '9':
            d += 1

    return a >= alpha and d >= digit and u >= upper

def gen_psw():
    correct = False

    while not correct:
        psw = list(alphabet)
        random.shuffle(psw)     # don't know if shuffle is "secure enough" for you, feel free to use any alternatives
        psw = ''.join(psw)
        psw = psw[:length]

        correct = check_psw(psw)

    return psw

def main():
    print('Here is your new password:', gen_psw())

if __name__ == '__main__':
    main()
