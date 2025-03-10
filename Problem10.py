"""Find the sum of all the primes below two million."""

from NumberTests import isPrime

def main():
  total = 0 #sum of prime numbers
  for i in range(2000000): #testing each value for primeness
    if isPrime(i):
      total+=i #calculating sum
      
  print(total) #prints sum

  


if __name__ == '__main__':
  main()