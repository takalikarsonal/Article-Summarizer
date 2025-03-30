# Article-Summarizer

This project demonstrates how to perform **extractive text summarization** using the **Natural Language Toolkit (NLTK)** in Python. The solution is designed to process large amounts of text, clean it, and extract the most important sentences based on word frequency.

## Features
- **Text Preprocessing**: Tokenization, stopword removal, and punctuation removal.
- **Sentence Scoring**: Assigns scores to sentences based on the frequency of words they contain.
- **Extractive Summarization**: Selects the top `n` most important sentences to generate a summary.

## Libraries Used
- [NLTK](https://www.nltk.org/) - A powerful Python library for natural language processing.
- [Heapq](https://docs.python.org/3/library/heapq.html) - For efficiently extracting the largest sentences based on scores.
- [collections](https://docs.python.org/3/library/collections.html) - To use `defaultdict` for sentence score storage.

## Installation

To run the project, you'll need to install the required dependencies. You can do this by running:
pip install nltk

## Usage

- Clone the repository:
  git clone [https://github.com/your-username/text-summarization-nltk.git](https://github.com/takalikarsonal/Article-Summarizer.git)
- cd Article-Summarizer
- Run the script:
  python TextSummerization.py
- Modify the text variable in the script with your own content or provide text input as needed.
