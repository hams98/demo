import re
from django.core.exceptions import ValidationError

#for single character responses like aaaaaaaaaaaaaaaa
def validate_meaningful_response(value):
    print("validate_meaningful_response triggered")
    if value and len(set(value)) <= 1:
        raise ValidationError("Please provide a more meaningful response")

# for minimum 10 charcater length of 10
def validate_min_length(value):
    print("validate_min_length triggered")
    if value and len(value) < 10:
        raise ValidationError("This field must be at least 10 characters long")

# Validate against excessive punctuation
def validate_no_excessive_punctuation(value):
    excessive_punctuation = ["!!!", "???", "...."]  # Add more patterns as needed
    for pattern in excessive_punctuation:
        if pattern in value:
            raise ValidationError("Please avoid excessive punctuation in your response.")
        

# Validate against specific patterns (e.g., phone numbers, email addresses)
def validate_no_patterns(value):
    patterns_to_avoid = [r'\d{10}', r'\S+@\S+\.\S+']  # Add more regex patterns as needed
    for pattern in patterns_to_avoid:
        if re.search(pattern, value):
            raise ValidationError("Please provide a response without specific patterns (e.g., phone numbers, email addresses).")

# Validate against overly short or trivial responses
def validate_not_trivial(value):
    trivial_responses = ["yes", "no", "ok", "maybe", "idk", "lol", "haha"]  # Add more trivial responses
    if value.lower() in trivial_responses:
        raise ValidationError("Please provide a more substantial response.")
    
def validate_no_repetitive_characters(value):
    """
    Validate that the response does not contain words with repetitive characters.
    For example, "aannyydddd" would trigger this validation.
    """
    words = value.split()  # Split the response into individual words
    repetitive_words = []

    for word in words:
        # Check if the word has repetitive characters (e.g., "aannyydddd")
        if any(char * 3 in word for char in word):
            repetitive_words.append(word)

    if repetitive_words:
        raise ValidationError(f"Words with repetitive characters found: {', '.join(repetitive_words)}")