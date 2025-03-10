"""What is the 10001st prime number?"""

from NumberTests import isPrime

def main():
  n = 0 #number of prime numbers found
  i = 0 #value being tested for being prime
  while n < 1001: #counts number of prime numbers found
    if isPrime(i):
      print(i)
      i+=1
      n+=1
    else:
        i+=1
  print(i) #prints 10001st prime number

  


if __name__ == '__main__':
  main()