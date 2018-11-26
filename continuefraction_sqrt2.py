from random import randint
'''
sqrt(2) = 1 + 1 / (1 + sqrt(2))
sqrt(n) = a + (n - a ** 2) / (a + sqrt(n)) for what ever a
'''
a = str(randint(1, 5))
n = '10000' # any number to be starter value
mmsqrt = randint(1, 5)
stsqrt = str(mmsqrt)
for _ in range(100):
  print(_, mmsqrt)
  stsqrt = f'{a} + ({n} - {a} ** 2) / ({a} + {mmsqrt})'
  mmsqrt = eval(stsqrt)
