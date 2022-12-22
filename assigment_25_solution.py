'''Question1
Create a function that takes three integer arguments (a, b, c) and returns the amount of integers which are of equal value.
Examples
equal(3, 4, 3) ➞ 2

equal(1, 1, 1) ➞ 3

equal(3, 4, 1) ➞ 0 
Notes
Your function must return 0, 2 or 3.'''

def equal(a=int,b=int,c=int):
    if a/b == 1 and a/c == 1:
        return 3
    elif a/b == 1 or b/c == 1 or a/c==1:
        return 2
    else:
        return 0

print(equal(3,4,3), equal(1,1,1),equal(3,4,1))

'''
Question2
Write a function that converts a dictionary into a list of keys-values tuples.
Examples
dict_to_list({
  "D": 1,
  "B": 2,
  "C": 3
}) ➞ [("B", 2), ("C", 3), ("D", 1)]

dict_to_list({
  "likes": 2,
  "dislikes": 3,
  "followers": 10
}) ➞ [("dislikes", 3), ("followers", 10), ("likes", 2)]
Notes
Return the elements in the list in alphabetical order.'''

def dict_to_list(d=dict):
    resp = d.items()
    return sorted(resp, key= lambda i:i[0])

d1 = {
  "D": 1,
  "B": 2,
  "C": 3
}
d2 = {
  "likes": 2,
  "dislikes": 3,
  "followers": 10
}
print(dict_to_list(d1), dict_to_list(d2))
'''
Question3
Write a function that creates a dictionary with each (key, value) pair being the (lower case, upper case) versions of a letter, respectively.
Examples
mapping(["p", "s"]) ➞ { "p": "P", "s": "S" }

mapping(["a", "b", "c"]) ➞ { "a": "A", "b": "B", "c": "C" }

mapping(["a", "v", "y", "z"]) ➞ { "a": "A", "v": "V", "y": "Y", "z": "Z" }
Notes
All of the letters in the input list will always be lowercase.
'''
def mapping(input=list):
  try:
    resp_dict = {input[i]:(input[i]).upper() for i in range(len(input))}
  except Exception as e:
    resp_dict ={'Error':e}
  return resp_dict

print(mapping(["p","s"]),mapping(["a", "b", "c"]), mapping(1))

'''
Question4
Write a function, that replaces all vowels in a string with a specified vowel.
Examples
vow_replace("apples and bananas", "u") ➞ "upplus und bununus"

vow_replace("cheese casserole", "o") ➞ "chooso cossorolo"

vow_replace("stuffed jalapeno poppers", "e") ➞ "steffed jelepene peppers"
Notes
All words will be lowercase. Y is not considered a vowel.'''

def vow_replace(string=str, toBeReplaceWith=str):
  vowel = ['a','e','i','o','u']
  for i in string:
    if i in vowel:
      rtn=string.replace(i,toBeReplaceWith)
  return rtn

print(vow_replace("apples and bananas", "u"),vow_replace("cheese casserole", "o"))

'''
Question5
Create a function that takes a string as input and capitalizes a letter if its ASCII code is even and returns its lower case version if its ASCII code is odd.
Examples
ascii_capitalize("to be or not to be!") ➞ "To Be oR NoT To Be!"

ascii_capitalize("THE LITTLE MERMAID") ➞ "THe LiTTLe meRmaiD"

ascii_capitalize("Oh what a beautiful morning.") ➞ "oH wHaT a BeauTiFuL moRNiNg."
'''

def ascii_capitalize(string=str):
  str_list =set([i for i in string])
  for i in str_list:
    if ord(i)%2 == 0:
      string = string.replace(i, i.upper())
    else:
      string = string.replace(i, i.lower())
  return string

print(ascii_capitalize("to be or not to be!"),ascii_capitalize("THE LITTLE MERMAID"),ascii_capitalize("Oh what a beautiful morning."))