import streamlit as st
from omr_processor import evaluate_omr
import json
import cv2
import pandas as pd
import numpy as np
from PIL import Image
import os
import json

template_path = os.path.join(os.path.dirname(__file__), "templates", "template.json")
with open(template_path) as f:
    template = json.load(f)

# Load template and answer key
with open("templates/template.json") as f:
    template = json.load(f)

answer_key = ["B","B","B","B","B"]
 # for demo, all B. Replace with real key

st.title("Automated OMR Evaluation & Scoring System")

uploaded_files = st.file_uploader("Upload OMR sheets", accept_multiple_files=True, type=["jpg","png","jpeg"])

result = evaluate_omr("dummy_omr.jpg", answer_key, template)

if uploaded_files:
    results = []
    for file in uploaded_files:
        with open(file.name, "wb") as f:
            f.write(file.getbuffer())

        result = evaluate_omr(file.name, answer_key, template)

        # show overlay
        overlay_rgb = cv2.cvtColor(result["overlay"], cv2.COLOR_BGR2RGB)
        st.image(overlay_rgb, caption=f"{file.name} - Overlay")

        # show scores
        st.write("Per-subject scores:", result["subject_scores"])
        st.write("Total score:", result["total_score"])

        results.append({
            "file": file.name,
            **result["subject_scores"],
            "total_score": result["total_score"]
        })

    # export CSV
    df = pd.DataFrame(results)
    csv = df.to_csv(index=False)
    st.download_button("Download Results CSV", data=csv, file_name="omr_results.csv")
