import pandas as pd
import numpy as np
import streamlit as st

fatalities=pd.read_csv('fatalities_df_final.csv')
state_travel=pd.read_csv('final_state_travel.csv')
seasonal=pd.read_csv('seasonal.csv')

st.subheader('Table')

Ascending_list=False
if st.checkbox('Worst Performing'):
    Ascending_list=True

option = st.radio('Sort column',options=['items_available','daily_customer_count','store_sales','sales_per_customer'])