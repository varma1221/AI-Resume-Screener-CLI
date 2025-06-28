import pdfplumber
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag
from nltk.corpus import wordnet
from rapidfuzz import fuzz

resume_path = input("📄 Enter the path to your RESUME PDF: ").strip('"')
jd_path = input("📝 Enter the path to the JOB DESCRIPTION PDF: ").strip('"')

print(f"\n✅ Resume file selected: {resume_path}")
print(f"✅ Job description file selected: {jd_path}")
print()

def get_wordnet_pos(tag):
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


nltk.download("punkt")
nltk.download("stopwords")
nltk.download("wordnet")
nltk.download("omw-1.4")
nltk.download("averaged_perceptron_tagger_eng")

with pdfplumber.open(resume_path) as pdf:
    extracted_resume_text = ""
    for page in pdf.pages:
        extracted_resume_text += page.extract_text()

resume_tokens = word_tokenize(extracted_resume_text.lower())


stop_words = set(stopwords.words("english"))

filtered_resume_words = []

for word in resume_tokens:
    if word.isalpha():
        if word not in stop_words:
            filtered_resume_words.append(word)

pos_tags = pos_tag(filtered_resume_words)

resume_lemmatizer = WordNetLemmatizer()

resume_lemmatized_words = []

for word,tag in pos_tags:
    wn_pos = get_wordnet_pos(tag)
    resume_lemma = resume_lemmatizer.lemmatize(word, pos=wn_pos)
    resume_lemmatized_words.append(resume_lemma)

clean_resume = resume_lemmatized_words
#######################################################################################
with pdfplumber.open(jd_path) as pdf:
    jd_text = ''
    for page in pdf.pages:
        jd_text += page.extract_text()

jd_tokens = word_tokenize(jd_text.lower())

jd_filtered_tokens = []

for word in jd_tokens:
    if word.isalpha():
        if not word in stop_words:
            jd_filtered_tokens.append(word)

pos_tags = pos_tag(jd_filtered_tokens)

jd_lemmatizer = WordNetLemmatizer()

jd_lemmatized_words = []
for word,tag in pos_tags:
    wn_pos = get_wordnet_pos(tag)
    jd_lemma = jd_lemmatizer.lemmatize(word, pos=wn_pos)
    jd_lemmatized_words.append(jd_lemma)

clean_jd = jd_lemmatized_words

resume_set = set(clean_resume)

matched_skills = []
missing_skills = []

for word in clean_jd:
    if word in resume_set:
        matched_skills.append(word)
    else:
        missing_skills.append(word)

fuzzy_matched = []

for word_jd in clean_jd:
    for word_resume in clean_resume:
        similarity = fuzz.ratio(word_jd, word_resume)
        if similarity > 80:
            fuzzy_matched.append(word_jd)
            break

match_percentage = (len(set(fuzzy_matched)) / len(set(clean_jd))) * 100

print("\n✅ Match Summary")
print("-----------------------")
print(f"Match Percentage: {match_percentage:.2f}%")

