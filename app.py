import streamlit as st
import numpy as np
import pickle

# Load models
price_model = pickle.load(open("best_price_model.pkl", "rb"))
cluster_model = pickle.load(open("kmeans_model.pkl", "rb"))
cluster_scaler = pickle.load(open("cluster_scaler.pkl", "rb"))

st.set_page_config(page_title="Diamond Dynamics", layout="centered")

st.title("💎 Diamond Dynamics")
st.subheader("Price Prediction & Market Segmentation")

st.write("Enter the diamond details below")

# ---------------------------
# USER INPUTS
# ---------------------------

carat = st.number_input("Carat", min_value=0.1, max_value=5.0, step=0.01)

cut = st.selectbox(
    "Cut",
    ["Fair", "Good", "Very Good", "Premium", "Ideal"]
)

color = st.selectbox(
    "Color",
    ["J","I","H","G","F","E","D"]
)

clarity = st.selectbox(
    "Clarity",
    ["I1","SI2","SI1","VS2","VS1","VVS2","VVS1","IF"]
)

depth = st.number_input("Depth", min_value=40.0, max_value=80.0)

table = st.number_input("Table", min_value=40.0, max_value=100.0)

x = st.number_input("Length (x mm)", min_value=0.1)
y = st.number_input("Width (y mm)", min_value=0.1)
z = st.number_input("Depth (z mm)", min_value=0.1)

# ---------------------------
# ENCODING
# ---------------------------

cut_map = {"Fair":0,"Good":1,"Very Good":2,"Premium":3,"Ideal":4}
color_map = {"J":0,"I":1,"H":2,"G":3,"F":4,"E":5,"D":6}
clarity_map = {"I1":0,"SI2":1,"SI1":2,"VS2":3,"VS1":4,"VVS2":5,"VVS1":6,"IF":7}

cut_encoded = cut_map[cut]
color_encoded = color_map[color]
clarity_encoded = clarity_map[clarity]

# ---------------------------
# FEATURE ENGINEERING
# ---------------------------

volume = x * y * z
dimension_ratio = (x + y) / (2 * z)

if carat < 0.5:
    carat_category = 0
elif carat <= 1.5:
    carat_category = 1
else:
    carat_category = 2

features = np.array([[carat, cut_encoded, color_encoded, clarity_encoded,
                      depth, table, x, y, z,
                      volume, dimension_ratio, carat_category]])

# ---------------------------
# PRICE PREDICTION
# ---------------------------

if st.button("Predict Price 💰"):

    price_prediction = price_model.predict(features)

    st.success(f"Predicted Diamond Price (INR): ₹{int(np.exp(price_prediction[0]))}")

# ---------------------------
# CLUSTER PREDICTION
# ---------------------------

if st.button("Predict Market Segment 📊"):

    scaled_features = cluster_scaler.transform(features)

    cluster = cluster_model.predict(scaled_features)[0]

    cluster_names = {
        0: "Premium Heavy Diamonds 💎",
        1: "Affordable Small Diamonds 💰",
        2: "Mid-range Balanced Diamonds ⭐"
    }

    st.success(f"Cluster: {cluster}")
    st.write("Market Segment:", cluster_names[cluster])