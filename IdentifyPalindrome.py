#Identify a palindrome
#Write a function if a given string is a palindrome
#Input string
#output bool
import re

def solution(N):
    forwards = ''.join(re.findall(r'[a-z]+',N.lower()))
    backwards = forwards[::-1]
    print (forwards == backwards)
#JAva https://www.baeldung.com/java-palindrome
#Backward iteration https://www.geeksforgeeks.org/backward-iteration-in-python/

def main():
    solution("Hello World") #F
    solution("Level") #T
    solution("Go hang a salami - I'm a lasagna hog")


if __name__ == "__main__":
    main()