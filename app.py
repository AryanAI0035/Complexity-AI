import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier

#Setup
st.set_page_config(page_title="Code Complexity AI",page_icon="🤖")

st.title("AI Code Complexity Predictor")
st.markdown("""
This tool uses **Machine Learning (Random Forest)** to analyze C code 
and predict its Time Complexity ($O(1)$, $O(n)$, $O(n^2)$).
""")

#Sidebar
st.sidebar.header("Project Stats")
try:
    df=pd.read_csv("complexity_data.csv").dropna()
    st.sidebar.success(f"Dataset Loaded: {len(df)} examples")
except:
    st.sidebar.error("Dataset not found!")
    st.stop()

#Training
# We use CountVectorizer because we care about the NUMBER of loops.
# ngram_range=(1,3) lets it see sequences like "for ( int" and "for { for"
vectorizer = CountVectorizer(token_pattern=r"\b\w+\b|[^\w\s]", ngram_range=(1,3))
X=vectorizer.fit_transform(df['code'])
model=RandomForestClassifier(n_estimators=100,random_state=42)
model.fit(X,df['label'])

#Interface
user_code=st.text_area("Paste your C Code snippet here:",height=200,placeholder="for(int i=0; i<n; i++) { ... }")

if st.button("Analyze Complexity"):
    if user_code:
        # 1. Transform
        vec=vectorizer.transform([user_code])
        # 2. Predict
        prediction=model.predict(vec)[0]
        # 3. Get Confidence
        probs=model.predict_proba(vec)[0]
        confidence=max(probs) * 100

        # 4. Display
        st.subheader("Results:")
        col1,col2=st.columns(2)
        with col1:
            if prediction=="O(1)":
                st.success(f"**Prediction:** {prediction} (Constant)")
            elif prediction=="O(n)":
                st.warning(f"**Prediction:** {prediction} (Linear)")
            else:
                st.error(f"**Prediction:** {prediction} (Quadratic)")
            st.caption(f"Confidence: {confidence:.1f}%")
        with col2:
            st.markdown("### Confidence Distribution")
            chart_data = pd.DataFrame(probs, index=model.classes_, columns=["Probability"])
            st.bar_chart(chart_data)
    else:
        st.warning("Please enter some code first.")

#Footer
st.markdown("---")
st.caption("Built with Python & Streamlit | 2nd Year AI Project")
