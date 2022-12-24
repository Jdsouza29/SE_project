import streamlit as st
from gui.adminmain.add_room import add_rooms_by_admin
from gui.adminmain.edit import edit_facility_by_admin
from gui.adminmain.delete import delete_by_admin
from gui.adminmain.view import view_records
#from view import view_records
#from edit import edit_facility
def admin_main():
    print(st.session_state['log'])
    #if st.session_state['log']==3:
        #st.session_state['log']=4
    st.title("ADMIN PAGE FOR CONFERENCE ROOM BOOKING SYSTEM")
    menu = ["ADD ROOMS", "EDIT ROOM FACILITIES", "VIEW BOOKING RECORDS","DELETE ROOMS"]
    choice = st.sidebar.selectbox("Menu", menu)

    #create_table()
    if choice == "ADD ROOMS":
        #st.session_state['log']=5
        print(st.session_state['log'])
        st.subheader("ENTER ROOM DETAILS")
        add_rooms_by_admin()

    elif choice == "EDIT ROOM FACILITIES":
        st.subheader("UPDATE ROOM FACILITIES")
        edit_facility_by_admin()

    elif choice == "VIEW BOOKING RECORDS":
        st.subheader("VIEW RECORDS")
        view_records()

    elif choice == "DELETE ROOMS":
        st.subheader("DELETE ROOM FROM THE TABLE")
        delete_by_admin()

    
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
    admin_main()

