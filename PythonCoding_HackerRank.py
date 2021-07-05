""" Problem 1: Swap Case 
    Ex: s = "heLLo" ==> output = "HEllO"
"""
def swap_case(s):
    returned_str = ""
    for char in s:
        if char.isalpha():
            if char.isupper():
                returned_str += char.lower()
            else:
                returned_str += char.upper()
        else:
            returned_str += char    
    return returned_str

""" Problem 2: Using hyphen (-) to connect all words
    in a given string that is separated by spaces 
    Ex: line = "hello I am Thy" --> output = "hello-I-am-Thy"
"""
def split_and_join(line):
    returned = ''
    for elem in line:
        if elem == ' ':
            returned += '-'
        else:
            returned += elem
    return returned

""" Problem 3: Print string as this following format:
               "Hello FirstName LastName! You just delved into python."
"""
def print_full_name(first, last):
    strs = 'Hello ' + first + ' ' + last + '! You just delved into python.'
    print(strs)

""" Problem 4: Replace the character at a give position by a new character 
    Ex: string = "hello", position = 3, character = 'L'
        output = "helLo"
"""
def mutate_string(string, position, character):
    string = string[:position] + character + string[position+1:]
    return string

""" Problem 5: Count how many times sub_string appears in string 
    Ex: "ABCDCDC" ==> "CDC" appears twice
    Thinking of recursive function...
"""
def count_substring(string, sub_string):
    if len(string) < len(sub_string):
        return 0
    if sub_string in string[0:len(sub_string)]:
        return 1 + count_substring(string[1:], sub_string)
    else:
        return count_substring(string[1:], sub_string)
 
""" Problem 6: Use built-in textwrap to separate a string
               into smaller string of length max_width 
    Example: input = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
             max_width = 4
             output = 
                        "ABCD
                         EFGH
                         IJKL
                         IMNO
                         QRST
                         UVWX
                         YZ"
"""
# import textwrap
def wrap(string, max_width):
    wrapper = textwrap.TextWrapper(width=max_width)
    word_list = wrapper.wrap(text=string)
    output = ""
    # Connect each line
    for elem in word_list:
        output += elem + "\n"
    # Remove '\n' at the end of output
    return output[:-1]

""" Problem 7: Given an integer (n), print its values: 
               (1) decimal, (2) octal, (3) hexa (capitalized), (4) binary
               Format of output is all about spacing:
               Ex: n = 17
                1     1     1     1
                2     2     2    10
                3     3     3    11
                4     4     4   100
                5     5     5   101
                6     6     6   110
                7     7     7   111
                8    10     8  1000
                9    11     9  1001
               10    12     A  1010
               11    13     B  1011
               12    14     C  1100
               13    15     D  1101
               14    16     E  1110
               15    17     F  1111
               16    20    10 10000
               17    21    11 10001
"""
def print_formatted(number):
    lst = []
    out_lst = []
    # find dec, oct, hex, bin of those numbers
    for i in range(1, number+1):
        s = str(i) + " " + oct(i)[2:] + " " + hex(i)[2:].upper() + " " + bin(i)[2:]
        lst.append(s)
    # spacing
    max_width = len(lst[-1].split()[-1]) + 1  # len(last elem of last string in lst) + 1
    for elem in lst:
        elems = elem.split() # split values of each row
        str_lst = [" " * (max_width - len(elems[i])) + elems[i] if i > 0 else " " * (max_width - len(elems[i]) - 1) + elems[i] for i in range(0,len(elems))] # reformat the string
        out_lst += ["".join(str_lst)]
    return print("\n".join(out_lst))

if __name__ == '__main__':
  """ Problem 7: Print hash code of a tuple (t) of an input tuple of n integers separated by space """
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))
  
  """
   Problem 8: Given an input dictionary {"student_name" : [score1, score2, score3]}
   Print average scores of a student (note: give 2 decimal places)) 
  """
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    stu_scores = student_marks[query_name]
    avg = sum(stu_scores) / len(stu_scores)
    print("{:0.2f}".format(avg))

 """ Problem 9: check if 5 conditions satisfy 
     Condition 1: string has at least an alphanumeric character
     Condition 2: string has at least an alphabetical character
     Condition 3: string has any digits
     Condition 4: string has lowercase character(s)
     Condition 5: string has uppercase character(s)
 """
    s = input()
    lst = [False, False, False, False, False]
    for char in s:
        if char.isalnum():
            lst[0] = True
        if char.isalpha():
            lst[1] = True
        if char.isdigit():
            lst[2] = True
        if char.islower():
            lst[3] = True
        if char.isupper():
            lst[4] = True
     for i in range(5):
        print(lst[i])

""" Problem 10: print logo of HackerRank 
    H    
   HHH   
  HHHHH  
 HHHHHHH 
HHHHHHHHH
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHHHHHHHHHHHHHHHHHHHHHH   
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
  HHHHH               HHHHH             
                    HHHHHHHHH 
                     HHHHHHH  
                      HHHHH   
                       HHH    
                        H 
"""
# Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

# Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

# Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

# Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

# Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

# Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
    
""" Problem 11: Print a Door Mat (N x 3N) 
    Ex: 7 x 21
    ---------.|.---------
    ------.|..|..|.------
    ---.|..|..|..|..|.---
    -------WELCOME-------
    ---.|..|..|..|..|.---
    ------.|..|..|.------
    ---------.|.---------
"""
inp = input()
row = int(inp.split()[0])
col = int(inp.split()[1])
# those 3 lines ^^^ can be replaced by >>> n, m = map(int, input().split()) [credit: ursan]

mid_pattern = ".|."
mat = []
# First-half pattern
for i in range(row//2):    
    mat.append(mid_pattern.center(col, '-'))
    mid_pattern = ".|." + mid_pattern + ".|."
# those lines ^^^ can be replaced by >>> pattern = [('.|.'*(2*i + 1)).center(m, '-') for i in range(n//2)]
# [credit: ursan]

count = 1
for i in range(row):
    # mid row
    if i == (row - 1) / 2:
        print("WELCOME".center(col, '-'))
    elif i < (row-1)/2:
        print(mat[i]) # first-half
    else:
        print(mat[len(mat) - count]) # second-half
        count += 1
# ^^^ >>> print('\n'.join(pattern + ['WELCOME'.center(m, '-')] + pattern[::-1])) [credit: ursan]
        
