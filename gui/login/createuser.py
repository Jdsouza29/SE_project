import streamlit as st
from datetime import date
from gui.usermain.main import *
import re

passpat = re.compile("^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$")
phonepat = re.compile("^(\+91[\-\s]?)?[0]?(91)?[789]\d{9}$")
emailpat = re.compile(
    "^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9_\-\.]+)\.([a-zA-Z]{2,5})$")


def change(uname, upass, name, dob, phone, mail, gender):
    print("why")
    if uname == '' or upass == '' or name == '' or dob == '' or phone == '' or mail == '' or gender == '':
        st.error("All fields should filled")
        st.session['new'] == 0
    else:
        try:
            add_(uname, upass, name, dob, phone, mail, gender)
            st.session_state['new'] = 1
            # st.info("Your account has been created")
            # user_main()
        except Exception as e:
            st.info("Enter a valid phone number")


def CreateUser():
    if 'new' not in st.session_state:
        st.session_state['new'] = 0
        st.title("Create_User")
        col1, col2 = st.columns(2)
        with col1:
            uname = st.text_input("Enter Username")
            upass = st.text_input("Enter password", type="password")
            againupass = st.text_input("Enter password again", type="password")
            name = st.text_input("Enter your name")
        with col2:
            dob = st.date_input("DateOfBirth", date(
                2002, 1, 1), date(1950, 1, 1), date(2004, 1, 1))
            phone = st.text_input("Enter your phone number:")
            mail = st.text_input("Enter our mail:")
            gender = st.radio("Gender", ["Male", "Female"])
        if upass != againupass:
            st.info("Re-entered password doesn't match with password")

        if st.button("Create"):
            change(uname, upass, name, dob, phone, mail, gender)
        if st.button("go back to login"):
            st.experimental_rerun()
            del st.session_state['new']
            st.experimental_rerun()
            del st.session_state['log']
            st.experimental_rerun()
    else:
        if st.session_state['new'] == 1:
            user_main()
        elif st.session_state['new'] == 0:
            st.session_state['new'] = 0
            st.title("Create_User")
            col1, col2 = st.columns(2)
            with col1:
                uname = st.text_input("Enter Username")
                upass = st.text_input("Enter password", type="password")
                againupass = st.text_input(
                    "Enter password again", type="password")
                name = st.text_input("Enter your name")
            with col2:
                dob = st.date_input("DateOfBirth", date(
                    2002, 1, 1), date(1950, 1, 1), date(2004, 1, 1))
                phone = st.text_input("Enter your phone number:")
                mail = st.text_input("Enter our mail:")
                gender = st.radio("Gender", ["Male", "Female"])
            if not passpat.match(upass):
                st.error(
                    "password should be min 8 character long with min 1 digit")
            elif not phonepat.match(phone):
                st.error("Enter valid phone number")
            elif not emailpat.match(mail):
                st.error("Enter valid mail")
            else:
                if upass != againupass:
                    st.info("Re-entered password doesn't match with password")
                if st.button("Create"):
                    change(uname, upass, name, dob, phone, mail, gender)
            if st.button("go back to login"):
                del st.session_state['new']
                del st.session_state['log']
