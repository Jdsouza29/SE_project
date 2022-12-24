from controller import view_booking_record
import streamlit as st
import pandas as pd
from controller import *


def view_records():
    #tables_list = show_tables()
    #table = st.selectbox("Select table", tables_list)
    result = view_booking_record()
    result1 = []
    result2 = []
    result1 = [list(result[i]) for i in range(len(result))]
    for i in range(len(result)):
        result1[i][4] = str(result1[i][4])
        result1[i][5] = str(result1[i][5])
        result2.append(tuple(result1[i]))
    # result1.append(result[0][0])
    # result1.append(result[0][0])
    # result1.append(result[0][0])
    # result1.append(result[0][0])
    # result1.append(result[0][0])
    # result1.append(result[0][0])
    # result1.append(result[0][0])
    # result1.append(result[0][0])
    print(result2)

    attributes = get_attribute_of_booking_record()
    if st.button("view Records"):
        df = pd.DataFrame(result2, columns=attributes)
        # print(df)
        st.dataframe(df)
