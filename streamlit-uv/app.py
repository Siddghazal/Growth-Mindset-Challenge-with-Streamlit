import streamlit as st

st.title(" Growth Mindset Challenge🌱")

st.header("🚀 welcome to your Grouth Journey!")
st.write("Embrace challenges, learn from mistake, and unlock ypur full potential!")

st.header("💡Today's Grouth Mindset Quote")
st.write("Success is not an accident, success is a choice. — Stephen Curry")

st.header("🏆 What is your challenge today? ")
user_input = st.text_input("Describe a challenge you are facing:")


# condition
if user_input:
    st.success(f"💪You are facing: {user_input}. Keep pushing forwards towords your goal!🚀 ")

else:
    st.warning("tell us about your challenge to get started!")    

 # reflexing
st.header("Reflect on your Learning")
reflection = st.text_area("write your reflections here")

if reflection:
    st.success(f"✨Great Insight! Your reflection:{reflection}")

else:
    st.info("Reflecting on past experience help you grow! Share your difficulties")

 # acheivements   

st.header("🏆 Celebrate Your Wins!")
acheivment = st.text_input("Share something you have recently accomplished:")

if acheivment:
    st.success(f"🏅Amazing! you achieved:{acheivment}")

else:
    st.info("big or small,every acheivment counts! share one now 😊 ")

 # footer

st.write("---")
st.write("🚀 Keep believing in yourself.Grouth is a journey ,not a destination!⭐")
st.write("**✍️ Made with ❤️ by Ghazala Siddiqui**")