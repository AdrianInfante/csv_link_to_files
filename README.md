# Extract and Download URLs from CSV

# Script Details

Reading the CSV File: The script uses the pandas library to read the CSV file into a DataFrame.
Extracting URLs: It iterates over each row, extracts the URL from the specified column, and sends a GET request using the requests library.
Downloading Files: The script saves each file to the specified local directory, handling various file types and names.
Error Handling: The script includes error handling for issues like invalid URLs, network errors, and missing directories.

