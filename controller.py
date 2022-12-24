import mysql.connector
import os
import streamlit as st
from config import config
from dotenv import load_dotenv

load_dotenv()

connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='SE_Project',
    port="3306"
)

c = connection.cursor(buffered=True)


def login(a, b):
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='se_project',
        port="3306"
    )

    c = connection.cursor(buffered=True)
    c.execute(
        "Select username,user_password from user where username=(%s) and user_password=(%s)", (a, b))
    return c.fetchall()


def login_admin(user_id, password, uni_key):
    user_id = str(user_id)
    password = str(password)
    uni_key = str(uni_key)
    c.execute(
        "Select ad_username,ad_password,Uni_key from admn where ad_username=(%s) and ad_password=(%s) and Uni_key=(%s)", (user_id, password, uni_key))
    x = c.fetchall()
    if (x):
        print("1")
        return 1
    else:
        print("0")
        return 0


def view_record():
    c.execute(
        'select BR_ID,U_ID,R_ID,Book_date,Book_start_time,book_stop_time from booking_record')
    res = c.fetchall()
    return res


def add_(uname, upass, name, dob, phone, mail, gender):
    c.execute('insert into user (Username,user_password,U_name,gender,DOB,phone,e_mail) values'
              '(%s,%s,%s,%s,%s,%s,%s);', (uname, upass, name, gender, dob, phone, mail))
    connection.commit()


def add_rooms(table, new_val):
    new_val = tuple(new_val)
    tot_values = '%s,'*len(new_val)
    tot_values = tot_values[:-1]
    c.execute(
        f"INSERT INTO {table} (size,project,A_V,white_board_util,mic_speaker,Camera,AC,add_date,last_modi,A_ID) VALUES ({tot_values})", new_val)
    connection.commit()


def get_attribute_of_room():
    c.execute(f'select * from room')
    #res = c.fetchall()
    attributes = c.column_names
    return attributes


def select_table_room():
    c.execute('show tables')
    res = c.fetchall()
    tables = [i[0] for i in res]
    for i in tables:
        if i == "room":
            return i


def view_room():
    c.execute(f'select * from room')
    res = c.fetchall()
    return res


def view_only_room_id():
    c.execute('SELECT R_id from room')
    data = c.fetchall()
    return data


def get_selected_room(selected_room):
    c.execute(f'select * from room where R_id={selected_room}')
    data = c.fetchall()
    return data


def edit_room(new_room_id, new_size, new_project, new_A_V, new_white_board, new_mic_speaker, new_camera, new_AC, new_add_date, new_last_modi, new_A_id, room_id, size, project, A_V, white_board_util, mic_speaker, camera, AC, add_date, last_modi, A_id):
    c.execute("UPDATE room SET R_id=%s, size=%s, project=%s, A_V=%s, white_board_util=%s,mic_speaker=%s,camera=%s,AC=%s,add_date=%s,last_modi=%s,A_id=%s WHERE R_id=%s and size=%s and project=%s and A_V=%s and white_board_util=%s and mic_speaker=%s and camera=%s and AC=%s and add_date=%s and last_modi=%s and A_id=%s",
              (new_room_id, new_size, new_project, new_A_V, new_white_board, new_mic_speaker, new_camera, new_AC, new_add_date, new_last_modi, new_A_id, room_id, size, project, A_V, white_board_util, mic_speaker, camera, AC, add_date, last_modi, A_id))
    connection.commit()
    # data = c.fetchall()
    # return data


def get_all_values_of_room():
    c.execute(f"show keys from room where key_name = 'primary'")
    res = c.fetchall()
    P_key = res[0][4]
    c.execute(f"select {P_key} from room")
    attri_list = c.fetchall()
    attri_list = [i[0] for i in attri_list]
    return [sorted(attri_list), P_key]


def delete_val(value, attribute):
    try:
        # que to get datatype if needed select data_type from information_schema.columns where table_name = 'ticket' and column_name = 'pnr'
        c.execute(f"delete from room where {attribute}='{value}'")
        connection.commit()
        st.success("Deletion successful")
    except Exception as e:
        st.error(e)


def view_booking_record():
    c.execute(f'select * from booking_record')
    res = c.fetchall()
    return res


def get_attribute_of_booking_record():
    c.execute(f'select * from booking_record')
    #res = c.fetchall()
    attributes = c.column_names
    return attributes


def view_room_by_user():
    c.execute(
        f'select * from room where R_id not in(select R_id from booking_record)')
    res = c.fetchall()
    return res


def get_room(room_no):
    c.execute(f'select * from room where R_id={room_no}')
    res = c.fetchall()
    return res


def add_to_booking_record(R_id, u_id, book_date, book_start_time, book_stop_time, size, project, A_V, white_board_util, mic_speaker, Camera, AC):
    #new_list = tuple(new_list)
    #tot_values = '%s,'*len(new_list)
    #tot_values = tot_values[:-1]
    c.execute('INSERT INTO booking_record (R_id,u_id,book_date,book_start_time,book_stop_time,size,project,A_V,white_board_util,mic_speaker,Camera,AC) VALUES  (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);',
              (R_id, u_id, book_date, book_start_time, book_stop_time, size, project, A_V, white_board_util, mic_speaker, Camera, AC))
    connection.commit()


def delete_from_room(R_id):
    c.execute(f'delete from room where R_id={R_id}')
    connection.commit()


def cancel_booking_by_user(R_id):
    c.execute(f'delete from booking_record where R_id={R_id}')
    connection.commit()


def get_selected_record(room_id):
    c.execute(
        f'SELECT size,project,A_V,white_board_util,mic_speaker,camera,AC,book_date FROM booking_record WHERE R_id={room_id}')
    data = c.fetchall()
    return data


def add_to_room(size, project, A_V, white_board_util, mic_speaker, Camera, AC, add_date):
    # new_val = tuple(new_val)
    # tot_values = '%s,'*len(new_val)
    # tot_values = tot_values[:-1]
    c.execute('INSERT INTO room (size,project,A_V,white_board_util,mic_speaker,Camera,AC,add_date) VALUES' '(%s,%s,%s,%s,%s,%s,%s,%s);',
              (size, project, A_V, white_board_util, mic_speaker, Camera, AC, add_date))
    connection.commit()


def view_only_room_id_not_in_booking():
    c.execute(
        'SELECT R_id from room where R_id not in(select R_id from booking_record')
    data = c.fetchall()
    return data


def add_to_booking_table(table, new_val):
    new_val = tuple(new_val)
    tot_values = '%s,'*len(new_val)
    tot_values = tot_values[:-1]
    c.execute(
        f"INSERT INTO {table} (R_id,u_id,book_date,book_start_time,book_stop_time,size,project,A_V,white_board_util,mic_speaker,Camera,AC) VALUES ({tot_values})", new_val)
    connection.commit()


def select_record_table():
    c.execute('show tables')
    res = c.fetchall()
    tables = [i[0] for i in res]
    for i in tables:
        if i == "booking_record":
            return i
