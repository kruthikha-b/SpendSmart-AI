# 💸 SpendSmart AI

🚀 **Your Money. Simplified.**

SpendSmart AI is a smart financial dashboard that helps users track expenses, analyze spending habits, and make better financial decisions using intuitive insights and predictions.

---

## ✨ Features

* 🔐 **User Authentication**

  * Signup & Login system using Firebase
* 📂 **CSV Upload**

  * Upload transaction data easily
* 📊 **Smart Dashboard**

  * Daily & monthly spending insights
* 🎯 **Goal Tracking**

  * Track progress towards financial goals
* 🔮 **Predictions**

  * Estimate future spending
* ☁️ **Cloud Storage**

  * Data stored securely using Firebase Firestore

---

## 🛠️ Tech Stack

* **Frontend & App Framework:** Streamlit
* **Backend / Logic:** Python
* **Database:** Firebase Firestore
* **Data Processing:** Pandas

---

## 📁 Project Structure

```
├── app.py              # Main Streamlit app
├── auth.py             # Authentication logic
├── requirements.txt    # Dependencies
├── database.db         # (local fallback - optional)
└── README.md
```

---

## ⚙️ Setup Instructions (Local)

### 1. Clone the repository

```bash
git clone https://github.com/your-username/spendsmart-ai.git
cd spendsmart-ai
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Add Firebase Key

* Download your Firebase service account JSON
* Place it in the project folder as:

```
firebase_key.json
```

### 4. Run the app

```bash
streamlit run app.py
```

---

## ☁️ Deployment (Streamlit Cloud)

1. Push code to GitHub
2. Go to **Streamlit Cloud**
3. Click **New App → Select repo**
4. Set:

   * Main file: `app.py`
5. Add Firebase key in **Secrets**:

```toml
firebase_key = "PASTE_YOUR_JSON_AS_STRING"
```

6. Deploy 🚀

---

## 📊 Sample CSV Format

Your CSV must have:

```
Date,Description,Amount
2024-03-01,Zomato,250
2024-03-02,Uber,180
```

---

## 🔐 Security Note

* Do NOT upload `firebase_key.json` to GitHub
* Always use **Streamlit secrets** for deployment

---

## 🚀 Future Improvements

* 📈 AI-based expense categorization
* 📊 Advanced visual analytics
* 💡 Personalized financial tips
* 📱 Mobile-friendly UI



## 👩‍💻 Author

**Kruthikha B**
CSE (Data Science) Student | Developer


