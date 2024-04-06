import pandas as pd
import streamlit as st
import os


st.title("Simple CSV file to database converter")

st.header("Please enter database details")

hostname = st.text_input("Please enter host name")
database = st.text_input("Please enter database name")
username = st.text_input("Please enter username")
pwd = st.text_input("Please enter password", type="password")
port_id = st.text_input("Please enter port_id")

connuri = f'postgresql://{username}:{pwd}@{hostname}:{port_id}/{database}'
st.write("Connection URI")
st.write(connuri)

@st.cache_data
def connect_to_db(connuri):
    return pd.read_sql('SELECT current_database();', connuri)

try:
    df = connect_to_db(connuri)
    st.write(df.head())
except Exception as e:
    st.error(f"Error connecting to the database: {e}")
st.header("Please upload the CSV file")
uploaded_file = st.file_uploader("Choose a CSV file")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write('**Uploaded CSV file:**')
    st.write(df)
    table_name = os.path.splitext(uploaded_file.name)[0]
    
    try:
        df.to_sql(table_name, connuri, if_exists='replace', index=False)
        st.success(f"Table '{table_name}' created and data inserted successfully!")
    except Exception as e:
        st.error(f"Error creating table or inserting data: {e}")