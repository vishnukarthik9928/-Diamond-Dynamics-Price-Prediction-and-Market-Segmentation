# 💎 Diamond Dynamics: Price Prediction & Market Segmentation

## 📌 Project Overview

The **Diamond Dynamics Project** aims to build a machine learning system that can:

1. **Predict the price of a diamond** based on its physical and quality attributes.
2. **Segment diamonds into market categories** using clustering techniques.

The project uses **multiple regression models, an Artificial Neural Network (ANN), and K-Means clustering** to analyze and categorize diamonds effectively.

This system can assist **retailers, e-commerce platforms, and buyers** in making data-driven decisions about diamond pricing and inventory categorization.

---

# 🎯 Objectives

* Predict diamond prices using **machine learning regression algorithms**
* Compare performance of **multiple models**
* Build an **Artificial Neural Network (ANN)** for price prediction
* Perform **diamond market segmentation using clustering**
* Visualize clusters using **Principal Component Analysis (PCA)**
* Deploy a **Streamlit web application** for real-time predictions

---

# 🧠 Skills Demonstrated

* Data Cleaning & Preprocessing
* Exploratory Data Analysis (EDA)
* Feature Engineering
* Outlier Detection & Skewness Handling
* Regression Modeling
* Artificial Neural Networks (ANN)
* K-Means Clustering
* Dimensionality Reduction (PCA)
* Model Evaluation & Comparison
* Streamlit Web App Development

---

# 📊 Dataset Information

**Dataset Source:** Diamonds Dataset

**Total Records:** 53,940

### Features

| Feature | Description            |
| ------- | ---------------------- |
| carat   | Weight of the diamond  |
| cut     | Quality of diamond cut |
| color   | Diamond color grading  |
| clarity | Internal diamond flaws |
| depth   | Total depth percentage |
| table   | Width of top facet     |
| price   | Price in USD           |
| x       | Length (mm)            |
| y       | Width (mm)             |
| z       | Depth (mm)             |

Target variable:

```
price → converted to price_inr
```

---

# ⚙️ Data Preprocessing

The following preprocessing steps were applied:

### Data Cleaning

* Removed invalid zero values in `x`, `y`, `z`
* Handled missing values
* Converted price from **USD → INR**

### Outlier Handling

* Used **IQR method** to remove extreme values

### Skewness Treatment

* Applied **log transformation** to skewed features

---

# 📈 Exploratory Data Analysis (EDA)

Visualizations performed:

* Distribution plots
* Count plots for categorical features
* Boxplots of price vs features
* Correlation heatmap
* Pairplot relationships

Libraries used:

```
Matplotlib
Seaborn
```

---

# ⚡ Feature Engineering

New features created:

```
Volume = x * y * z
Price per carat = price / carat
Dimension ratio = (x + y) / (2 * z)
Carat category:
    Light (<0.5)
    Medium (0.5 - 1.5)
    Heavy (>1.5)
```

These features improved model performance.

---

# 🤖 Machine Learning Models

The following regression models were implemented:

1. Linear Regression
2. Decision Tree Regressor
3. Random Forest Regressor
4. K-Nearest Neighbors (KNN)
5. XGBoost Regressor

Additionally:

### Artificial Neural Network (ANN)

Built using **TensorFlow / Keras**

Architecture:

```
Input Layer
Dense Layer (128 neurons)
Dense Layer (64 neurons)
Output Layer
```

Activation Function:

```
ReLU
```

Optimizer:

```
Adam
```

Loss Function:

```
Mean Squared Error
```

---

# 📊 Model Evaluation

Models were evaluated using:

* **MAE (Mean Absolute Error)**
* **MSE (Mean Squared Error)**
* **RMSE (Root Mean Squared Error)**
* **R² Score**

The best performing model was saved as:

```
best_price_model.pkl
```

---

# 🔍 Market Segmentation (Clustering)

Diamonds were grouped using:

### K-Means Clustering

To determine the optimal number of clusters:

* **Elbow Method**
* **Silhouette Score**

### Cluster Visualization

Dimensionality reduction using:

```
PCA (Principal Component Analysis)
```

Clusters were visualized in **2D space**.

---

# 🏷 Cluster Categories

Clusters were labeled based on diamond characteristics:

| Cluster | Category                    |
| ------- | --------------------------- |
| 0       | Premium Heavy Diamonds      |
| 1       | Affordable Small Diamonds   |
| 2       | Mid-range Balanced Diamonds |

---

# 🖥 Streamlit Web Application

The project includes an interactive **Streamlit application**.

### Features

#### 💰 Price Prediction

User inputs:

* carat
* cut
* color
* clarity
* depth
* table
* x
* y
* z

Output:

```
Predicted Diamond Price (INR)
```

---

#### 📊 Market Segment Prediction

Predicts the diamond cluster category:

Example output:

```
Premium Heavy Diamonds
Affordable Small Diamonds
Mid-range Balanced Diamonds
```

---

# 📁 Project Structure

```
Diamond_Dynamics_Project
│
├── diamonds.csv
├── diamond_project.ipynb
├── app.py
├── best_price_model.pkl
├── kmeans_model.pkl
├── cluster_scaler.pkl
└── README.md
```

---

# 🛠 Technologies Used

Programming Language

```
Python
```

Libraries

```
Pandas
NumPy
Matplotlib
Seaborn
Scikit-Learn
XGBoost
TensorFlow / Keras
Streamlit
```

Development Tools

```
Google Colab
VS Code
GitHub
```

---

# ▶ How to Run the Project

### 1️⃣ Install dependencies

```
pip install pandas numpy matplotlib seaborn scikit-learn xgboost tensorflow streamlit
```

---

### 2️⃣ Run Streamlit Application

```
streamlit run app.py
```

Then open:

```
http://localhost:8501
```

---

# 🌍 Real-World Applications

* Diamond pricing prediction for retailers
* Inventory segmentation
* Luxury product recommendation systems
* E-commerce dynamic pricing
* Customer segmentation

---

# 👨‍💻 Author

**Vishnu Karthik**

Data Science Project
Diamond Dynamics: Price Prediction & Market Segmentation

---

# ⭐ Acknowledgements

This project was developed as part of a **Data Science learning program** focusing on:

* Machine Learning
* Deep Learning
* Data Visualization
* Model Deployment

---
