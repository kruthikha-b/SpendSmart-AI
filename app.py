

import streamlit as st
import pandas as pd
import time
import matplotlib.pyplot as plt
import json

# Initialize Firebase 
import firebase_admin
from firebase_admin import credentials, firestore




firebase_dict = dict(st.secrets["firebase_key"])

if not firebase_admin._apps:
    cred = credentials.Certificate(firebase_dict)
    firebase_admin.initialize_app(cred)


db = firestore.client()
# ADD USER
def add_user(username, password):
    doc = db.collection("users").document(username).get()

    if doc.exists:
        return False   # user already exists

    db.collection("users").document(username).set({
        "username": username,
        "password": password
    })

    return True
def login_user(username, password):
    doc = db.collection("users").document(username).get()

    if doc.exists:
        user_data = doc.to_dict()

        if user_data["password"] == password:
            return True

    return False

# SAVE TRANSACTIONS
def save_transactions(username, df):

    if not username:
        return  #prevent crash

    data = df.to_dict(orient="records")  #clean format

    db.collection("transactions").document(username).set({
        "data": data
    })

# LOAD TRANSACTIONS
def load_transactions(username):

    if not username:
        return None

    doc = db.collection("transactions").document(username).get()

    if doc.exists:
        data = doc.to_dict()["data"]
        return pd.DataFrame(data)

    return None

# PAGE CONFIG
st.set_page_config(layout="wide")

# GLOBAL CSS 
st.markdown("""
<style>

/* REMOVE DEFAULT HEADER */
header {visibility: hidden;}

/*TOP SPACING */
.block-container {
    padding-top: 2rem;
}

/* BACKGROUND */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #f8fafc, #e0f2fe);
}

/* BUTTON STYLE */
.stButton>button {
    border-radius: 10px;
    padding: 10px 20px;
    border: none;
    background: #1e293b;
    color: white;
    transition: 0.3s;
}

.stButton>button:hover {
    background: #38bdf8;
    color: black;
    transform: scale(1.05);
}

/* NAVBAR CONTAINER STYLE */
section[data-testid="stHorizontalBlock"] {
    background: linear-gradient(90deg, #020617, #0f172a);
    padding: 14px 30px;
    border-radius: 12px;
    margin-bottom: 20px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.25);
}

</style>
""", unsafe_allow_html=True)

if "username" not in st.session_state:
    st.session_state.username = ""
# STATE INIT
if "page" not in st.session_state:
    st.session_state.page = "home"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False



# 🌐 NAVBAR 

nav = st.container()

with nav:
    col1, col2 = st.columns([6,2])  

    # LEFT → LOGO
    with col1:
       st.markdown(
        "<h3 style='color:#64748b; margin:0; font-weight:600;'>💸 SpendSmart AI</h3>",
        unsafe_allow_html=True
    )

    # RIGHT → BUTTONS 
    with col2:
        b1, b2, b3 = st.columns(3, gap="small")  

        with b1:
            if st.button("Home", key="nav_home"):
                st.session_state.page = "home"
                st.rerun()

        with b2:
            if not st.session_state.logged_in:
                if st.button("Login", key="nav_login"):
                    st.session_state.page = "login"
                    st.rerun()

        with b3:
            if not st.session_state.logged_in:
                if st.button("Signup", key="nav_signup"):
                    st.session_state.page = "signup"
                    st.rerun()
            else:
                if st.button("Dashboard", key="nav_dash"):
                    st.session_state.page = "dashboard"
                    st.rerun()

st.divider()
# HOME PAGE
if st.session_state.page == "home":

    st.markdown("<br><br>", unsafe_allow_html=True)

   
    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        st.markdown("""
        <div style='text-align:center;'>

        <h1 style='font-size:52px; margin-bottom:10px;'>💸 SpendSmart AI</h1>

        <h3 style='color:#64748b; font-weight:500;'>
        Your Money. Simplified.
        </h3>

        <p style='color:#475569; font-size:18px; margin-top:20px; line-height:1.6;'>
        Track spending, analyze habits, and make smarter financial decisions.
        </p>

        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br><br>", unsafe_allow_html=True)

        # BUTTONS CENTERED
        b1, b2, b3 = st.columns([1,1,1])

        with b1:
            pass

        with b2:
            if st.button("🚀 Get Started", key="home_start"):
                st.session_state.page = "signup"
                st.rerun()

        with b3:
            if st.button("🔐 Login", key="home_login"):
                st.session_state.page = "login"
                st.rerun()


# 🔐 LOGIN PAGE
elif st.session_state.page == "login":

    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        st.subheader("🔐 Login")

        username = st.text_input("Username")
        password = st.text_input("Password", type="password")


        
        if st.button("Login"):
            if login_user(username, password):
                st.session_state.logged_in = True
                st.session_state.username = username 
                st.success("🎉 Login successful! Redirecting...")

                time.sleep(1)
                st.session_state.page = "dashboard"
                st.rerun()

            else:
                st.error("Invalid credentials")


# 📝 SIGNUP PAGE
elif st.session_state.page == "signup":

    col1, col2, col3 = st.columns([1,2,1])

    with col2:
        st.subheader("📝 Create Account")

        new_user = st.text_input("Username")
        new_pass = st.text_input("Password", type="password")
        if st.button("Signup", key="signup_btn"):
            if add_user(new_user, new_pass):
                st.success("🎉 Account created successfully!")
                st.session_state.page = "login"
                st.rerun()
            else:
                st.error("⚠️ Username already exists")
   


        if st.button("Already have an account? Login"):
            st.session_state.page = "login"
            st.rerun()
# 📊 DASHBOARD
elif st.session_state.page == "dashboard":
    if st.button("🔄 Reset Data"):
        db.collection("transactions").document(user).delete()
        st.success("Data deleted!")
        st.rerun()

    st.markdown(f"### 👋 Welcome back, {st.session_state.username}!")

    # CSS
    st.markdown("""
    <style>
    .card {
        background: linear-gradient(135deg, #1e293b, #0f172a);
        padding: 20px;
        border-radius: 14px;
        color: white;
        text-align: center;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
    }

    .green {background: #065f46;}
    .purple {background: #6d28d9;}
    .blue {background: #1e40af;}
    .red {background: #be123c;}

    div.stButton > button {
        width: 100%;
        margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1 style='text-align:center;'>📊 Financial Dashboard</h1>", unsafe_allow_html=True)

    st.subheader("📂 Upload Transactions")
   
    user = st.session_state.get("username")
    # 🔄 Try loading existing data first
    df = load_transactions(user)

    if df is None:
        st.info("Upload your transactions to get started")

        file = st.file_uploader("Upload CSV", type=["csv"])

        if file:
            df = pd.read_csv(file)

            # 🧹 CLEANING
            df = df.dropna(axis=1, how='all')
            df['Date'] = pd.to_datetime(df['Date']).astype(str)   
            df['Amount'] = pd.to_numeric(df['Amount'])
            df = df.dropna().reset_index(drop=True)

            # 💾 SAVE
            if user:
                save_transactions(user, df)

            st.success("✅ Data uploaded & saved!")
            st.rerun()

    if df is not None:
        # 🏷️ CATEGORY
        def categorize(desc):
            desc = str(desc).lower()

            if any(w in desc for w in ["zomato","swiggy","ubereats","pizza","kfc","burger"]):
                return "Food"
            elif any(w in desc for w in ["uber","ola","rapido","fuel"]):
                return "Transport"
            elif any(w in desc for w in ["amazon","flipkart","myntra"]):
                return "Shopping"
            elif "rent" in desc:
                return "Rent"
            elif any(w in desc for w in ["grocery","zepto","dmart"]):
                return "Groceries"
            elif any(w in desc for w in ["bill","wifi","recharge"]):
                return "Utilities"
            elif any(w in desc for w in ["netflix","spotify","prime"]):
                return "Entertainment"
            else:
                return "Other"

        df["Category"] = df["Description"].apply(categorize)

        # SECTION STATE
        if "section" not in st.session_state:
            st.session_state.section = "overview"

        st.markdown("### 🚀 Explore Insights")

        # NAV BUTTONS
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            if st.button("📊 Overview", key="sec_overview"):
                st.session_state.section = "overview"

        with col2:
            if st.button("💸 Spending", key="sec_spending"):
                st.session_state.section = "spending"

        with col3:
            if st.button("🎯 Goals", key="sec_goals"):
                st.session_state.section = "goals"

        with col4:
            if st.button("🔮 Predictions", key="sec_pred"):
                st.session_state.section = "predictions"

        section = st.session_state.section

        # =========================
        # 📊 OVERVIEW
        # =========================
        if section == "overview":

            total = df["Amount"].sum()

            col1, col2, col3 = st.columns(3)

            with col1:
                st.markdown(f"""
                <div class="card">
                <h4>💸 Total Spending</h4>
                <h2>₹{total:.0f}</h2>
                </div>
                """, unsafe_allow_html=True)

            income = st.number_input("Enter Monthly Income (₹)", min_value=0)

            if income > 0:
                savings = income - total
                percent = (savings / income) * 100

                with col2:
                    st.markdown(f"""
                    <div class="card green">
                    <h4>💰 Balance</h4>
                    <h2>₹{savings:.0f}</h2>
                    </div>
                    """, unsafe_allow_html=True)

                with col3:
                    st.markdown(f"""
                    <div class="card purple">
                    <h4>📊 Savings Rate</h4>
                    <h2>{percent:.1f}%</h2>
                    </div>
                    """, unsafe_allow_html=True)

        # =========================
        # 💸 SPENDING
        # =========================
        elif section == "spending":

            st.subheader("💸 Spending Analysis")

            category_data = df.groupby("Category")["Amount"].sum()

            col1, col2 = st.columns(2)

            with col1:
                fig, ax = plt.subplots()
                ax.pie(category_data, labels=category_data.index, autopct='%1.1f%%')
                st.pyplot(fig)

            with col2:
                fig2, ax2 = plt.subplots()
                category_data.plot(kind='bar', ax=ax2)
                st.pyplot(fig2)

            st.markdown("### 📅 Spending Trend")

            date_data = df.groupby("Date")["Amount"].sum()
            fig3, ax3 = plt.subplots()
            date_data.plot(ax=ax3)
            st.pyplot(fig3)

        # =========================
        # 🎯 GOALS
        # =========================
        elif section == "goals":

            st.subheader("🎯 Savings Goals")

            income = st.number_input("Income (₹)", min_value=0, key="goal_income")
            goal = st.number_input("Goal Amount (₹)", min_value=0)

            total = df["Amount"].sum()
            if income > 0 and goal > 0:
                savings = income - total
                progress = (savings / goal) * 100

                st.progress(min(int(progress), 100))

                st.markdown(f"""
                <div class="card blue">
                <h4>Progress</h4>
                <h2>{progress:.1f}%</h2>
                </div>
                """, unsafe_allow_html=True)

                # 💡 SMART MESSAGES
                if savings < 0:
                    st.error("🚨 You're overspending! Reduce expenses to start saving.")
                
                elif progress < 30:
                    st.warning("⚠️ You're just getting started. Try cutting small daily expenses.")

                elif progress < 70:
                    st.info("👍 Good progress! Stay consistent to reach your goal.")

                elif progress < 100:
                    st.success("🔥 Almost there! Keep going!")

                else:
                    st.success("🎉 Goal achieved! You're doing amazing!")

              

        # =========================
        # 🔮 PREDICTIONS
        # =========================
        elif section == "predictions":

            st.subheader("🔮 Future Predictions")

            num_days = df["Date"].nunique()
            avg = df["Amount"].sum() / num_days
            monthly = avg * 30

            col1, col2 = st.columns(2)

            with col1:
                st.markdown(f"""
                <div class="card red">
                <h4>📊 Daily Avg</h4>
                <h2>₹{avg:.0f}</h2>
                </div>
                """, unsafe_allow_html=True)

            with col2:
                st.markdown(f"""
                <div class="card green">
                <h4>📅 Monthly Estimate</h4>
                <h2>₹{monthly:.0f}</h2>
                </div>
                """, unsafe_allow_html=True)
            # after calculating avg and monthly

            st.markdown("### 💡 Insights")

            if monthly > avg * 30 * 1.2:
                st.error("🚨 Your spending trend is increasing rapidly!")

            elif monthly > avg * 30:
                st.warning("⚠️ Slight increase in spending detected.")

            else:
                st.success("✅ Your spending is stable and under control.")

            # compare with income
            income = st.number_input("Enter Income (₹)", min_value=0, key="pred_income")

            if income > 0:
                if monthly > income:
                    st.error("🚨 You may exceed your income this month!")
                
                elif monthly > income * 0.8:
                    st.warning("⚠️ You're spending close to your limit.")

                else:
                    st.success("💰 You're within budget. Good financial discipline!")
