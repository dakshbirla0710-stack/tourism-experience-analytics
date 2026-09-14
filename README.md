# Tourism Experience Analytics

## Project Overview

Tourism Experience Analytics is an end-to-end Machine Learning project designed to analyze tourist behaviour, predict tourism experiences, classify visitor behaviour, and generate personalized attraction recommendations.

The project combines Data Cleaning, Exploratory Data Analysis, Statistical Analysis, Regression, Classification, Recommendation Systems, and Streamlit deployment into a complete tourism analytics solution.

The final application provides three major functionalities:

- Attraction Rating Prediction
- Visit Mode Prediction
- Personalized Attraction Recommendations

---

## Project Objectives

The project focuses on three major Machine Learning tasks.

### 1. Attraction Rating Prediction

The regression system predicts the expected rating a tourist may give to an attraction based on tourism-related information such as visit period, visit mode, user geographical information, and attraction characteristics.

Models evaluated:

- Linear Regression
- Random Forest Regressor
- Gradient Boosting Regressor

**Final Regression Model:** Gradient Boosting Regressor

---

### 2. Visit Mode Prediction

The classification system predicts the tourist's Visit Mode.

Possible Visit Modes include:

- Business
- Couples
- Family
- Friends
- Solo

Models evaluated:

- Logistic Regression
- Random Forest Classifier
- Gradient Boosting Classifier

**Final Classification Model:** Gradient Boosting Classifier

---

### 3. Personalized Attraction Recommendation

The recommendation system generates personalized tourist attraction suggestions using historical user-attraction interactions.

The system uses:

- User-Item Interaction Matrix
- Item-Based Collaborative Filtering
- Cosine Similarity
- Recommendation Score Ranking

Already visited attractions are excluded and the highest-ranked unseen attractions are recommended to the user.

---

## Dataset

The tourism dataset contains historical tourist transactions along with information about users, attractions, geographical locations, attraction types, and visit modes.

The original dataset consists of multiple relational tables:

- Transaction
- User
- Item
- City
- Country
- Region
- Continent
- Type
- Mode

These tables were cleaned and integrated to create a consolidated dataset for analysis and Machine Learning.

---

## Project Workflow

The project follows the workflow below:

1. Data Collection and Understanding
2. Data Cleaning
3. Missing Value Treatment
4. Data Integration
5. Exploratory Data Analysis
6. Statistical Hypothesis Testing
7. Feature Engineering
8. Categorical Encoding
9. Feature Selection
10. Data Transformation and Scaling
11. Train-Test Splitting
12. Regression Modeling
13. Classification Modeling
14. Recommendation System Development
15. Model Evaluation and Comparison
16. Business Insights and Recommendations
17. Streamlit Application Development
18. Streamlit Community Cloud Deployment

---

## Exploratory Data Analysis

Exploratory Data Analysis was performed to understand tourism patterns and relationships in the dataset.

Major analyses included:

- Distribution of Visit Modes
- Distribution of Attraction Ratings
- Most Visited Tourist Attractions
- Average Attraction Rating by Visit Mode
- Most Popular Attraction Types
- Tourism Visits by Year
- Monthly Tourism Visit Trends
- Most Visited Countries
- Average Rating by Attraction Type
- Visit Mode vs Attraction Type
- Top User Countries by Number of Visits
- Rating Distribution by Visit Mode
- Average Rating of Popular Attractions
- Correlation Analysis
- Pair Plot Analysis

---

## Statistical Analysis

Statistical hypothesis testing was performed to examine important relationships within the tourism dataset.

The tests investigated:

- Whether attraction ratings differ across Visit Modes
- Whether Visit Mode and Attraction Type are associated
- Whether Attraction Type has a significant effect on tourist ratings

Statistical techniques included:

- One-Way ANOVA
- Chi-Square Test of Independence

---

## Machine Learning Models

### Regression Models

The following regression models were evaluated for Attraction Rating Prediction:

- Linear Regression
- Random Forest Regressor
- Gradient Boosting Regressor

The Gradient Boosting Regressor was selected as the final regression model.

### Classification Models

The following classification models were evaluated for Visit Mode Prediction:

- Logistic Regression
- Random Forest Classifier
- Gradient Boosting Classifier

The Gradient Boosting Classifier was selected as the final classification model.

---

## Final Model Performance

| Task | Final Model | Main Evaluation Metric | Score |
|---|---|---|---:|
| Attraction Rating Prediction | Gradient Boosting Regressor | RMSE | 0.9163 |
| Visit Mode Prediction | Gradient Boosting Classifier | Weighted F1 Score | 0.4164 |
| Personalized Recommendation | Item-Based Collaborative Filtering | RMSE | 1.1487 |

The Gradient Boosting Regressor achieved an R² score of approximately 0.1085 during the evaluated tuned configuration.

The original Gradient Boosting Classifier achieved approximately 0.4802 test accuracy and 0.4164 weighted F1-score. Hyperparameter tuning did not improve its performance, so the original model was retained.

The recommendation system achieved an RMSE of approximately 1.1487 across 19,679 evaluated ratings.

---

## Recommendation System

The personalized recommendation engine uses Item-Based Collaborative Filtering.

A User-Item Interaction Matrix is created using historical attraction ratings. Cosine similarity is then calculated between attractions based on user rating patterns.

For a selected user, the system:

1. Identifies attractions previously rated by the user.
2. Finds similar attractions using cosine similarity.
3. Calculates recommendation scores.
4. Excludes attractions already visited by the user.
5. Ranks unseen attractions.
6. Returns the top recommended tourist attractions.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- SciPy
- Matplotlib
- Seaborn
- Joblib
- Collaborative Filtering
- Cosine Similarity
- Streamlit
- Google Colab
- GitHub
- Streamlit Community Cloud

---

## Streamlit Application

An interactive Streamlit web application was developed to make the Machine Learning models and recommendation system accessible through a simple user interface.

The application contains three modules.

### Attraction Rating Prediction

Users can enter tourism-related information and obtain the predicted attraction rating from the trained regression model.

### Visit Mode Prediction

Users can provide tourist and attraction information and obtain the predicted Visit Mode from the trained classification model.

### Personalized Attraction Recommendation

Users can select a User ID and generate ranked personalized attraction recommendations using the collaborative filtering recommendation engine.

---

## Live Application

The Tourism Experience Analytics application is deployed using Streamlit Community Cloud.

**Live Application:**

https://tourism-experience-analytics-daksh.streamlit.app

The deployed application provides:

- Attraction Rating Prediction
- Visit Mode Prediction
- Personalized Attraction Recommendations

---

## Project Structure

```text
tourism-experience-analytics/
│
├── app.py
├── requirements.txt
├── tourism_rating_model.pkl
├── tourism_visit_mode_model.pkl
├── user_item_matrix.pkl
├── item_similarity_matrix.pkl
├── attraction_info.pkl
└── README.md

## Author

**Daksh Birla**

Tourism Experience Analytics  
Machine Learning Capstone Project
