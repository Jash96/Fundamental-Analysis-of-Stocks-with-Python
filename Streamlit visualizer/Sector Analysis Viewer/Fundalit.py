# -*- coding: utf-8 -*-
"""
Created on Tue May 31 16:28:06 2022

@author: Jashan
"""

import streamlit as st
import pandas as pd
import sqlalchemy

st.title('Fundamentals Comparison')

engine = sqlalchemy.create_engine('sqlite:///Fundamentals.db')

df = pd.read_sql('Fundamentalstable',
                 engine, index_col=['symbol'])

dropdownI = st.selectbox('Choose your sector',
                         df.sector.unique())

dropdownII = st.selectbox('Choose your metric',
                          df.columns[df.columns != 'sector'])

values = df[df.sector == dropdownI][[dropdownII]]

st.bar_chart(values)