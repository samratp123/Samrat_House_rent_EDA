import streamlit as st
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt

st.header("The Data is here!!!")
df=pd.read_csv("C:\\Users\\samra\\OneDrive\\Desktop\\DATASETS\\House_Rent_Dataset.csv")
st.write(df)

def stats(dataframe):
    st.header('Data Statistics')
    st.write(dataframe.describe())

def data_header(dataframe):
    st.header('Data Header')
    st.write(df.head())
 
def plot(dataframe):
    fig,ax=plt.subplots(1,1)
    ax.bar(x=df['City'],y=df['Rent'])
    ax.set_xlabel('City')
    ax.set_ylabel('Rent')
    st.pyplot(fig)

def interactive_plot(dataframe):
    x_axis_val = st.selectbox('select X_Axis value',options=df.columns)
    y_axis_val = st.selectbox('select Y_Axis value',options=df.columns)
    col = st.color_picker('Select a bar color')
    plot =px.bar(dataframe,x=x_axis_val,y=y_axis_val,template='plotly_dark',barmode='overlay')
    plot.update_traces(marker=dict(color=col))
    st.plotly_chart(plot)



st.title('House_Rent_Dataset')
st.text('This is a overview of House_Rent data')
st.sidebar.title('Nevigation')
uploaded_file=st.sidebar.file_uploader('Upload your file here')
options = st.sidebar.radio('Pages',options=['Home','Data Statistics','Data Header','plot','Interactive Plot'])

if uploaded_file:
    df=pd.read_csv(uploaded_file)

if options == 'Data Statistics':
    stats(df)
elif options == 'Data Header':
    data_header(df)
elif options == 'Plot':
    plot(df)
elif options == 'Interactive Plot':
    interactive_plot(df)


