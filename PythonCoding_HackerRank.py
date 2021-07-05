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
#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
