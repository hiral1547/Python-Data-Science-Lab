# Aim: To implement basic Machine Learning functionalities using Scikit-learn 
# to predict whether a user will like a movie based on viewing behavior.

# Basic Machine Learning using Scikit-learn
# Real-world IT Use Case: Netflix Movie Recommendation

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


# ---------------------------------------
# 1. Create sample user data
# ---------------------------------------

data = {
    "Watch_Hours": [
        1, 2, 3, 4, 5,
        6, 7, 8, 2, 3,
        6, 7, 1, 4, 8
    ],

    "Previous_Ratings": [
        2, 2, 3, 3, 4,
        5, 5, 5, 2, 3,
        4, 5, 1, 4, 5
    ],

    # 0 = Dislike
    # 1 = Like
    "Liked": [
        0, 0, 0, 1, 1,
        1, 1, 1, 0, 0,
        1, 1, 0, 1, 1
    ]
}

df = pd.DataFrame(data)

print("Netflix User Data:")
print(df)


# ---------------------------------------
# 2. Select Features and Target
# ---------------------------------------

X = df[["Watch_Hours", "Previous_Ratings"]]

y = df["Liked"]


# ---------------------------------------
# 3. Split data
# ---------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.30,
    random_state=42
)


# ---------------------------------------
# 4. Create Machine Learning Model
# ---------------------------------------

model = DecisionTreeClassifier(
    random_state=42
)


# ---------------------------------------
# 5. Train the model
# ---------------------------------------

model.fit(X_train, y_train)


# ---------------------------------------
# 6. Make predictions
# ---------------------------------------

y_pred = model.predict(X_test)

print("\nActual Values:")
print(y_test.values)

print("\nPredicted Values:")
print(y_pred)


# ---------------------------------------
# 7. Calculate Accuracy
# ---------------------------------------

accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", accuracy)


# ---------------------------------------
# 8. Predict for a New User
# ---------------------------------------

new_user = pd.DataFrame({
    "Watch_Hours": [7],
    "Previous_Ratings": [5]
})

prediction = model.predict(new_user)


if prediction[0] == 1:
    print("\nPrediction: User is likely to LIKE the movie.")
else:
    print("\nPrediction: User is likely to DISLIKE the movie.")


# User 1 → Watch 1 hour, rating 2 → Disliked → 0
# User 2 → Watch 2 hours, rating 2 → Disliked → 0
# User 3 → Watch 3 hours, rating 3 → Disliked → 0
# User 4 → Watch 4 hours, rating 3 → Liked    → 1
# User 5 → Watch 5 hours, rating 4 → Liked    → 1

# Why do we use data?
    # We use it to create a Pandas DataFrame:
    # df = pd.DataFrame(data)
    # This converts the dictionary into a table that looks like:

#        Watch_Hours  Previous_Ratings  Liked
# 0            1             2            0
# 1            2             2            0
# 2            3             3            0
# 3            4             3            1
# 4            5             4            1