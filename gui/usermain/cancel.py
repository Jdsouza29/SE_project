from controller import view_room_by_user
import streamlit as st
import pandas as pd
from controller import *

def cancel_booking():
    #user_name=st.text_input("Enter your user_name to view your booking")
    room_id=st.number_input("Enter the room id to cancel the booking")
    room_id=int(room_id)
    if True:
        if st.button("CONTINUE CANCELLATION"):
            selected_result = get_selected_record(room_id)
            print(selected_result)
            new_val=[]
            cancel_date=st.date_input("Select cancel date")
        if st.button("CONFIRM"):
        
            cancel_booking_by_user(room_id)
            st.success("CANCELLATION SUCCESSFUL")
            # size=selected_result[0][1]
            # project=selected_result[0][2]
            # A_V=selected_result[0][3]
            # white_board_util=selected_result[0][4]
            # mic_speaker=selected_result[0][5]
            # Camera=selected_result[0][6]
            # AC=selected_result[0][7]
            # add_date=cancel_date
            # last_modified=selected_result[0][8]
        
        #new_val.append(selected_result[0][0])
        # new_val.append(selected_result[0][1])
        # new_val.append(selected_result[0][2])
        # new_val.append(selected_result[0][3])
        # new_val.append(selected_result[0][4])
        # new_val.append(selected_result[0][5])
        # new_val.append(selected_result[0][6])
        # new_val.append(selected_result[0][7])
        # new_val.append(cancel_date)
        # new_val.append(selected_result[0][8])
        
        
        
            # add_to_room(size,project,A_V,white_board_util,mic_speaker,Camera,AC,add_date)