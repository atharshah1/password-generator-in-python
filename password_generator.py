# strong password generator


# Importing random to generate
# random string sequence
import random
# Importing string library function
import string


def random_pass(size):

    # Takes random choices from
    # ascii_letters and digits
    symbols = "*&$#@!()[]"
    letters = string.ascii_letters + string.digits

    # Takes random choices from ascii_letters and digits and
    #  add a random symbol
    generated_pass = ''.join([random.choice(letters)
                             for i in range(size-1)])+random.choice(symbols)
    return generated_pass


password = random_pass(10)
print(password)
