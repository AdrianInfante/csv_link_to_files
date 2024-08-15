import os
import requests
import pandas as pd


# path to your CSV file
csv_file_path = r"localPath"


# directory where you want to save the downloaded files
download_directory = r"localPath"



os.makedirs(download_directory, exist_ok=True)


try:
    df = pd.read_csv(csv_file_path)
except Exception as e:
    print(f"Error reading the CSV file: {e}")
    exit(1)


print("Columns in the DataFrame:", df.columns.tolist())


print(df.head())


url_column_name = 'URLs'  


for index, row in df.iterrows():
    
    print(f"Row {index}: {row}")

    
    if url_column_name in row:
        url = row[url_column_name]
        print(f"Processing URL: {url}")
    else:
        print(f"Column '{url_column_name}' not found in the row.")
        continue  

    try:
        
        response = requests.get(url, stream=True)
        response.raise_for_status()  

        
        file_name = os.path.basename(url)

        
        file_path = os.path.join(download_directory, file_name)

        
        with open(file_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)

        print(f"Downloaded: {file_name}")

    except requests.exceptions.RequestException as e:
        print(f"Failed to download {url}: {e}")
    except Exception as e:
        print(f"An error occurred while downloading {url}: {e}")
