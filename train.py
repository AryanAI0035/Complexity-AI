import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, ConfusionMatrixDisplay
from sklearn.tree import plot_tree

#Loading Dataset
try:
    df=pd.read_csv("complexity_data.csv").dropna()
except FileNotFoundError:
    print("Error: 'complexity_data.csv' not found!")
    exit()

#Vectorizing Code
vectorizer = CountVectorizer(token_pattern=r"\b\w+\b|[^\w\s]", ngram_range=(1,3))
X=vectorizer.fit_transform(df['code'])
y=df['label']

#Training
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.35,random_state=42)

print("Training Random Forest Model..")
model=RandomForestClassifier(n_estimators=100,random_state=42)
model.fit(X_train,y_train)

#Insights
predictions=model.predict(X_test)
acc=accuracy_score(y_test,predictions)

print("\n"+"="*40)
print(f"MODEL ACCURACY: {acc*100:.2f}%")
print("="*40)
print("\n---DETAILED METRICS---")
print(classification_report(y_test,predictions))

print("\n---EXPLAINABLE AI (XAI)---")
print("Top 10 tokens the AI uses to decide:")
feature_names=vectorizer.get_feature_names_out()
importances=model.feature_importances_
indices=np.argsort(importances)[::-1]

for i in range(10):
    if i<len(indices):
        token=feature_names[indices[i]]
        score=importances[indices[i]]
        print(f"Rank {i+1}: '{token}' (Importance: {score:.4f})")

#Visualization
print("\nConfusion Matrix...")
disp=ConfusionMatrixDisplay.from_estimator(model,X_test,y_test)
plt.title("Confusion Matrix: Where did the AI fail?")
plt.show()

#Tree
print("🌳 Generating Decision Tree")
plt.figure(figsize=(20,10))
plot_tree(model.estimators_[0],
          feature_names=vectorizer.get_feature_names_out(),
          class_names=model.classes_,
          filled=True,
          rounded=True,
          max_depth=3)
plt.title("Visualizing One Decision Tree from the Random Forest")
plt.show()
