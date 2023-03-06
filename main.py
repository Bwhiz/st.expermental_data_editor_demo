import streamlit as st
import pandas as pd

st.set_page_config(
    layout="wide",
)

st.markdown("<h2 style='text-align: center; color: #0c1864;'>Task Monitoring App</h2>", unsafe_allow_html=True)
st.markdown("")


df = pd.DataFrame(
    [{'TASKS':'','STATUS' : False}])
df.index = df.index+1

col1, col2, col3 = st.columns([0.25, 1, 0.25])

#st.eperimental_data_editor:
with col2:
    edited_df = st.experimental_data_editor(df, num_rows='dynamic', width=1000)

final_df = edited_df[(edited_df['STATUS'] == False)][['TASKS']]
pending_tasks = final_df.copy()
pending_tasks.columns= ['LIST OF PENDING TASKS']

st.markdown("")
col4, col5, col6 = st.columns([0.25, 1, 0.25])

with col5:
    if len(final_df) == 0:
        st.markdown("<h3 style='text-align: center; color: #0c1864;'>'Yippe!! you are done for the day'</h3>", unsafe_allow_html=True)
    else:
        st.dataframe(pending_tasks,width=500)
