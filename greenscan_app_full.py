import streamlit as st
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import datetime
import random
import io

# Load model and encoder
with open("greenscan_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("category_encoder.pkl", "rb") as f:
    encoder = pickle.load(f)

# Category options
categories = encoder.classes_.tolist()

# Initialize session history
if "history" not in st.session_state:
    st.session_state.history = []

# Title and logo
st.image("https://i.imgur.com/zMZ4iPi.png", use_column_width=True)
st.title("♻️ GreenScan - Eco-Friendliness Predictor")

# Tabs for Prediction and Advanced Tools
tab1, tab2 = st.tabs(["🔮 Prediction", "⚙️ Advanced Tools"])

with tab1:
    # Columns layout for inputs
    col1, col2 = st.columns(2)
    category = col1.selectbox("Select Product Category", categories)
    stock = col2.number_input("Enter Stock Quantity", min_value=0, max_value=500, value=50)
    score = st.slider("Sustainability Score (1 to 10)", 1, 10, 5)

    expiry = st.date_input("📅 Product Expiry Date")
    if expiry < datetime.date.today() + datetime.timedelta(days=30):
        st.error("⚠️ This product is expiring soon!")

    if st.button("Predict"):
        encoded_category = encoder.transform([category])[0]
        input_data = pd.DataFrame([[encoded_category, stock, score]],
                                  columns=["Category_encoded", "Stock", "Sustainability_Score"])
        prediction = model.predict(input_data)[0]

        result_text = "✅ Eco-Friendly" if prediction == 1 else "⚠️ Not Eco-Friendly"
        color = "green" if prediction == 1 else "orange"
        st.markdown(f"### Prediction Result:\n<span style='color:{color}'>{result_text}</span>", unsafe_allow_html=True)

        # Save to history
        st.session_state.history.append({
            "Category": category,
            "Stock": stock,
            "Score": score,
            "Result": "Eco-Friendly" if prediction == 1 else "Not Eco-Friendly"
        })

        # Chart for score
        with st.expander("📊 Sustainability Score Visualization"):
            fig, ax = plt.subplots()
            ax.bar(["Score"], [score], color='green' if prediction else 'red')
            ax.set_ylim(0, 10)
            st.pyplot(fig)

        # Random eco tip
        tips = [
            "Switch to reusable bottles.",
            "Avoid single-use plastic.",
            "Compost organic waste.",
            "Buy in bulk to reduce packaging waste."
        ]
        if prediction == 0:
            st.info("💡 Green Tip: " + random.choice(tips))

with tab2:
    # Feature importance
    with st.expander("🔍 Show Feature Importance"):
        importances = model.feature_importances_
        importance_df = pd.DataFrame({
            "Feature": ["Category", "Stock", "Sustainability Score"],
            "Importance": importances
        })
        st.bar_chart(importance_df.set_index("Feature"))

    # Upload CSV and bulk prediction
    with st.expander("📁 Bulk Prediction via CSV Upload"):
        uploaded_file = st.file_uploader("📂 Upload product data (.csv)")
        if uploaded_file:
            df_uploaded = pd.read_csv(uploaded_file)
            df_uploaded["Category_encoded"] = encoder.transform(df_uploaded["Category"])
            X_new = df_uploaded[["Category_encoded", "Stock", "Sustainability_Score"]]
            df_uploaded["Prediction"] = model.predict(X_new)
            df_uploaded["Prediction"] = df_uploaded["Prediction"].apply(lambda x: "Eco-Friendly" if x == 1 else "Not Eco-Friendly")
            st.dataframe(df_uploaded)

    # Show prediction history
    if st.session_state.history:
        with st.expander("🧾 Prediction History (Session)"):
            hist_df = pd.DataFrame(st.session_state.history)
            st.dataframe(hist_df, use_container_width=True)

            # Download button
            csv = hist_df.to_csv(index=False)
            st.download_button("📥 Download History as CSV", csv, "greenscan_results.csv", "text/csv")
