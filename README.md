# Tourism Experience Analytics

## Project Overview

Tourism Experience Analytics is an end-to-end machine learning project designed to analyze tourist behaviour and provide intelligent predictions and personalized attraction recommendations.

The project combines Regression, Classification, and Recommendation System techniques and integrates them into an interactive Streamlit web application.

## Project Objectives

The project focuses on three major machine learning tasks:

1. **Attraction Rating Prediction**
   - Predicts the rating a tourist may give to an attraction.
   - Final Model: Gradient Boosting Regressor.

2. **Visit Mode Prediction**
   - Predicts the tourist's Visit Mode such as Business, Couples, Family, Friends, or Solo.
   - Final Model: Gradient Boosting Classifier.

3. **Personalized Attraction Recommendation**
   - Recommends attractions based on historical user preferences.
   - Uses Item-Based Collaborative Filtering with Cosine Similarity.

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
- SciPy
- Machine Learning
- Collaborative Filtering
- Streamlit
- Joblib
- Google Colab

## Machine Learning Models

### Regression
- Linear Regression
- Random Forest Regressor
- Gradient Boosting Regressor

### Classification
- Logistic Regression
- Random Forest Classifier
- Gradient Boosting Classifier

### Recommendation System
- Item-Based Collaborative Filtering
- Cosine Similarity

## Final Model Performance

| Task | Final Model | Evaluation Metric | Score |
|---|---|---|---:|
| Rating Prediction | Gradient Boosting Regressor | RMSE | 0.9163 |
| Visit Mode Prediction | Gradient Boosting Classifier | Weighted F1 Score | 0.4164 |
| Recommendation System | Item-Based Collaborative Filtering | RMSE | 1.1487 |

## Streamlit Application

The Streamlit application provides three interactive modules:

- Attraction Rating Prediction
- Visit Mode Prediction
- Personalized Attraction Recommendation

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
