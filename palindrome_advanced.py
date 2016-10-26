import re
user_input = ''

def string_cleaner(user_input):
     no_punc = re.sub(r'\W+', '', user_input)
     clean_string = no_punc.lower()
     return clean_string

def is_palindrome(user_input):
    palindrome = string_cleaner(user_input)
    if palindrome == palindrome[::-1]:
        print("Success!  Your phrase is a palindrome.")
        return True
    else:
        print("Your phrase is not a palindrome.")
        return False

def main():
    user_input = input("Enter a suspected palindrome: ")
    return(is_palindrome(user_input))

if __name__ == "__main__":
    main()
