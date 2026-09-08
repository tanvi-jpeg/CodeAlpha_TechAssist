#takes data from faqs.json and uses it to answer for user question
import json
#used for regular expressions (text-cleaning)
import re
#used for natural language processing (NLP) tasks
import nltk
# stopwords are common words that are usually filtered out in NLP tasks like "the", "is", "in", etc.
from nltk.corpus import stopwords
#Lemmartizer is used to convert words to thier base form (e.g., "running" -> "run", "better" -> "good")
from nltk.stem import WordNetLemmatizer
#converts text into numerical TF-IDF vectors, which represent the importance of words in documents
from sklearn.feature_extraction.text import TfidfVectorizer
#used to calculate the similarity between two vectors, which helps in finding the most relevant FAQ answer based on the user's question
from sklearn.metrics.pairwise import cosine_similarity


#for english stopwords
nltk.download("stopwords")
# for lemmatization
nltk.download("wordnet")
# additional wordNet resources for lemmatization
nltk.download("omw-1.4")

#to convert words to their base form
lemmatizer = WordNetLemmatizer()
#to load english stopwords into a set for efficient lookup
stop_words = set(stopwords.words("english"))


# Load FAQ data from the JSON file
with open("data/faqs.json", "r", encoding="utf-8") as file:
    faqs = json.load(file)


#Text Procesing Function
def preprocess(text):
    text = text.lower() #convert text to lowercase
    text = re.sub(r"[^a-zA-Z\s]", "", text) #remove punctuation,numbers and special characters

    words = text.split() #split the text into individual words

# only sees the important content
    words = [
        word for word in words
        if word not in stop_words
    ]
#convert words to their base form
    words = [
        lemmatizer.lemmatize(word)
        for word in words
    ]

#joins the words back into a single string and returns the processed text
    return " ".join(words)

#extracts the questions from the FAQs and preprocesses them to prepare for vectorization
questions = [faq["question"] 
             for faq in faqs]

#preprocesses every FAQ question
processed_questions = [
    preprocess(question)
    for question in questions
]

#creates TF-IDF vectorizer, converts text to numbers
vectorizer = TfidfVectorizer()

#transforms all FAQ questions to TF-IDF vectors
faq_vectors = vectorizer.fit_transform(processed_questions)

#for best FAQ Answer match
def get_response(user_question):
    processed_question = preprocess(user_question) #processes the user question

#Checks if the user question is empty or contains only whitespace then it returns enter a question.
    if not processed_question.strip():
        return "Please enter a question."

#transforms the user question to TF-IDF vector
    user_vector = vectorizer.transform([processed_question])

#compares the user question vector with all FAQ questions
    similarity_scores = cosine_similarity(
        user_vector,
        faq_vectors
    )[0]

#finds the index of the FAQ question with the highest similarity score
    best_match_index = similarity_scores.argmax()

    #gets the highest similarity score
    best_score = similarity_scores[best_match_index]

#minimum similarity score
    threshold = 0.20

#if the best similarity score is below the threshold, it returns a message indicating that no relevant answer was found
    if best_score < threshold:
        return "Sorry, I couldn't find a relevant answer to your question."

#otherwise,returns the best match answer from the FAQs
    return faqs[best_match_index]["answer"]

#runs the chatbot in a loop, allowing the user to ask questions until they type 'quit' to exit
if __name__ == "__main__":
    print("🤖 FAQ Chatbot")
    print("Type 'quit' to exit.\n")

    while True:
        user_question = input("You: ")

        if user_question.lower() == "quit":
            print("Bot: Goodbye! 👋")
            break

        response = get_response(user_question)

        print("Bot:", response)