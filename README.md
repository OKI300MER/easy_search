# easy_search



# import libraries
import pandas as pd
import requests
# read in and export file
input_file = '/Users/christhompson/Desktop/Thompson Files/Code/katch/test data/test.xlsx'  # Change to excel file from user
output_file = '/Users/christhompson/Desktop/Thompson Files/Code/katch/test data/test1.xlsx' # Saved file after searches
df = pd.read_excel(input_file)
df.head()
API Interaction:
A function search_site is defined to send a POST request to the API and handle the response.
# define API URLs & endpoints
api_urls = {
    'Whitepages': 'https://www.whitepages.com/name/Jon-Morgan?fs=1&searchedName=Jon%20Morgan',  # Replace with actual API endpoint
    # 'Site1': 'https://api.site1.com/search', ### Add in real websites with APIs ###
    # 'Site2': 'https://api.site2.com/search',
    # 'Site3': 'https://api.site3.com/search',
    # 'Site4': 'https://api.site4.com/search'
}
Input Handling:
The script checks if the name and number are missing in the spreadsheet, and if so, it prompts the user for input.
# # Function to search a website using its API
# def search_site(api_url, name, number):
#     formatted_url = api_url.format(name=name.replace(" ", "%20"))
#     response = requests.post(api_url, json={'name': name, 'number': number})
#     if response.status_code == 200:
#         return response.json().get('result')
#     else:
#         return None
    

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
# Function to collect additional names and numbers from the user
def collect_additional_entries():
    additional_entries = []
    while True:
        add_more = input("Do you want to add additional names and numbers? (Y/N): ").strip().lower()
        if add_more == 'y':
            name = input("Enter name: ")
            number = input("Enter number: ")
            additional_entries.append({'First Name': name.split()[0], 'Last Name': ' '.join(name.split()[1:]), 'ID Number': number})
        else:
            break
    return additional_entries
Collect Additional Entries:

The collect_additional_entries function prompts the user to add additional names and numbers, storing them in a list of dictionaries.
This list is then converted to a DataFrame and appended to the existing DataFrame.
# Collect additional entries
additional_entries = collect_additional_entries()
# Convert additional entries to DataFrame and append to the existing DataFrame
if additional_entries:
    additional_df = pd.DataFrame(additional_entries)
    df = pd.concat([df, additional_df], ignore_index=True)
Concatenating Results:
It collects results from each API, concatenates them with a separator (e.g., ' | '), and appends them to a list.
# Iterate through each row in the dataframe
new_info_list = []
for index, row in df.iterrows():
    name = row['First Name'] + row['Last Name']
    number = row['ID Number']

    # Check if name and number are available, else prompt user
    if pd.isna(name):
        name = input(f"Enter name for row {index}: ")
    if pd.isna(number):
        number = input(f"Enter number for row {index}: ")

     # Collect results from each API
    results = []
    for site, url in api_urls.items():
        result = search_site(url, name, number)
        if result:
            results.append(result)
    
    # Concatenate results and append to list
    new_info = ' | '.join(results)
    new_info_list.append(new_info)    
Writing the Updated DataFrame:
Adds the new information as a column to the DataFrame and writes the updated DataFrame to a new Excel file.
# Add new column to dataframe
df['new_info'] = new_info_list
# Write updated dataframe to a new Excel file
df.to_excel(output_file, index=False)
print(f"Updated spreadsheet saved to {output_file}")
