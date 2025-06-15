import streamlit as st
from langchain_helper import generate_restaurant_name_and_items

# Premium UI setup
st.set_page_config(page_title="AI Restaurant Name & Menu Generator", layout="centered")

st.title("🍽️ AI-Powered Restaurant Generator")
st.markdown("Generate unique restaurant names and delicious menu items based on any cuisine.")

# User input method: Dropdown or Text
st.sidebar.header("Cuisine Options")

input_method = st.sidebar.radio("Choose how to enter a cuisine:", ("Select from list", "Type your own"))

# Predefined cuisine list
cuisine_list = [
    "Indian", "Mexican", "Chinese", "Italian", "Thai", "Japanese",
    "French", "Greek", "Korean", "Vietnamese", "Spanish", "Turkish",
    "American", "Lebanese", "Ethiopian", "Brazilian", "Caribbean"
]

# Choose cuisine
if input_method == "Select from list":
    cuisine = st.sidebar.selectbox("Choose a cuisine", cuisine_list)
else:
    cuisine = st.sidebar.text_input("Enter your own cuisine")

# Generate results
if cuisine:
    try:
        with st.spinner("Generating a perfect name and menu..."):
            response = generate_restaurant_name_and_items(cuisine=cuisine)
        st.success("Here’s what we cooked up!")

        st.subheader("🏪 Restaurant Name")
        st.markdown(f"### {response['resturant_name']}")

        st.subheader("🍴 Menu Items")
        menu_items = [item.strip() for item in response['menu_items'].split(",")]
        for item in menu_items:
            st.write(f"- {item}")

    except Exception as e:
        st.error("Something went wrong while generating. Please try again.")
        st.exception(e)
else:
    st.info("Please select or type a cuisine to get started.")
