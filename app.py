import streamlit as st
from PIL import Image
import joblib

def main():
    st.title("Fake news :sunglasses:")
    image = Image.open('trump.png')
    st.image(image, caption='Make America great again',width=400)
    newmodel = joblib.load('fakenews.pkl')

    x1=st.text_input(label='Inserisci qui il testo:')
    pred = newmodel.predict([x1])
    st.write( "è una fake news? 0=FAKE 1=TRUE ", pred) #non funziona :(








if __name__ == "__main__":
    main()