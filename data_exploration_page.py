import streamlit as st
import pandas as pd
import plotly.express as px

def run_data_exploration_page():
    st.title("Data Exploration - Sales Prediction System")

    # Upload a CSV file with a unique key
    uploaded_file = st.sidebar.file_uploader("Upload a CSV file", type=["csv"], key="file_uploader")

    if uploaded_file is not None:
        # Load the user-uploaded data
        df = pd.read_csv(uploaded_file)

        # Displaying the DataFrame
        st.subheader("Uploaded Dataset")
        st.write(df)

        # Sidebar Filters
        st.sidebar.header("Filters")
        selected_year = st.sidebar.selectbox("Select Year", df['Year'].unique())
        selected_product = st.sidebar.selectbox("Select Product", df['Products'].unique())

        filtered_df = df[(df['Year'] == selected_year) & (df['Products'] == selected_product)].copy()

        # Bar Chart
        st.subheader("Bar Chart - Units Sold per Season")
        if 'UnitsSold' in filtered_df.columns:
            fig_bar = px.bar(filtered_df, x='Season', y='UnitsSold', color='Season', title='Units Sold per Season')
            st.plotly_chart(fig_bar, use_container_width=True)
        else:
            st.warning("The 'UnitsSold' column is not present in the filtered dataset.")

        # Line Chart
        if 'Date' in filtered_df.columns:
            st.subheader("Line Chart - Sales over Time")
            fig_line = px.line(filtered_df, x='Date', y='Sales', title='Sales over Time')
            st.plotly_chart(fig_line, use_container_width=True)
        else:
            st.warning("The 'Date' column is not present in the filtered dataset.")

        # Pie Chart
        st.subheader("Pie Chart - Sales Percentage by Product Color")
        if 'ProductColor' in filtered_df.columns:
            fig_pie = px.pie(filtered_df, names='ProductColor', values='SalesPercentage', title='Sales Percentage by Product Color')
            st.plotly_chart(fig_pie, use_container_width=True)
        else:
            st.warning("The 'ProductColor' column is not present in the filtered dataset.")

        # TreeMap
        st.subheader("TreeMap - Sales by Product Size")
        if 'ProductSize' in filtered_df.columns:
            fig_tree = px.treemap(filtered_df, path=['Products', 'ProductSize'], values='UnitsSold', title='Sales by Product Size')
            st.plotly_chart(fig_tree, use_container_width=True)
        else:
            st.warning("The 'ProductSize' column is not present in the filtered dataset.")

        # HeatMap
        st.subheader("HeatMap - Correlation between Price, Units Sold, and Rating")
        if all(col in filtered_df.columns for col in ['Price', 'UnitsSold', 'Rating']):
            fig_heatmap = px.imshow(filtered_df[['Price', 'UnitsSold', 'Rating']].corr(), labels=dict(color="Correlation"))
            st.plotly_chart(fig_heatmap, use_container_width=True)
        else:
            st.warning("Columns 'Price', 'UnitsSold', and 'Rating' are not all present in the filtered dataset.")

        # Scatter Plot
        st.subheader("Scatter Plot - Price vs. Units Sold")
        if all(col in filtered_df.columns for col in ['Price', 'UnitsSold', 'Rating']):
            fig_scatter = px.scatter(filtered_df, x='Price', y='UnitsSold', size='Rating', color='Rating',
                                     title='Relationship between Price and Units Sold')
            st.plotly_chart(fig_scatter, use_container_width=True)
        else:
            st.warning("Columns 'Price', 'UnitsSold', and 'Rating' are not all present in the filtered dataset.")

        # Time Series Analysis
        st.subheader("Time Series Analysis - Sales over Time")
        if 'Date' in filtered_df.columns:
            linechart = pd.DataFrame(filtered_df.groupby('Date')["Sales"].sum()).reset_index()
            fig_ts = px.line(linechart, x="Date", y="Sales", labels={"Sales": "Sales over Time"},
                             height=500, width=1000, template="gridon")
            st.plotly_chart(fig_ts, use_container_width=True)
        else:
            st.warning("The 'Date' column is not present in the filtered dataset.")

        with st.expander("View Data of TimeSeries:"):
            st.write(linechart.T.style.background_gradient(cmap="Blues"))
            csv_ts = linechart.to_csv(index=False).encode("utf-8")
            st.download_button(f'Download Time Series Data {selected_year}', data=csv_ts,
                               file_name=f"TimeSeries_Data_{selected_year}.csv", mime='text/csv')

        # Download Data
        csv = filtered_df.to_csv(index=False).encode('utf-8')
        st.download_button('Download Filtered Data', data=csv, file_name="Filtered_Data.csv", mime="text/csv")

if __name__ == "__main__":
    run_data_exploration_page()

        