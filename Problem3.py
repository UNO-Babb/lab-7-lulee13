from NumberTests import isPrime
from NumberTests import getFactors

def main():
  n = 13195
  factors = getFactors(n)

  for f in factors:
    if isPrime(f):
      print(f)  



if __name__ == '__main__':
  main()