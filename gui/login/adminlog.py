import streamlit as st
from controller import *
from gui.adminmain.admin_main_page import *

def adLoggedIn_Clicked(user_id,password,unique_key):
    if user_id=='' or password=='' or unique_key=='':  
            st.error("Enter all fileds")  
    elif login_admin(user_id,password,unique_key):
        st.session_state['ad']=1
        print("Here5")
    else:
        st.info("Wrong login Credentials")

def admin_login():
    print("hey5")
    if 'ad' not in st.session_state or st.session_state['ad']==0:
        st.title("admin Login Page")
        user_id = st.text_input ("Enter your ID")
        password = st.text_input ("Enter your password")
        unique_key = st.text_input ("Enter the Unique key")
        
        
        st.button ("Login", on_click=adLoggedIn_Clicked, args= (user_id, password,unique_key))
        if st.button("go back to login"):
            # del st.session_state['new']
            del st.session_state['log']
                
    else:
        admin_main()
    # login_admin()


# class login_admin():
#     def _init_(self):
#         print("Hello world")
        
#         self.show_adlogin()
        




#     #def create_user(self):
#      #   createuser()

#     def show_adlogin(self):
#         print("WHY HERE")
#         st.title("admin Login Page")
#         user_id = st.text_input ("Enter your ID")
#         password = st.text_input ("Enter your password")
#         unique_key = st.text_input ("Enter the Unique key")
        
#         st.button ("Login", on_click=self.adLoggedIn_Clicked, args= (user_id, password,unique_key))

