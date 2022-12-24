from controller import add_rooms,get_attribute_of_room
import streamlit as st
import pandas as pd
from controller import *


def add_rooms_by_admin():
    #st.session_state['active']=2
    room=select_table_room()
    attributes = get_attribute_of_room()
    new_val=[]
    #st.session_state['log']=4
    
        #st.session_state['active']=3
    print(st.session_state['log'])
    #if st.session_state['log']==5:
        #st.session_state['log']=0
    size=st.number_input("Enter Room size")
    new_val.append(size)
    project=st.checkbox("Projector facility")
    print(project)
    if project:
        new_val.append(1)
    else:
        new_val.append(0)
    A_V=st.checkbox("Audio video facility")
    if A_V:
        new_val.append(1)
    else:
        new_val.append(0)
    white_board=st.checkbox("white board facility")
    if white_board:
        new_val.append(1)
    else:
        new_val.append(0)
    mic_speaker=st.checkbox("Mic and speaker facility")
    if mic_speaker:
        new_val.append(1)
    else:
        new_val.append(0)
    camera=st.checkbox("Camera facility")
    if camera:
        new_val.append(1)
    else:
        new_val.append(0)
    AC=st.checkbox("AC facility")
    if AC:
        new_val.append(1)
    else:
        new_val.append(0)
        
    add_date=st.date_input("Enter the date")
    new_val.append(add_date)
    last_modi=st.date_input("Enter last modified date")
    new_val.append(last_modi)
        
    A_id=st.number_input("Enter Admin id")
    new_val.append(A_id)
        
        #print(st.session_state['log'])
            #new_val.append(val)
        
    if st.button("Add"):
        add_rooms(room,new_val)
        st.success("insertion was successful")