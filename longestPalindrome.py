"""
https://www.codewars.com/kata/54bb6f887e5a80180900046b/train/python

Longest Palindrome
Find the length of the longest substring in the given string s that is the same in reverse.

As an example, if the input was “I like racecars that go fast”, the substring (racecar) length would be 7.

If the length of the input string is 0, the return value must be 0.

Example:
"a" -> 1 
"aab" -> 2  
"abcde" -> 1
"zzbaabcd" -> 4
"" -> 0
"""

def longest_palindrome (s):
        odd = 1
        while search(s,odd):
                odd += 2
        odd -= 2
        even = 2
        while search(s,even):
                even += 2
        even -= 2
        return max(odd,even)
        
def search (s,l):
        for x in range(0,len(s)-l+1):
                sub = s[x:x+l]
                if sub == sub[::-1]:
                        return True
        return False
print(longest_palindrome("baablkj12345432133d"))