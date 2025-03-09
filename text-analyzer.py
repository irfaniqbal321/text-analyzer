import streamlit as st

def count_vowels(text):
    vowels = 'aeiouAEIOU'
    return sum(1 for char in text if char in vowels)

def main():
    st.title("Text Analyzer")
    
    # User input with validation
    text = st.text_area("Enter your paragraph:")
    if st.button("Analyze"):
        if not text.strip():
            st.error("Please enter some text to analyze!")
            return
            
        # Word and character count
        words = text.split()
        word_count = len(words)
        char_count = len(text)
        
        # Convert counts to strings (type casting)
        word_count_str = str(word_count)
        char_count_str = str(char_count)
        
        # Vowels count
        vowel_count = count_vowels(text)
        vowel_count_str = str(vowel_count)
        
        # Display basic statistics
        st.subheader("Basic Statistics")
        st.write(f"Total Words: {word_count_str}")
        st.write(f"Total Characters: {char_count_str}")
        st.write(f"Total Vowels: {vowel_count_str}")
        
        # Calculate and display average word length
        avg_word_length = char_count / word_count if word_count > 0 else 0
        st.write(f"Average Word Length: {avg_word_length:.2f}")
        
        # Search and Replace functionality
        st.subheader("Search and Replace")
        search_word = st.text_input("Enter word to search:")
        replace_word = st.text_input("Enter word to replace with:")
        
        if search_word and replace_word:
            modified_text = text.replace(search_word, replace_word)
            st.write("Modified text:")
            st.write(modified_text)
        
        # Case conversion
        st.subheader("Case Conversion")
        st.write("Uppercase version:")
        st.write(text.upper())
        st.write("Lowercase version:")
        st.write(text.lower())
        
        # Check for "python" using comparison operator
        st.subheader("Python Check")
        if "python" in text.lower():
            st.write("This text contains the word 'python'!")
        else:
            st.write("This text does not contain the word 'python'.")

if __name__ == "__main__":
    main()
