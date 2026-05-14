
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Breast Cancer Tumor Classification",
    page_icon="🩺",
    layout="wide"
)

# =====================================================
# LOAD MODEL FILES
# =====================================================

model = joblib.load("breast_cancer_model.pkl")
selector = joblib.load("selector.pkl")
scaler = joblib.load("scaler.pkl")

# =====================================================
# SIDEBAR
# =====================================================

st.sidebar.title("🩺 About Project")

st.sidebar.info(
    """
    This application predicts whether a breast tumor is:

    - Benign
    - Malignant

    using Machine Learning techniques.
    """
)

st.sidebar.success("Model Used: Logistic Regression")

# =====================================================
# TITLE
# =====================================================

st.title("🩺 Breast Cancer Tumor Classification")

st.markdown("### Upload a CSV file containing tumor feature values for prediction")

# =====================================================
# FILE UPLOADER
# =====================================================

uploaded_file = st.file_uploader("📂 Upload CSV File", type=["csv"])

# =====================================================
# INSTRUCTIONS
# =====================================================

with st.expander("📘 Instructions"):
    st.write("""
    1. Upload a CSV file  
    2. System will preprocess automatically  
    3. View predictions and graphs below  
    """)

# =====================================================
# MAIN LOGIC
# =====================================================

if uploaded_file is not None:

    try:
        # Read file
        data = pd.read_csv(uploaded_file)

        # Drop unwanted columns
        data.drop(
            columns=["Unnamed: 32", "id", "diagnosis"],
            inplace=True,
            errors="ignore"
        )

        st.subheader("📄 Uploaded Data")
        st.dataframe(data)

        # =====================================================
        # PREPROCESSING
        # =====================================================

        scaled_data = scaler.transform(data)
        selected_data = selector.transform(scaled_data)

        # =====================================================
        # PREDICTION
        # =====================================================

        prediction = model.predict(selected_data)
        probabilities = model.predict_proba(selected_data)

        result_data = data.copy()

        result_data["Prediction"] = prediction
        result_data["Prediction"] = result_data["Prediction"].map({
            0: "Benign",
            1: "Malignant"
        })

        result_data["Benign Probability"] = probabilities[:, 0]
        result_data["Malignant Probability"] = probabilities[:, 1]

        # =====================================================
        # RESULTS
        # =====================================================

        st.subheader("🔍 Prediction Results")
        st.dataframe(result_data)

        # =====================================================
        # SUMMARY
        # =====================================================

        summary = result_data["Prediction"].value_counts()

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Benign Cases", summary.get("Benign", 0))

        with col2:
            st.metric("Malignant Cases", summary.get("Malignant", 0))

        # =====================================================
        # BAR CHART (SMALL)
        # =====================================================

        st.subheader("📈 Prediction Distribution")

        fig, ax = plt.subplots(figsize=(3.5, 2.5))  # 👈 SMALL SIZE

        summary.plot(kind="bar", ax=ax)

        ax.set_xlabel("Class")
        ax.set_ylabel("Count")
        ax.set_title("Prediction Counts")

        col1, col2, col3 = st.columns(3)
        with col2:
            st.pyplot(fig, use_container_width=False)

        # =====================================================
        # PIE CHART (SMALL)
        # =====================================================

        st.subheader("🥧 Prediction Percentage")

        fig2, ax2 = plt.subplots(figsize=(3.5, 3.5))  # 👈 SMALL SIZE

        ax2.pie(
            summary,
            labels=summary.index,
            autopct='%1.1f%%'
        )

        ax2.set_title("Prediction Percentage")

        col1, col2, col3 = st.columns(3)
        with col2:
            st.pyplot(fig2, use_container_width=False)

        # =====================================================
        # DOWNLOAD
        # =====================================================

        csv = result_data.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="⬇ Download Prediction Results",
            data=csv,
            file_name="prediction_results.csv",
            mime="text/csv"
        )

        st.success("✅ Prediction Completed Successfully!")

    except Exception as e:
        st.error(f"❌ Error: {e}")
