
import streamlit as st
import pandas as pd
import joblib

st.set_page_config(
    page_title="Tourism Experience Analytics",
    layout="wide"
)

st.title("Tourism Experience Analytics")

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Choose Module",
    [
        "Attraction Rating Prediction",
        "Visit Mode Prediction",
        "Personalized Recommendation"
    ]
)

rating_model = joblib.load("tourism_rating_model.pkl")
visit_mode_model = joblib.load("tourism_visit_mode_model.pkl")
user_item_matrix = joblib.load("user_item_matrix.pkl")
item_similarity_df = joblib.load("item_similarity_matrix.pkl")
attraction_info = joblib.load("attraction_info.pkl")


if page == "Attraction Rating Prediction":

    st.header("Attraction Rating Prediction")

    visit_year = st.number_input(
        "Visit Year",
        min_value=2010,
        max_value=2030,
        value=2023
    )

    visit_month = st.selectbox(
        "Visit Month",
        list(range(1, 13))
    )

    visit_mode = st.selectbox(
        "Visit Mode",
        ["Business", "Couples", "Family", "Friends", "Solo"]
    )

    user_continent = st.text_input("User Continent")
    user_region = st.text_input("User Region")
    user_country = st.text_input("User Country")

    attraction_type = st.text_input("Attraction Type")
    attraction_city = st.text_input("Attraction City")
    attraction_country = st.text_input("Attraction Country")

    if st.button("Predict Rating"):

        input_data = pd.DataFrame({
            "VisitYear": [visit_year],
            "VisitMonth": [visit_month],
            "VisitMode_Name": [visit_mode],
            "UserContinent": [user_continent],
            "UserRegion": [user_region],
            "UserCountry": [user_country],
            "AttractionType": [attraction_type],
            "AttractionCityName": [attraction_city],
            "AttractionCountry": [attraction_country]
        })

        prediction = rating_model.predict(input_data)[0]

        st.success(
            f"Predicted Attraction Rating: {prediction:.2f}"
        )


elif page == "Visit Mode Prediction":

    st.header("Visit Mode Prediction")

    visit_year = st.number_input(
        "Visit Year",
        min_value=2010,
        max_value=2030,
        value=2023
    )

    visit_month = st.selectbox(
        "Visit Month",
        list(range(1, 13))
    )

    user_continent = st.text_input("User Continent")
    user_region = st.text_input("User Region")
    user_country = st.text_input("User Country")

    attraction_type = st.text_input("Attraction Type")
    attraction_city = st.text_input("Attraction City")
    attraction_country = st.text_input("Attraction Country")

    if st.button("Predict Visit Mode"):

        input_data = pd.DataFrame({
            "VisitYear": [visit_year],
            "VisitMonth": [visit_month],
            "UserContinent": [user_continent],
            "UserRegion": [user_region],
            "UserCountry": [user_country],
            "AttractionType": [attraction_type],
            "AttractionCityName": [attraction_city],
            "AttractionCountry": [attraction_country]
        })

        prediction = visit_mode_model.predict(input_data)[0]

        st.success(
            f"Predicted Visit Mode: {prediction}"
        )


elif page == "Personalized Recommendation":

    st.header("Personalized Attraction Recommendation")

    user_id = st.selectbox(
        "Select User ID",
        user_item_matrix.index.tolist()
    )

    top_n = st.slider(
        "Number of Recommendations",
        min_value=1,
        max_value=10,
        value=5
    )

    if st.button("Generate Recommendations"):

        user_ratings = user_item_matrix.loc[user_id].dropna()

        scores = {}

        for attraction_id, rating in user_ratings.items():

            similarities = item_similarity_df[attraction_id]

            for similar_id, similarity in similarities.items():

                if similar_id not in user_ratings.index:

                    scores[similar_id] = (
                        scores.get(similar_id, 0)
                        + similarity * rating
                    )

        if scores:

            recommendations = (
                pd.Series(scores)
                .sort_values(ascending=False)
                .head(top_n)
            )

            result = attraction_info.loc[
                recommendations.index
            ].copy()

            result["RecommendationScore"] = recommendations.values

            st.dataframe(
                result.reset_index(),
                use_container_width=True
            )

        else:

            st.warning(
                "No recommendations available for this user."
            )
