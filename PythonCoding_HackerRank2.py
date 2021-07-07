""" Problem: Output the cube of fibonacci numbers 
    Ex: n = 5 (input) 
    if __name__ == '__main__':
        n = int(input())
        print(list(map(cube, fibonacci(n))))
==> print [0, 1, 1, 8, 27] b.c the first 5 fibonacci numbers are [0, 1, 1, 2, 3]
"""
cube = lambda x: x*x*x# complete the lambda function 
 
def fibonacci(n):
    if n == 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return  [0, 1]
    if n > 2:
        lst = [0, 1]
        for i in range(n-2):
            lst += [lst[-1]+lst[-2]]
        return lst
      
""" Problem: Print the number of non-repeated elems
    Ex: 7
        UK
        China
        USA
        France
        New Zealand
        UK
        France 
"""
def print_non_repeated():
  inp = int(input())
  lst = []
  for i in range(inp):
      lst += [input()]
  print(len(set(lst)))
