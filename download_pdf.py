import os 
import requests

from config import PATH_TO_PDFS

def download_all_papers(pdf_directory):
    with open(pdf_directory, "r") as f:
        file = [line.strip() for line in f]


    for i, name_of_pdf in enumerate(file):
        path = f"{PATH_TO_PDFS}/{i + 1}.pdf"

        if not os.path.exists(path):
            print(f"[INFO] We don't have this file, downloading...")
            
            url = name_of_pdf
            filename = path
            
            response = requests.get(url)
            
            if response.status_code == 200:
                with open(filename, "wb") as file:
                    file.write(response.content)
                    print(f"File downloaded in path {filename} as {i + 1}")
            else:
                print(f"Can't download. Status code: {response.status_code}")
                continue
        else:
            print(f"[INFO] File {i} in path: {path} is downloaded!")