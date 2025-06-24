'''
user input as list of mob=vies
dump all  data in csv files
for any which is not found print message the movie is not found'''
import requests
import json
import csv
def im():
    l=[]
    k=True
    while k==True:
        name = str(input("enter movie or series"))
        l.append(name)
        try:
            n=int(input("enter 1 to continue or 2 to exit"))
        except Exception as e:
            continue
        if n==2:
            k=False
    return l

def search(l,file_path,api="af60a0ec"):
    base_url="http://www.omdbapi.com/"
    results =[]
    for i in l:
        params= {

        "t": i,
        "apikey":api
        }
        response = requests.get(url=base_url, params=params)
        data = response.json()

        if data.get("Response") == "True":
            results.append(data)
        else:
            print(f"The movie '{i}' was not found.")

    if results:
        with open(file_path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=results[0].keys())
            writer.writerows(results)

        

def read(file_path):
    with open(file_path,'r') as f:
        print(f.read())
        


if __name__=='__main__':
    
    

    mov = im()
    
    file_path = r"C:\Users\Naman\notes\NF\movie.csv"

    search(mov,file_path)
    read(file_path)

    
    


#200--success , 300--network,400-- client error ,500-- server error ,600 -- redirect
