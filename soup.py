import requests
from bs4 import BeautifulSoup
url = 'https://www.namal.edu.pk'  
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
# Step 3: Extract data
paragraphs = soup.find_all('p')
file_path = "G:\\webscraping\\task3.txt"
with open(file_path, "a") as f:
    for para in paragraphs:
        f.write(para.text + "\n")  # Write each paragraph to the file followed by a newline

print(f"File saved successfully at {file_path}")
f = open("G:\\webscraping\\task3.txt", "r")
print(f.read())
f.close()