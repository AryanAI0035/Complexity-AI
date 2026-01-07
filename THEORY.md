Here is a comprehensive **Theory Guide** (approx. 1000 words) tailored for undergraduate students. It breaks down the complex Machine Learning concepts into simple, digestible analogies.

Create a new file in your repository named **`THEORY.md`** and paste this content inside.

---

# 📘 Theoretical Foundations: How AI Predicts Code Complexity

## 1. Introduction

In Computer Science, **Time Complexity** is the theoretical speed limit of an algorithm. It tells us how the runtime of a program grows as the input size () increases. Traditionally, determining this requires a human expert to mathematically analyze loops, recursion, and variable states.

This project asks a fundamental question: **"Can we teach an Artificial Intelligence to 'read' C code and predict its complexity just like a human would?"**

To achieve this, we combine two powerful fields of Computer Science:

1. **Static Analysis:** Examining code without running it.
2. **Natural Language Processing (NLP):** Treating code as a language (like English) to find patterns.

---

## 2. The Core Concepts (The "What")

Before understanding the AI, we must understand what it is predicting. This model classifies code into three "Buckets of Speed":

### 🟢 Constant Time - 

* **Definition:** The code takes the exact same amount of time, no matter how much data you throw at it.
* **Analogy:** Looking up the first name in a phone book. It takes one second whether the book has 10 names or 1,000,000 names.
* **Code Pattern:** No loops, just simple math or `if-else` statements.

### 🟡 Linear Time - 

* **Definition:** The runtime grows directly in proportion to the input. If you double the data, you double the time.
* **Analogy:** Reading a book page-by-page. A 100-page book takes 1 hour; a 200-page book takes 2 hours.
* **Code Pattern:** A single loop (`for`, `while`) that iterates from `0` to `n`.

### 🔴 Quadratic Time - 

* **Definition:** The runtime grows exponentially. If you double the data, the time quadruples.
* **Analogy:** Having a deck of cards and comparing *every* card to *every other* card to check for duplicates.
* **Code Pattern:** Nested loops—a loop *inside* another loop.

---

## 3. Treating Code as Language (The "How")

Computers cannot "read" code; they only understand numbers. To feed C code into an AI model, we must convert it into a numerical format. This process is called **Vectorization**.

### 3.1 Tokenization

First, we break the raw code string into "tokens" (words and symbols).

* **Input:** `for(int i=0; i<n; i++)`
* **Bad Tokenization:** Splitting by space might give `for(int` as one word.
* **Our Solution:** We use **Regex Tokenization** (`r"\b\w+\b|[^\w\s]"`). This forces the computer to see symbols as separate entities:
* `for` `(` `int` `i` `=` `0` `;` ...
* **Why?** Because in C, symbols like `{` and `;` carry huge meaning!



### 3.2 The "Bag of Words" Problem

Standard NLP uses a technique called "Bag of Words." It counts how many times words appear but ignores order.

* **Sentence A:** "The dog bit the man."
* **Sentence B:** "The man bit the dog."
* To a standard AI, these look **identical** because they contain the exact same words.

In code, this is a disaster:

* **Code A (Sequential):** Loop 1 ends `}`, then Loop 2 starts. (Speed: )
* **Code B (Nested):** Loop 1 starts `{`, then Loop 2 starts immediately inside. (Speed: )

If the AI only counts "2 loops" and "2 brackets," it cannot tell the difference.

### 3.3 The Solution: N-Grams

To fix this, we use **N-Grams**. Instead of looking at single words, we look at **sequences of words**.
We configured our model to look at **Bigrams (2 words)** and **Trigrams (3 words)**.

* Now the AI sees patterns like:
* `{ for` (Open bracket followed by loop  **Nesting**)
* `} for` (Close bracket followed by loop  **Sequential**)
This allows the model to "understand" structure without actually knowing how to compile code.



---

## 4. The Brain: Random Forest Classifier

Once the code is converted into numbers (vectors), we need a brain to make the decision. We chose the **Random Forest** algorithm.

### 4.1 What is a Decision Tree?

Imagine a flowchart.

1. Does the code contain `for`?
* **No:** Predict .
* **Yes:** Go to next question.


2. Does the code contain `for { for`?
* **Yes:** Predict .
* **No:** Predict .



A single Decision Tree is good, but it can be "biased" (it might over-focus on one specific keyword).

### 4.2 Why Random Forest?

A Random Forest creates **100 different Decision Trees**.

* Tree #1 looks mostly at `{` symbols.
* Tree #2 looks mostly at keywords like `while`.
* Tree #3 looks at variable assignments.

When a new code snippet comes in, all 100 trees vote.

* 80 trees say 
* 20 trees say 
* **Final Prediction:** 

This "Ensemble Learning" makes our model incredibly robust against weird formatting or unusual variable names.

---

## 5. The Hybrid Architecture (Our Innovation)

Pure Machine Learning has a flaw: it is probabilistic. It "guesses" based on what it has seen before. In strict algorithmic analysis, sometimes a simple logical rule is more accurate than a probability.

We implemented a **Hybrid System**:

1. **The ML Model:** Does the heavy lifting. It identifies keywords, context, and vague structures.
2. **The Logic Layer (Heuristic Override):** We wrote a simple Python script that physically counts the **Maximum Nesting Depth** of the curly braces `{ }`.
* If `Depth >= 2` AND specific loop keywords are present, we **override** the AI and force a prediction of Quadratic Time ().



This combination gives us the best of both worlds: the flexibility of AI to handle messy code, and the precision of logic to catch deep nesting.

---

## 6. Limitations & The Halting Problem

No discussion on code analysis is complete without mentioning the **Halting Problem**.

> *Alan Turing proved that it is mathematically impossible to create a program that can perfectly predict the behavior of **all** other programs.*

Our tool is an **Approximation**. It has specific limitations:

1. **Recursion:** The model relies on explicit loop keywords (`for`, `while`). It struggles to detect recursion (a function calling itself) because that structure is much harder to capture with simple N-Grams.
2. **Variable Bounds:**
* `for(i=0; i<n; i++)` is .
* `for(i=0; i<5; i++)` is technically  (it runs 5 times, always).
* Our AI sees "loop" and likely guesses  for both, because it doesn't semanticially "understand" that `5` is a constant number and `n` is a variable.



## 7. Conclusion

This project demonstrates a practical application of **Supervised Learning** on **Structured Text**. By treating code syntax as features, we successfully built a tool that provides instant feedback to students, bridging the gap between abstract theory and practical coding.
