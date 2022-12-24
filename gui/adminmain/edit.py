from controller import get_selected_room
import streamlit as st
import pandas as pd
from controller import *

def edit_facility_by_admin():
    #st.session_state['active']=2
    result=view_room()
    df = pd.DataFrame(result, columns=['Room_id','size','project','A_V','white_board_util','mic_speaker','Camera','AC','add_date','last_modi','A_ID'])
    with st.expander("Current Rooms"):
        st.dataframe(df)
    list_of_rooms = [i[0] for i in view_only_room_id()]
    selected_room = st.selectbox("Room to Edit", list_of_rooms)
    selected_result = get_selected_room(selected_room)
    #attributes = get_attribute_of_room()
    #new_val=[]
    #st.session_state['log']=4
    
        #st.session_state['active']=3
    #print(st.session_state['log'])
    #if st.session_state['log']==5:
        #st.session_state['log']=0
    if selected_result:
        room_id = selected_result[0][0]
        size= selected_result[0][1]
        project = selected_result[0][2]
        A_V = selected_result[0][3]
        white_board_util = selected_result[0][4]
        mic_speaker = selected_result[0][5]
        camera = selected_result[0][6]
        AC = selected_result[0][7]
        add_date = selected_result[0][8]
        last_modi = selected_result[0][9]
        A_id = selected_result[0][10]
        
        col1, col2 = st.columns(2)
        new_room_id=room_id
        with col1:
            new_size=st.number_input("Enter Room size")
            new_project=st.checkbox("Projector facility")
            #print(project)
            if new_project:
                new_project=1
            else:
                new_project=0
            new_A_V=st.checkbox("Audio video facility")
            if new_A_V:
                new_A_V=1
            else:
                new_A_V=0
            new_white_board=st.checkbox("white board facility")
            if new_white_board:
                new_white_board=1
            else:
                new_white_board=0
                
        with col2:
            new_mic_speaker=st.checkbox("Mic and speaker facility")
            if new_mic_speaker:
                new_mic_speaker=1
            else:
                new_mic_speaker=0
                
                
            new_camera=st.checkbox("Camera facility")
            if new_camera:
                new_camera=1
            else:
                new_camera=0
                
                
            new_AC=st.checkbox("AC facility")
            if new_AC:
                new_AC=1
            else:
                new_AC=0
                
                
            new_add_date=st.date_input("Enter the date")
            
            new_last_modi=st.date_input("Enter last modified date")
            
                
            new_A_id=st.number_input("Enter Admin id")
        if st.button("Update Room details"):
            edit_room(new_room_id,new_size,new_project,new_A_V,new_white_board,new_mic_speaker,new_camera,new_AC,new_add_date,new_last_modi,new_A_id,room_id,size,project,A_V,white_board_util,mic_speaker,camera,AC,add_date,last_modi,A_id)
            st.success("Successfully updated")
    
                    
            
            
        
    
    

    