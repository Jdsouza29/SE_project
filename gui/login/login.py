import streamlit as st
# from user import login
# Third change in april
from controller import *

headerSection = st.container()
mainSection = st.container()
loginSection = st.container()
logOutSection = st.container()



def login_Main():
    login()


class login():

    def show_main_page(self):
        with mainSection:
            dataFile = st.text_input("Enter your Test file name: ")
            Topics = st.text_input("Enter your Model Name: ")
            ModelVersion = st.text_input("Enter your Model Version: ")
            processingClicked = st.button ("Start Processing", key="processing")
            if processingClicked:
                st.balloons() 
    
    def LoggedOut_Clicked(self):
        st.session_state['loggedIn'] = False
        
    def show_logout_page(self):
        loginSection.empty();
        with logOutSection:
            st.button ("Log Out", key="logout", on_click=self.LoggedOut_Clicked)
        
    def LoggedIn_Clicked(self,userName, password):
        if (userName - password):
            st.session_state['loggedIn'] = True
        else:
            st.session_state['loggedIn'] = False
            st.error("Invalid user name or password")
        
    def show_login_page(self):
        with loginSection:
            if st.session_state['loggedIn'] == False:
                userName = st.text_input (label="", value="", placeholder="Enter your user name")
                password = st.text_input (label="", value="",placeholder="Enter password", type="password")
                st.button ("Login", on_click=self.LoggedIn_Clicked, args= (userName, password))

    def __init__(self):
        with headerSection:
            st.title("Streamlit Application")
            #first run will have nothing in session_state
            if 'loggedIn' not in st.session_state:
                st.session_state['loggedIn'] = False
                self.show_login_page() 
            else:
                if st.session_state['loggedIn']:
                    self.show_logout_page()    
                    self.show_main_page()  
                else:
                    self.show_login_page()