import streamlit as st
from transformers import pipeline
import pandas as pd
import datetime

@st.cache_resource
def load_classifier():
    return pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

classifier = load_classifier()

probability_ranges = {
    "Remote": "0–5%",
    "Highly Improbable": "5–15%",
    "Improbable": "15–35%",
    "Roughly Even Odds": "35–65%",
    "Probable": "65–80%",
    "Highly Probable": "80–95%",
    "Nearly Certain": "95–100%"
}

label_explanations = {
    "Remote": "Extremely unlikely",
    "Highly Improbable": "Very unlikely, but not impossible",
    "Improbable": "Unlikely, but might happen",
    "Roughly Even Odds": "Could go either way",
    "Probable": "More likely than not",
    "Highly Probable": "Very likely",
    "Nearly Certain": "Almost sure to happen"
}

labels = list(probability_ranges.keys())

st.title("🧠 Uncertainly Yours")
st.write("Describe how confident you feel about something, and this app will map your intuition to a probability range.")

user_input = st.text_area("✍️ What do you feel about the event?", placeholder="e.g., It’s very likely to happen...")

if user_input:
    with st.spinner("Analyzing..."):
        result = classifier(user_input, candidate_labels=labels)
        top_label = result['labels'][0]
        top_score = result['scores'][0]
        prob_range = probability_ranges[top_label]
        explanation = label_explanations[top_label]

    st.subheader("🔍 Interpretation")
    st.markdown(f"**Label:** `{top_label}`")
    st.markdown(f"**Probability Range:** `{prob_range}`")
    st.markdown(f"**Meaning:** {explanation}")
    st.markdown(f"**Model Confidence for This Label:** `{round(top_score * 100, 2)}%`")

    st.subheader("📊 Confidence Scores for All Labels")
    chart_data = pd.DataFrame({
        "Label": result["labels"],
        "Confidence": [round(score * 100, 2) for score in result["scores"]]
    }).sort_values("Confidence", ascending=False)

    st.bar_chart(chart_data.set_index("Label"))

    summary_md = f"""### 🧠 Forecast Snapshot  
**Input**: {user_input}  
**Inferred Label**: `{top_label}`  
**Range**: {prob_range}  
**Meaning**: {explanation}  
**Timestamp**: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
    st.markdown(summary_md)

st.markdown("---")