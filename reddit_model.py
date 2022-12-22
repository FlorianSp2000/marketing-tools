import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

# Read in the dataset of subreddit names and post titles
data = pd.read_csv('dataset_100.csv', index_col=0)

# Create a list of all the subreddit names
subreddit_names = data['subreddit']

# Create a list of all the post titles
post_titles = data['title'].tolist()

# Create a pipeline that vectorizes the post titles and trains a logistic regression model
model = Pipeline([
    ('vectorizer', TfidfVectorizer()),
    ('classifier', LogisticRegression())
])

# Fit the model to the post titles and subreddit names
model.fit(post_titles, subreddit_names)

# Define a function that takes in a subreddit name and generates a new post title
def generate_post_title(subreddit):
    # Use the model to predict a new post title for the given subreddit
    new_title = model.predict([subreddit])[0]
    return new_title

# Test the function by generating a new post title for the 'science' subreddit
print(generate_post_title('rapefantasies'))


# Estimates how many upvotes post title gets---
"""
# Import required libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load the dataset
df = pd.read_csv('dataset_100.csv')

# Preprocess the data
df['post_title'] = df['post_title'].apply(preprocess_text)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(df['post_title'], df['upvotes'], test_size=0.3)

# Vectorize the post titles
vectorizer = CountVectorizer()
X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

# Train the language model
model = MultinomialNB()
model.fit(X_train, y_train)

# Evaluate the model's performance
accuracy = model.score(X_test, y_test)
print('Accuracy:', accuracy)
"""

