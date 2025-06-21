# ♻️ GreenScanApp

GreenScan is a smart, ML-powered web app built with **Streamlit** that predicts whether a product is eco-friendly based on its category, stock level, and sustainability score.

This project promotes environmental awareness and responsible consumer choices through automation and intuitive design.

---

## 🌟 Features

- 🔮 **Eco-Friendliness Prediction** using a trained ML model (Random Forest)
- 📊 Visual score feedback with helpful eco tips
- 🧾 Prediction history saved in the session with CSV export
- 📂 Upload CSV for bulk predictions
- 📈 Feature importance chart to explain predictions
- ☁️ Deployed online using **Streamlit Cloud**
- 📱 Mobile-optimized UI with emojis, icons, and soft styling

---

## 🚀 Try it Live

👉 [Click here to open the app](https://your-username-green-scan.streamlit.app/)  
_Replace this link after deployment_

---

## 🧠 How It Works

- The app takes:
  - Product category (e.g., bottle, bag, straw)
  - Current stock level
  - Sustainability score (1 to 10)
- It predicts: ✅ Eco-Friendly or ❌ Not Eco-Friendly
- Built using:  
  `pandas`, `scikit-learn`, `matplotlib`, `streamlit`

---

## 🗂 Project Files

| File                      | Purpose                                |
|---------------------------|----------------------------------------|
| `greenscan_app_full.py`   | Main Streamlit app                     |
| `greenscan_model.pkl`     | Trained Random Forest model            |
| `category_encoder.pkl`    | Label encoder for category values      |
| `requirements.txt`        | Packages needed for deployment         |
| `README.md`               | Project overview and documentation     |

---

## 📦 Setup & Run (Local)

```bash
pip install -r requirements.txt
streamlit run greenscan_app_full.py
## 🙌 Credits

This project was created as part of an academic submission.

