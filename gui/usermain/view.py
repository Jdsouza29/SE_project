from controller import view_room_by_user
import streamlit as st
import pandas as pd
from controller import *
from datetime import datetime
#from gui.usermain.book import book_by_user

def view_rooms_by_user():
    #tables_list = show_tables()
    #table = st.selectbox("Select table", tables_list)
    result = view_room_by_user()
    attributes = get_attribute_of_room()
    if st.button("View rooms"):
        df = pd.DataFrame(result, columns=attributes)
        st.dataframe(df)
    
    
    
    st.write("Enter below details")
    #room_no=st.number_input("Enter the room id from the above list to book the room")
    #room_no=int(room_no)
    new_list=[]
        #result=get_room(room_no)
    list_of_rooms = [i[0] for i in view_only_room_id()]
    selected_room = st.selectbox("Room to book", list_of_rooms)    
    user_id=st.number_input("Please enter your user id")


        
    selected_result = get_selected_room(selected_room)
    from datetime import datetime
        #new_list.append(room_no)
    book_date=st.date_input("Book date")
    book_start_time=st.time_input("Booking time")
    book_stop_time=st.time_input("Book end time")
    start_time = st.slider(
    "When do you start?",
    value=datetime(2020, 1, 1, 9, 30),
    format="MM/DD/YY - hh:mm") 
    u_id=user_id
    
    R_id=selected_result[0][0]
    new_list.append(R_id)
    new_list.append(u_id)
    
    new_list.append(book_date)
    new_list.append(book_start_time)
    new_list.append(book_stop_time)
    size=selected_result[0][1]
    new_list.append(size)
    project=selected_result[0][2]
    new_list.append(project)
    A_V=selected_result[0][3]
    new_list.append(A_V)
    white_board_util=selected_result[0][4]
    new_list.append(white_board_util)
    mic_speaker=selected_result[0][5]
    new_list.append(mic_speaker)
    Camera=selected_result[0][6]
    new_list.append(Camera)
    AC=selected_result[0][7]
    new_list.append(AC)
        #attributes=get_attribute_of_room()
        #result.append[user_id]
        
        #delete_from_room()z
    table=select_record_table()
    if st.button("CONFIRM BOOKING"):
        st.success("Booking Successful")
        print(new_list)
        add_to_booking_table(table, new_list)
        # delete_from_room(R_id)
    
    
    
