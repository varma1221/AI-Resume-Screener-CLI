# AI-Resume-Screener-(Command Line Version)
A beginner-friendly command-line tool that compares a resume PDF with a job description PDF and calculates a keyword-based match score using basic Natural Language Processing (NLP) techniques.

**📌 Project Description**

This project reads two PDF files — one containing a candidate’s resume and the other a job description and processes the text to calculate a match percentage. It uses elementary NLP techniques such as tokenization, stopword removal, lemmatization, and fuzzy string comparison to identify keyword overlaps between the two documents.

While the accuracy is basic, the intent is educational: to simulate a real-world screening concept using beginner-level tools.

**✅ Features**
1) Extracts and cleans text from PDF resumes and job descriptions
2) Applies NLP techniques: tokenization, stopword removal, lemmatization
3) Uses fuzzy matching to compute a similarity score
4) Accepts inputs via Command Line Interface (CLI)

Beginner-friendly, lightweight, and easy to run locally

**🛠️ Technologies Used**
1) Python 3.10+
2) pdfplumber – PDF text extraction
3) nltk – Tokenization, stopword removal, POS tagging, lemmatization
4) fuzzywuzzy – Fuzzy string comparison

**📁 Project Structure**
AI-Resume-Screener-CLI/
├── AI-Resume-Screener-CLI.py      # Main script file
├── LICENSE                        # MIT License
├── README.md                      # Project description and instructions
├── requirements.txt               # Dependency list for pip install

**🚀 How to Run**

**Install required libraries:**

pip install pdfplumber nltk fuzzywuzzy python-Lemmatization

**Run the script:**

python AI-Resume-Screener-CLI.py

When prompted, enter the full file paths to:
Your Resume PDF
The Job Description PDF

View the match percentage in the terminal.

**Note**: Match accuracy is based purely on keyword and phrase similarity, not deep contextual meaning.

**⚠️ Limitations**
1) This is a prototype for learning purposes and not production-ready.
2) Does not use advanced AI or ML models
3) Only compares word-level similarity
4) Cannot understand intent, tone, or experience level

**Results may vary based on formatting and phrasing**

**🌱 What I Learned**
1) How to extract and clean text from PDFs
2) Basics of NLP: tokenization, stopwords, POS tagging, lemmatization
3) CLI-based interaction and text-based input
4) Modular coding practices
5) Importance of testing, debugging, and documentation

**🙏 Acknowledgements**
Special thanks to:
ChatGPT – For step-by-step guidance, mentoring, and explanations
Developers of nltk, pdfplumber, and fuzzywuzzy for building accessible tools for beginners

**👤 About the Author**
I am Penmatsa Tanoj Pavan Surya Varma, a first-year B.Tech student in CSE (AI & ML). I know only basic Python and am still new to NLP. I have not learned NLP or libraries like NLTK fully. I referred to ChatGPT extensively to understand and build this project. This is my first complete project, built with determination, curiosity, and a desire to learn. This project is a milestone in my learning journey and a foundation for more advanced tools I hope to build in the future.
