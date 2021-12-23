"""
FAVORITO

def balance(left, right):
  left_count = left.count("!")*2 + left.count("?")*3
  right_count = right.count("!")*2 + right.count("?")*3

  if(left_count > right_count):
    return "Left"
  elif(right_count>left_count):
    return "Right"
  else:
    return "Balance"
"""


"""
https://www.codewars.com/kata/57fb44a12b53146fe1000136/train/python

Each exclamation mark weight is 2; Each question mark weight is 3. Put two string left and right to the balance, Are they balanced?

If the left side is more heavy, return "Left"; If the right side is more heavy, return "Right"; If they are balanced, return "Balance".

Examples
balance("!!","??") == "Right"
balance("!??","?!!") == "Left"
balance("!?!!","?!?") == "Left"
balance("!!???!????","??!!?!!!!!!!") == "Balance"
"""



def balance(left, right):
    
    weightLeft=0
    for element in left:
        if element=="!":
            weightLeft += 2
        else:
            weightLeft += 3
    weightRight= 0
    for element in right:
        if element=="!":
            weightRight += 2
        else:
            weightRight += 3
    totalBalanced= weightRight - weightLeft
    if totalBalanced >0:
        return "Right"
    elif totalBalanced<0:
        return "Left"
    else:
        return "Balance"



balance("!!","??") # "Right"
balance("!??","?!!") # "Left"
balance("!?!!","?!?") # "Left"
balance("!!???!????","??!!?!!!!!!!") # "Balance"