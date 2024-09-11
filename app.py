import streamlit as st
import plotly.express as px
st.header('Iris Data Set')
df=px.data.iris()
with st.expander('Show data'):
    st.write(df)
with st.sidebar:
    st.subheader('Scatter')
    option = st.selectbox('Select X axis',('sepal_length','sepal_width'))

    optiony = st.selectbox('Select Y axis',('petal_length','petal_width'))
st.subheader('Scatter')
fig=px.scatter(df,x=option,y=optiony)
st.plotly_chart(fig)

with st.sidebar:
    st.subheader('Histogram')
    opt=st.selectbox('Select first coloum ',('sepal_length','sepal_width','petal_length','petal_width'))
st.subheader('Histogram')
fig1=px.histogram(df,opt)  
st.plotly_chart(fig1)  
    
