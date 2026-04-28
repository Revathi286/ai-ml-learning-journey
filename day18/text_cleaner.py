import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import string

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')

def clean_bio(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    tokens = word_tokenize(text)
    stop_words = set(stopwords.words('english'))
    filtered_text = [w for w in tokens if w not in stop_words]
    lemmatizer = WordNetLemmatizer()
    lemmatized_text = [lemmatizer.lemmatize(w) for w in filtered_text]
    
    return " ".join(lemmatized_text)

sample_bio = "I love Hiking in the mountains and Coding late at night!"

print(f"Cleaned Bio: {clean_bio(sample_bio)}")


from sklearn.feature_extraction.text import TfidfVectorizer

bios = [
"Expert in Python and Machine Learning for social good.",
"Professional Chef who loves outdoor Hiking and mountains.",
"Machine Learning enthusiast and mountain hiker."
]

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(bios)
print("Vocabulary:", vectorizer.get_feature_names_out())
print("Vector Shape:", tfidf_matrix.toarray().shape)