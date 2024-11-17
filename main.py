import streamlit as st
import random


wayToWinList = [3, 1, 2, 3]

def showComputerMove():
    if st.session_state['compMove'] == 1:
        st.write("opponent played ✋")
    elif st.session_state['compMove'] == 2:
        st.write("opponent played ✌")
    else:
        st.write("opponent played 👊")

def compare():
    if st.session_state['compMove'] == st.session_state['move']:
        st.write("Draw")
    elif wayToWinList[st.session_state['move'] - 1] == st.session_state['compMove']:
        st.write("Win")
    else:
        st.write("Lose")

if st.button("✋"):
    st.session_state['move'] = 1
if st.button("✌"):
    st.session_state['move'] = 2
if st.button("👊"):
    st.session_state['move'] = 3

if st.button("Play"):
    st.session_state['compMove'] = random.randint(1, 3)
    showComputerMove()
    compare()
