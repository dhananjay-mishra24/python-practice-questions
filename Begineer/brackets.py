Question: Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.



Solution: 
class Solution:
    def isValid(self, s: str) -> bool:
        

        stack = []

        #Create pair of brackets
        pair_of_brackets = {')':'(','}':'{',']':'['}

        for char in s:

            #Check if the char is value of pair that is all opening brackets
            if char in pair_of_brackets.values():
                
                #Add them to stack
                stack.append(char)

            #Check if the char is key of pair that is char is closing brackets
            elif char in pair_of_brackets.keys():

                #If that is true check is stack empty or last element of stack is not equal to same as value of char
                if not stack or stack[-1] != pair_of_brackets[char]:
                    
                    #Return False if matched any one
                    return False

                #else pop last element of the stack
                stack.pop()

        return not stack
