import random
import string

def random_string(length=8):
  return ''.join(random.choice(string.ascii_lowercase) for n in range(length))
