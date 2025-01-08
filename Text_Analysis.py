def analyzeText(text):
    print("\n--- Text Analysis Results ---")
    print(f"Original Text: {text}")
    print(f"Text in uppercase: {text.upper()}")
    print(f"Text in lowercase: {text.lower()}")
    print(f"Reversed Text: {text[::-1]}")
    
    words = text.split()
    print(f"Word Count: {len(words)}")
    print(f"Character count (excluding spaces): {len(text.replace('', ''))}")
    
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in text if char in vowels)
    consonant_count = sum(1 for char in text if char.isalpha() and char not in vowels)
    print(f"Vowel Count: {vowel_count}")
    print(f"Consonant Count: {consonant_count}")
    
def main():
    print("Welcome to the text analysis tool.")
    
    while True:
        text = input("Enter a sentence (or type 'exit' to quit ): ").strip()
        if text.lower() == 'exit':
            print("Thank you for using text analysis tool. Goodbye")
            break
        elif text == "":
            print("Input cannot be empty. Please try again")  
        else:
            analyzeText(text)
                  

if __name__ == "__main__":
    main()                  