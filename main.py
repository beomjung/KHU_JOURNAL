import streamlit as st

st.logo("./images/logo.jpg",size='large', icon_image='./images/logo.jpg')


st.header("2024 KIISS-APCIM Joint Conference")
st.markdown("""
 * If you have any questions about the conference, please look for staff members with 📇**Staff** written on their name badges.
 * If you suddenly feel unwell or become ill, please look for staff members with 📇 **Staff** written on their name badges.
 
 
""")
st.subheader("🏦Venue Floor Guide")
road_tab1, road_tab2, road_tab3 = st.tabs(["1F", "2F", "3F"])
with road_tab1:
    st.image('./images/1f.png')
with road_tab2:
    st.image('./images/2f.png')
    st.markdown("""
        * ⓵ Coffee and refreshments are ready.
        * ⓶ The main hall is the venue for the opening ceremony and the Korean paper session.
        * ⓶
        
        
        """)
    
with road_tab3:
    st.image('./images/3f.png')
    
    
st.subheader("🍴Restaurant Guide (Pureun Sol)")

st.markdown("""
* There may be a large number of attendees at the conference, so the restaurant could be crowded. Please be mindful!
""")
food_tab1, food_tab2 = st.tabs(["Guidance in Images", "Naver Map"])
with food_tab1:
    st.image('./images/food.png')
with food_tab2:
    st.image('./images/naver.png')
    
st.subheader("🅿️Parking Information (Pureun Sol)")
car_tab1, car_tab2 = st.tabs(["Guidance in Images", "Naver Map"])
with car_tab1:
    st.image('./images/food.png')
with car_tab2:
    st.image('./images/naver.png')


