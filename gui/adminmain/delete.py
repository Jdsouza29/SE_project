from controller import get_selected_room
import streamlit as st
import pandas as pd
from controller import *


#   tables_list = 
    #table = st.selectbox("Select table", tables_list)
def delete_by_admin():
    result = view_room()
    attributes = get_attribute_of_room()
    df = pd.DataFrame(result, columns=attributes)
    st.dataframe(df)
    # if st.button('select row'):
    rooms = get_all_values_of_room()
    value = st.selectbox(f'select {rooms[1]} to delete',rooms[0])
    st.warning("Changes Made will be commited")
    #col1=st.columns(1)
    #with col1:
    if st.button("delete value"):
        delete_val(value,rooms[1])
