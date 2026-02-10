import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.io

uploaded_files = st.file_uploader(
    "Upload data", accept_multiple_files=True, type="csv"
)
for uploaded_file in uploaded_files:
    df = pd.read_csv(uploaded_file)
    #st.write(df)
    #st.line_chart(df)
    x = st.selectbox("Select X-axis", df.columns)
    y = st.multiselect("Select Y-axis", df.columns)
    x_axis_title = st.text_input("X-Axis Title", value=x)
    y_axis_title = st.text_input("Y-Axis Title", value=y[0] if y else "")
    fig = px.line(df, x=x, y=y, title="Line Chart")
    fig.update_xaxes(title_text=x_axis_title)
    fig.update_yaxes(title_text=y_axis_title)
    st.plotly_chart(fig)
    st.download_button(
        label="Download Plot as HTML", 
        data=fig.to_html(),
        file_name="line_chart.html",
        mime="text/html"
    )
    