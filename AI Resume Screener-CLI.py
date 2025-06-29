"""
Resume-Job Description Matching Tool

This script analyzes and matches resume content against job descriptions using natural language processing.
It extracts text from PDF files, processes the text through tokenization, lemmatization, and performs
both exact and fuzzy matching to calculate compatibility percentage.

Dependencies:
    - pdfplumber: For PDF text extraction
    - nltk: For natural language processing tasks
    - rapidfuzz: For fuzzy string matching
"""

from typing import List, Tuple, Set, Any
import pdfplumber
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from nltk.corpus import wordnet
from rapidfuzz import fuzz

# Get file paths from user input
resume_path: str = input("📄 Enter the path to your RESUME PDF: ").strip('"')
jd_path: str = input("📝 Enter the path to the JOB DESCRIPTION PDF: ").strip('"')

# Display selected file paths
print(f"\n✅ Resume file selected: {resume_path}")
print(f"✅ Job description file selected: {jd_path}")
print()

def get_wordnet_pos(tag: str) -> str:
    """
    Convert NLTK POS tag to WordNet POS tag for better lemmatization.
    
    Args:
        tag (str): NLTK part-of-speech tag
        
    Returns:
        str: WordNet POS tag constant (ADJ, VERB, NOUN, or ADV)
    """
    if tag.startswith("J"):
        return wordnet.ADJ
    elif tag.startswith("V"):
        return wordnet.VERB
    elif tag.startswith("N"):
        return wordnet.NOUN
    elif tag.startswith("R"):
        return wordnet.ADV
    else:
        return wordnet.NOUN

# Download required NLTK data packages
nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("omw-1.4")
nltk.download("averaged_perceptron_tagger_eng")

# Extract text from resume PDF
with pdfplumber.open(resume_path) as pdf:
    extracted_resume_text: str = ""
    for page in pdf.pages:
        extracted_resume_text += page.extract_text()

# Tokenize resume text and convert to lowercase
resume_tokens: List[str] = word_tokenize(extracted_resume_text.lower())

# Get English stop words
stop_words: Set[str] = set(stopwords.words("english"))

# Filter resume words: keep only alphabetic words that are not stop words
filtered_resume_words: List[str] = []
for word in resume_tokens:
    if word.isalpha():
        if word not in stop_words:
            filtered_resume_words.append(word)

# Apply POS tagging to filtered resume words
pos_tags: List[Tuple[str, str]] = pos_tag(filtered_resume_words)

# Initialize lemmatizer for resume processing
resume_lemmatizer: WordNetLemmatizer = WordNetLemmatizer()

# Lemmatize resume words based on their POS tags
resume_lemmatized_words: List[str] = []
for word,tag in pos_tags:
    wn_pos: str = get_wordnet_pos(tag)
    resume_lemma: str = resume_lemmatizer.lemmatize(word, pos=wn_pos)
    resume_lemmatized_words.append(resume_lemma)

# Store processed resume words
clean_resume: List[str] = resume_lemmatized_words

#######################################################################################

# Extract text from job description PDF
with pdfplumber.open(jd_path) as pdf:
    jd_text: str = ''
    for page in pdf.pages:
        jd_text += page.extract_text()

# Tokenize job description text and convert to lowercase
jd_tokens: List[str] = word_tokenize(jd_text.lower())

# Filter job description words: keep only alphabetic words that are not stop words
jd_filtered_tokens: List[str] = []
for word in jd_tokens:
    if word.isalpha():
        if not word in stop_words:
            jd_filtered_tokens.append(word)

# Apply POS tagging to filtered job description words
pos_tags: List[Tuple[str, str]] = pos_tag(jd_filtered_tokens)

# Initialize lemmatizer for job description processing
jd_lemmatizer: WordNetLemmatizer = WordNetLemmatizer()

# Lemmatize job description words based on their POS tags
jd_lemmatized_words: List[str] = []
for word,tag in pos_tags:
    wn_pos: str = get_wordnet_pos(tag)
    jd_lemma: str = jd_lemmatizer.lemmatize(word, pos=wn_pos)
    jd_lemmatized_words.append(jd_lemma)

# Store processed job description words
clean_jd: List[str] = jd_lemmatized_words

# Convert resume words to set for faster lookup
resume_set: Set[str] = set(clean_resume)

# Lists to store matched and missing skills
matched_skills: List[str] = []
missing_skills: List[str] = []

# Perform exact matching between job description and resume words
for word in clean_jd:
    if word in resume_set:
        matched_skills.append(word)
    else:
        missing_skills.append(word)

# List to store fuzzy matched words
fuzzy_matched: List[str] = []

# Perform fuzzy matching with 80% similarity threshold
for word_jd in clean_jd:
    for word_resume in clean_resume:
        similarity: int = fuzz.ratio(word_jd, word_resume)
        if similarity > 80:
            fuzzy_matched.append(word_jd)
            break

# Calculate match percentage based on fuzzy matching results
match_percentage: float = (len(set(fuzzy_matched)) / len(set(clean_jd))) * 100

# Display final results
print("\n✅ Match Summary")
print("-----------------------")
print(f"Match Percentage: {match_percentage:.2f}%")
