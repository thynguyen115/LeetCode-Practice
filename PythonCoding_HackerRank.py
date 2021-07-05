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
  
if __name__ == '__main__':
  """ Problem 6: Print hash code of a tuple (t) of an input tuple of n integers separated by space """
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))
  
  """
   Problem 7: Given an input dictionary {"student_name" : [score1, score2, score3]}
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

