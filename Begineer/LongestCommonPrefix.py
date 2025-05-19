Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.



Solution - 
  class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if len(strs)==0:
            return ""
        
        #We need to find the shortest array
        min_length = min([len(x) for x in strs])

        #Looping over shortest array
        for index in range(min_length):
            
            #Getting the word to be checked
            word_to_check = strs[0][index]

            for word in strs[1:]: #Looping over all the elements except the first one
                if word_to_check != word[index]:
                    return strs[0][:index]

        return strs[0][:min_length]
