import streamlit as st
from pathlib import Path

MAIN_DIR = Path(__file__).parent
ADAMLAR_FAYLI = MAIN_DIR / 'adamlar.txt'

st.title('Hello')

st.markdown('necesen')

ad = st.text_input("Adinizi daxil edin")
yash = st.number_input(
    "Yasinizi daxil edin",
    min_value = 0,
    max_value = 100
    
)   

sherler = st.selectbox("Doguldugunuz seher?",["Baki", "Shemkir", "Gence"]
)

def adami_save_et(*args):
    adamin_melumatlari = " - ".join(args)
    with open(ADAMLAR_FAYLI, mode='a') as f:
        f.write(f"{adamin_melumatlari}\n")

if st.button('yadda  saxla'):
    adami_save_et(ad, str(yash), sherler)

