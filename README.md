# 🧠 AI Code Complexity Predictor

> **A Machine Learning-powered Static Analysis tool that predicts the Big-O Time Complexity of C source code.**

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-red)
![Scikit-Learn](https://img.shields.io/badge/ML-Scikit--Learn-orange)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📖 Overview
Determining the time complexity of an algorithm is usually a manual task for Computer Science students. This project automates that process using **Natural Language Processing (NLP)** and **Supervised Learning**. 

By treating source code as "text" and syntax structures (loops, recursion, nesting) as "features," the AI classifies code into three complexity tiers:
* 🟢 **O(1)** - Constant Time
* 🟡 **O(n)** - Linear Time
* 🔴 **O(n^2)** - Quadratic Time

---

## ⚙️ How the AI Works (Methodology)

The core of this project relies on a pipeline that transforms raw C code into mathematical vectors.

### 1. Data Collection (Synthetic Augmentation)
Since no standard dataset exists for this problem, a **synthetic dataset** of 80+ C functions was generated.
* **Data Augmentation:** The dataset includes variations in variable naming (`i`, `j` vs `row`, `col`), formatting styles (one-liners vs indented), and "distractor" comments.

### 2. Feature Engineering (The "Brain")
We switched from standard TF-IDF to **CountVectorizer** with **N-Grams** to capture structural depth.
```python
# Captures single words ("for") and sequences ("for { for")
vectorizer = CountVectorizer(token_pattern=r"\b\w+\b|[^\w\s]", ngram_range=(1,3))
```

* **Why?** This ensures symbols like `{`, `}`, `++`, and `;` are treated as distinct features.
* **Insight:** The model learns that nested brackets `{{` often correlate with O(n^2).

## 📊 Results & Analysis

### 1. Model Accuracy & Validation
The model was rigorously tested using an 80-20 train-test split via the `train_research.py` script.

* **Overall Accuracy:** ~95.00%
* **Precision:** High precision in detecting $O(n^2)$ due to the N-Gram logic.

**Terminal Output Validation:**
<img width="680" height="654" alt="Screenshot 2026-01-07 at 7 20 24 PM" src="https://github.com/user-attachments/assets/9e58aca8-f363-4eec-96f1-5bc841ca1f65" />


### 2. Confusion Matrix Analysis
 <img width="581" height="470" alt="Screenshot 2026-01-07 at 7 20 04 PM" src="https://github.com/user-attachments/assets/9f3884e7-493b-44e6-b2ee-fd701892a697" />

### 3. Feature Importance (XAI)
The Random Forest model identified the following tokens as the strongest predictors:
1.  `for` (Loop Sequence)
2.  `n` (Variable)
3.  `+` (Plus Operator)

---

## 📸 App Screenshots

| **Input Interface** | **Result Visualization** |
|:---:|:---:|
| <img width="856" height="665" alt="Screenshot 2026-01-07 at 7 06 34 PM" src="https://github.com/user-attachments/assets/5c119434-98f6-4874-98fa-3617ebc1ae19" /> | <img width="737" height="483" alt="Screenshot 2026-01-07 at 7 53 14 PM" src="https://github.com/user-attachments/assets/52c4a710-4179-4a04-b07f-dff04faab650" /> |

---

## 🚀 Installation & Usage

1. **Clone the Repository**
   
       git clone https://github.com/YOUR_USERNAME/AI-Complexity-Predictor.git
       cd AI-Complexity-Predictor

2. **Install Dependencies**
   
       pip install -r requirements.txt

3. **Run the Application**
   
       streamlit run app.py

---

## ⚠️ Challenges & Limitations

* **Recursion Detection:** The model relies on iterative loops (`for`/`while`) and may miss complex recursion.
* **Variable Bounds:** The model assumes loops run to `n`. It cannot distinguish `i < 10` (O(1)) from `i < n` (O(n)) purely via token counting.

---

## 👨‍💻 Author
**Aryan Shukla** 2nd Year B.Tech AI Student  
*Passionate about AI, Algorithms, and ML.*
