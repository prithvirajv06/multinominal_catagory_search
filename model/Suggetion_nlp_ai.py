from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn import metrics
import pandas as pd
import joblib

csv_file_path = 'data.csv'

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(csv_file_path,sep=',')

# Extract the 'Text' column and store it in X
X = df['Text'].tolist()
y = df['Category'].tolist()

# Assume 'X' is a list of texts and 'y' is a list of corresponding business categories
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Convert text data to TF-IDF features
vectorizer = TfidfVectorizer()
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

# Train Naive Bayes classifier
clf = MultinomialNB()
clf.fit(X_train_tfidf, y_train)

# Make predictions
y_pred = clf.predict(X_test_tfidf)

# Evaluate the model
accuracy = metrics.accuracy_score(y_test, y_pred)
precision = metrics.precision_score(y_test, y_pred, average='weighted')
recall = metrics.recall_score(y_test, y_pred, average='weighted')
f1 = metrics.f1_score(y_test, y_pred, average='weighted')

print(f"Accuracy: {accuracy:.2f}")
print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1 Score: {f1:.2f}")

# Save the vectorizer and classifier using joblib
joblib.dump(vectorizer, 'tfidf_vectorizer.joblib')
joblib.dump(clf, 'naive_bayes_classifier.joblib')

# Assuming clf is the trained Naive Bayes model and vectorizer is the TF-IDF vectorizer
# You should replace these with your actual trained model and vectorizer

# Example user input
# user_input = "I'm interested in learning about artificial intelligence."

# Preprocess the input
# You should use the same preprocessing steps applied to the training data
# For simplicity, let's assume basic tokenization and lowercase conversion
# processed_input = [word.lower() for word in user_input.split()]

# Vectorize the input
# input_tfidf = vectorizer.transform([' '.join(processed_input)])

# Make a prediction
# predicted_category = clf.predict(input_tfidf)[0]

# Display the result
# print(f"Predicted Business Category: {predicted_category}")
