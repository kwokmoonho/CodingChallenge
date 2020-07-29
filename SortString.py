#Sort a String
#ignore case when sorting : The as the
# words in the output string should have same case as input

def solution(N):
    words = N.split()
    words = [w.lower() + w for w in words]
    words.sort()
    words = [w[len(2)//2:] for w in words]
    print(' '.join(words))
def main():
    solution("string of words")
    solution("banana ORANGE apple") #apple banana ORANGE


if __name__ == "__main__":
    main()