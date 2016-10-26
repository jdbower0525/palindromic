import re
user_input = ''

def string_cleaner(user_input):
     no_punc = re.sub(r'\W+', '', user_input)
     clean_string = no_punc.lower()
     return clean_string

def is_palindrome(user_input):
    palindrome = string_cleaner(user_input)
    if palindrome == palindrome[::-1]:
        return True
    else:
        return False

def main():
    user_input = input("Enter a suspected palindrome: ")
    print(is_palindrome(user_input))

if __name__ == "__main__":
    main()
