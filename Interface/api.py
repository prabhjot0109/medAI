import requests
# Define the API URL
api_url = "http://13.48.136.54:8000/api/api-code/"
# Define the access key
access_key = "480c2773-abda-4714-b5fc-082845ed516d"
# Set up the headers with the access key
headers = {
    "Authorization": f"Bearer {access_key}"
}
# Send the POST request
response = requests.post(api_url, headers=headers)
# Check if the request was successful
if response.status_code == 200:
    # Extract the API code from the response
    api_code = response.json().get("api_code")
    # Display the API code in the footer of your project
    print("API Code:", api_code)
else:
    # Handle errors
    print("Error:", response.status_code, response.text)