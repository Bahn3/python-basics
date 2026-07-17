def is_palindrome(word):
    left = 0
    right = len(word)-1

    while left < right:
        if word[left] != word[right]:
            return False
        left = left + 1
        right = right - 1

    return True

def main():
    user_word = input("Type a word: ")
    result = is_palindrome(user_word)
    print(result)
main()
        
