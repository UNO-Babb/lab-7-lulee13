import NumberTests

def main():
  total = 0
  for i in range(2, 2000000):
    if NumberTests.isPrime(i):
      total += i
  print(total)

  


if __name__ == '__main__':
  main()