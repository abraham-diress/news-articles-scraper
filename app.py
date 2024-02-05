import streamlit as st
import pandas as pd

# Load your clustered articles DataFrame
# Replace 'your_dataframe.csv' with the actual path to your CSV file
df = pd.read_csv('NYT_articles_20223_clustered.csv')

# Streamlit app
def main():
    st.title('Clustered Articles')

    # Dropdown to select cluster
    cluster_options = df['clusters'].unique().tolist()
    selected_cluster = st.selectbox('Select a Cluster', cluster_options)

    # Filter DataFrame based on selected cluster
    filtered_df = df[df['clusters'] == selected_cluster]

    # Display articles for the selected cluster
    st.subheader(f'Articles for Cluster {selected_cluster}')
    for index, row in filtered_df.iterrows():
        st.markdown(f"[{row['title']}]({row['web_url']})")

# Run the main function
if __name__ == '__main__':
    main()