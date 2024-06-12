import pandas as pd
import requests
import streamlit as st

# Define API URLs and endpoints
api_urls = {'whitepages': 'https://www.whitepages.com/?is_sem=true&utm_source=google&utm_medium=cpc&utm_campaign=649050479&utm_term=white%20pages&sem_account_id=1432223903&sem_campaign_id=649050479&sem_ad_group_id=9903578977&sem_device_type=c&sem_target_id=kwd-12141261&sem_keyword=white%20pages&sem_matchtype=e&sem_network=g&sem_location_id=9011147&sem_placement=&sem_placement_category=&sem_ad_id=564292005973&sem_ad_tag=&sem_lob=BR_HEAD&sem_path=default&gad_source=1&gclid=EAIaIQobChMI-JSSqvDWhgMVT1R_AB3PFwgIEAAYASAAEgKCh_D_BwE'}

# Function to search URLs using API and parse JSON responses
def search_site(api_url, name, number):
    payload = {'name': name, 'number': number}  # Adjust payload keys according to API requirements
    response = requests.get(api_url, params=payload, verify=False)  # Added verify=False to bypass SSL verification
    if response.status_code == 200:
        data = response.json()
        # Adjust the following line based on the actual structure of the JSON response
        result = data.get('result', {})
        return result
    else:
        return None
    
# Streamlit App
st.title("Katch")

# File uploader for input file
uploaded_file = st.file_uploader("Choose a file", type='xlsx') # Adjust for file type (excel, csv, json, etc.)

if uploaded_file is not None:
    # Read file
    df = pd.read_excel('/Users/christhompson/Desktop/Thompson/Code/Katch/easy_search/data/test.xlsx') # Adjust for file type and update path to file
    st.write("Dataframe loaded")
    st.write(df)

    # Collect additional entries
    additional_entries = []
    if st.checkbox("Do you want to add additional names and numbers?"):
        name = st.text_input("Enter name:")
        number = st.text_input("Enter number:")
        if st.button("Add entry"):
            additional_entries.append({'First Name': name.split()[0], 'Last Name': ' '.join(name.split()[1:]), 'ID Number': number})
            st.success(f"Added entry: {name}, {number}")
    if additional_entries:
            additional_df = pd.DataFrame(additional_entries)
            df = pd.concat([df, additional_df], ignore_index=True)

    # Process the DataFrame and search for each name and number
    new_info_list = []
    for index, row in df.iterrows():
        name = f"{row['First Name']} {row['Last Name']}"
        number = row['ID Number']

        # Check if name and number are available, else prompt user
        if pd.isna(name):
            name = st.text_input(f"Enter name for row {index}: ")
        if pd.isna(number):
            number = st.text_input(f"Enter number for row {index}: ")
        
        # Collect results from Whitepages API
        results = []
        for site, url in api_urls.items():
            result = search_site(url, name, number)
            if result:
                # Extract relevant information from JSON and convert to string
                result_str = ' | '.join([f"{key}: {value}" for key, value in result.items()])
                results.append(result_str)

        # Concatenate results and append to list
        new_info = ' | '.join(results)
        new_info_list.append(new_info)

    # Add new column to dataframe
    df['new_info'] = new_info_list

    # Show the updated DataFrame
    st.write("Updated DataFrame:")
    st.write(df)

    # File downloader for output file
    output_file = 'updated_data.xlsx'
    df.to_excel(output_file, index=False)
    st.download_button(label="Download updated file", data=open(output_file, 'rb').read(), file_name=output_file,
                        mime='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet') 