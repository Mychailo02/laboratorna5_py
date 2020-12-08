
n = int(input("Введіть значення n: "))
for c in range(1, n):
  for b in range (1 , c):
      for a in range (1, b):
          if a**2 + b**2 == c**2:
              print(a,b,c)
            
