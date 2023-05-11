# Dependecies
from textblob import TextBlob
from difflib import SequenceMatcher

def grade_motto(motto, target_phrase):
    # Calculate similarity score between motto and target phrase
    similarity_score = SequenceMatcher(None, motto, target_phrase).ratio()
    
    # Create a TextBlob object from the motto
    blob = TextBlob(motto)
    
    # Calculate polarity and subjectivity scores
    polarity_score = blob.sentiment.polarity
    subjectivity_score = blob.sentiment.subjectivity
    
    # Calculate length score
    length_score = len(motto)
    
    # Normalize similarity score to be in the range [-100, 100]
    similarity_score = (2 * similarity_score - 1) * 100
    
    # Return the four scores as a list
    return [polarity_score, subjectivity_score, length_score, similarity_score]

# Example usage
def main():
    motto = input("Enter a motto: ")
    target_phrase = input("Enter a target phrase: ")
    scores = grade_motto(motto, target_phrase)
    print("Positivity score:", scores[0])
    print("Subjectivity score:", scores[1])
    print("Length score:", scores[2])
    print("Similarity score:", scores[3])


if __name__ == '__main__':
    main()