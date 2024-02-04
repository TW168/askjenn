import streamlit as st 
import pandas as pd 
import plotly.express as px


st.title('Ask Jenn')
st.markdown('The purpose of this app to provide summary states based on your Redfin data search', unsafe_allow_html=True)

# Prep upload file
st.markdown('#### Upload a CSV file')
uploaded_file = st.file_uploader('Chooose a CSV file from Redfin:', accept_multiple_files=False)
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file, skiprows=range(1,2))
    st.dataframe(df)

    # Property Metrics
    st.markdown('## Property Metrices')
    col1, col2, col3, col4 = st.columns(4)
    col1.metric('Total', "{:,}".format(len(df), help='Number of properties'))
    col2.metric('Avg. Price', "${:,}".format(df['PRICE'].mean()).split(',')[0] + 'K', help = 'Average sales price')
    col3.metric('Avg. DOM', int(df['DAYS ON MARKET'].mean()), help = 'Average days on market')
    col4.metric('Avg. FT² ', "${:,}".format(int(df['$/SQUARE FEET'].mean())), help = 'Average price per square foot')

    # Charts
    with st.expander('Charts', expanded=True):
        st.markdown('## Charts')
        fig = px.histogram(df, x='DAYS ON MARKET', title='Days on Market Histogram Chart')
        st.plotly_chart(fig, use_container_width=True)

        fig = px.box(df, x='PRICE', title='Price Box Plot')
        st.plotly_chart(fig, use_container_width=True)

        fig = px.histogram(df, x='$/SQUARE FEET', title='Price per Square Feet Histogram')
        st.plotly_chart(fig, use_container_width=True)


  