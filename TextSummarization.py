import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from collections import defaultdict
import heapq
import string

# Download necessary NLTK data files
nltk.download('punkt')
nltk.download('stopwords')

# Preprocessing function to clean the text
def preprocess_text(text):
    # Tokenize the text into words and sentences
    sentences = sent_tokenize(text)
    words = word_tokenize(text.lower())
    
    # Remove stopwords and punctuation
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words and word not in string.punctuation]
    
    return sentences, words

# Function to generate the summary
def summarize(text, num_sentences=3):
    sentences, words = preprocess_text(text)
    
    # Compute word frequency
    word_freq = FreqDist(words)
    
    # Score each sentence based on word frequency
    sentence_scores = defaultdict(int)
    for sent in sentences:
        for word in word_tokenize(sent.lower()):
            if word in word_freq:
                sentence_scores[sent] += word_freq[word]
    
    # Select the top 'num_sentences' sentences based on sentence score
    summary_sentences = heapq.nlargest(num_sentences, sentence_scores, key=sentence_scores.get)
    return " ".join(summary_sentences)

# Example text for summarization
text = """
Artificial Intelligence (AI) is a branch of computer science that emphasizes the creation of intelligent machines 
that work and react like humans. AI is an interdisciplinary science with multiple approaches, but advancements 
in machine learning and deep learning are creating a paradigm shift in virtually every sector of the tech industry. 
AI applications include advanced web search engines, recommendation systems, digital assistants, self-driving cars, 
and more. Machine Learning (ML) is a subset of AI that allows computers to learn from data, identify patterns, 
and make decisions with minimal human intervention.
"""

# Generate summary
summary = summarize(text, num_sentences=2)
print("Summary:")
print(summary)
