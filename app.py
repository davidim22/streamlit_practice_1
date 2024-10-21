import streamlit as st

# streamlit run app.py
st.title("Streamlit Demo")

st.header(" Heading of Streamlit ")

st.subheader("  Subheading of Streamlit ")
st.text("This is an Example Text")

st.warning("Warning")
st.success("Success")
st.info("Information")
st.error("Error")

if st.checkbox("Select/Unselect"):
    st.text("User selected the checkbox")
else:
    st.text("User has not selected the checkbox")

state = st.radio("What is your favorite color?",
                 ("Red", "Green", "Yello"))

if state == 'Green':
    st.success("That is my favorite color as well")

occupation = st.selectbox("What do you do?",
                          ["Student","Vlogger","Engineer"])

st.text(f"Selected option is {occupation}")

if st.button("Example Button"):
    st.error("You clicked it")

st.sidebar.header("Heading of sidebar")
st.sidebar.text("This is a sidebar")