import re
user_input = ''

def string_cleaner(user_input):
    no_punc = re.sub(r'\W+', '', user_input)
    clean_string = no_punc.lower()
    return clean_string

def is_palindrome(user_input):
    clean_string = string_cleaner(user_input)
    if len(clean_string) < 2:
        print("Success!  Your phrase is a palindrome.")
        return True
    if clean_string[0] != clean_string[-1]:
        print("Your phrase is not a palindrome.")
        return False
    return is_palindrome(clean_string[1:-1])

def main():
    user_input = input("Enter a suspected palindrome: ")
    return(is_palindrome(user_input))

if __name__ == "__main__":
    main()

#is_palindrome(clean_string)
