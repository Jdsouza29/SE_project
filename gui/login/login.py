import mysql.connector
import streamlit as st

from gui.usermain.main import *
from controller import *
from gui.login.createuser import *
from gui.login.adminlog import *


def login_Main():
    print("here")
    login_user()

class login_user():
    def __init__(self):
        self.show_login()



    def LoggedIn_Clicked(self,userName,password):
        if userName =='' or password=='':
            st.error("Please enter all fields")
            st.session_state['log']=0
        elif login(userName,password):
            st.session_state['log']=1
            # st.sidebar.text("");st.sidebar.text("");st.sidebar.text("");st.sidebar.text("");st.sidebar.text("");st.sidebar.text("") 
            # st.sidebar.text("");st.sidebar.text("");st.sidebar.text("");st.sidebar.text("");st.sidebar.text("");st.sidebar.text("")
            # st.sidebar.text("");st.sidebar.text("");st.sidebar.text("");st.sidebar.text("");st.sidebar.text("");st.sidebar.text("")
            # st.sidebar.text("");st.sidebar.text("");st.sidebar.text("");st.sidebar.text("");st.sidebar.text("");st.sidebar.text("")
            # st.sidebar.text("");st.sidebar.text("");st.sidebar.text("");st.sidebar.text("")


        
            if st.sidebar.button("Logout"):
                st.experimental_rerun()
                del st.session_state['log']
                st.experimental_rerun()
                st.experimental_rerun()

        else:
            st.session_state['log']=0
            st.info("Wrong login Credentials")


    def create_user(self):
        # CreateUser()
        st.session_state['log'] =2
    
    def ad_login(self):
        st.session_state['log']=3
        # admin_login()


    def show_login(self):
        if 'log' not in st.session_state:
            st.session_state['log']=0
            st.title("Login Page")
            userName = st.text_input (label=" ", value="", placeholder="Enter your user name")
            password = st.text_input (label=" ", value="",placeholder="Enter password", type="password")
            st.button ("Login", on_click=self.LoggedIn_Clicked, args= (userName, password))
            st.button("Create_User",on_click=self.create_user)
            st.button("Admin_Login",on_click=self.ad_login)
        else:
            if st.session_state['log']==2:
                CreateUser()
            elif st.session_state['log']==3:
                admin_login()
            elif st.session_state['log']==1:
                # st.sidebar.text("");st.sidebar.text("");st.sidebar.text("");st.sidebar.text("");st.sidebar.text("");st.sidebar.text("") 
                # st.sidebar.text("");st.sidebar.text("");st.sidebar.text("");st.sidebar.text("");st.sidebar.text("");st.sidebar.text("")
                # st.sidebar.text("");st.sidebar.text("");st.sidebar.text("");st.sidebar.text("");st.sidebar.text("");st.sidebar.text("")
                # st.sidebar.text("");st.sidebar.text("");st.sidebar.text("");st.sidebar.text("");st.sidebar.text("");st.sidebar.text("")
                # st.sidebar.text("");st.sidebar.text("");st.sidebar.text("");st.sidebar.text("")


            
                # if st.sidebar.button("Logout"):
                #     st.experimental_rerun()
                #     del st.session_state['log']
                #     st.experimental_rerun()
                #     del st.session_state['new']
                #     st.experimental_rerun()
                user_main()
            else:
                st.session_state['log']=0
                st.title("Login Page")
                userName = st.text_input (label=" ", value="", placeholder="Enter your user name")
                password = st.text_input (label=" ", value="",placeholder="Enter password", type="password")
                st.button ("Login", on_click=self.LoggedIn_Clicked, args= (userName, password))
                st.button("Create_User",on_click=self.create_user)
                st.button("Admin_Login",on_click=self.ad_login)

    
