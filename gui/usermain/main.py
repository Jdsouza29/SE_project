import streamlit as st
import mysql.connector
from gui.usermain.view import view_rooms_by_user
from gui.usermain.view import *
from gui.usermain.cancel import cancel_booking
# from create import create
# # from database import create_table
# from delete import delete
# from read import read
# from update import update

def user_main():
    #print(st.session_state['log'])
    #if st.session_state['log']==1:
        
    #if 'us' not in st.session_state or st.session_state['us']==0:
        #st.session_state['us']=1
    
        st.title("USER PAGE FOR CONFERENCE ROOM BOOKING SYSTEM")
        menu = ["VIEW AVAILABLE ROOMS","CANCEL BOOKING"]
        choice = st.sidebar.selectbox("Menu", menu)

        #create_table()
        if choice == "VIEW AVAILABLE ROOMS":
            #st.session_state['log']=5
            #print(st.session_state['log'])
            #st.subheader("ENTER ROOM DETAILS")
            view_rooms_by_user()

        elif choice =="CANCEL BOOKING":
            st.subheader("CANCEL ROOM BOOKING")
            cancel_booking()


        
        else:
            st.subheader("About tasks")
        
        def add_bg_from_url():
            st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("https://wallpaperaccess.com/full/3386016.jpg");
                background-attachment: fixed;
                background-size: cover
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

        add_bg_from_url() 
        


if __name__ == '__admin_main__':
        user_main()
