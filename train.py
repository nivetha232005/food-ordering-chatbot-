import json
import numpy as np
import nltk
import pickle
import random
from nltk.stem import WordNetLemmatizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelBinarizer
from sklearn.metrics import accuracy_score
import os

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt', quiet=True)
    
try:
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('wordnet', quiet=True)
    
try:
    nltk.data.find('corpora/omw-1.4')
except LookupError:
    nltk.download('omw-1.4', quiet=True)

lemmatizer = WordNetLemmatizer()

# Load intents
with open('intents.json', 'r', encoding='utf-8') as file:
    intents = json.load(file)

words = []
classes = []
documents = []
ignore_words = ['?', '!', '.', ',', ';', ':']

# Process intents
for intent in intents['intents']:
    for pattern in intent['patterns']:
        # Tokenize each word
        w = nltk.word_tokenize(pattern)
        words.extend(w)
        # Add documents
        documents.append((w, intent['tag']))
        # Add to classes
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

# Lemmatize and lowercase words
words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words]
words = sorted(list(set(words)))
classes = sorted(list(set(classes)))

print(f"Found {len(words)} unique words")
print(f"Found {len(classes)} classes: {classes}")

# Create training data
training = []
output_empty = [0] * len(classes)

for doc in documents:
    bag = []
    pattern_words = doc[0]
    pattern_words = [lemmatizer.lemmatize(word.lower()) for word in pattern_words]
    
    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)
    
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1
    
    training.append([bag, output_row])

random.shuffle(training)
training = np.array(training, dtype=object)

train_x = np.array(list(training[:, 0]))
train_y = np.array(list(training[:, 1]))

print(f"Training data shape: {train_x.shape}")

# Use Random Forest Classifier instead of Neural Network
print("Training Random Forest Classifier...")
rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier.fit(train_x, train_y)

# Save the model using joblib (more reliable than pickle for sklearn models)
import joblib
joblib.dump(rf_classifier, 'chatbot_model.joblib')
print("Model saved as chatbot_model.joblib")

# Also save in pickle format for compatibility
with open('chatbot_model_sklearn.pkl', 'wb') as f:
    pickle.dump(rf_classifier, f)

# Save words and classes
with open('words.pkl', 'wb') as f:
    pickle.dump(words, f)
    
with open('classes.pkl', 'wb') as f:
    pickle.dump(classes, f)

print("Training completed successfully!")

# Test the model
test_sentence = "I want pizza"
test_bow = []
test_words = nltk.word_tokenize(test_sentence)
test_words = [lemmatizer.lemmatize(word.lower()) for word in test_words]
for w in words:
    test_bow.append(1) if w in test_words else test_bow.append(0)

prediction = rf_classifier.predict([test_bow])[0]
predicted_class = classes[np.argmax(prediction)]
print(f"Test prediction for '{test_sentence}': {predicted_class}")
