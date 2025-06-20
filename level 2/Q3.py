'''
3. Build a small command-line app to track quiz scores,
stored in a CSV file.
'''


import json
import os
def load_scores(f):
    l=[]
    if not os.path.exists(f):
        return l
    try:
        if f.endswith('.csv'):
            with open(f,'r') as file:
                    lines=file.readlines()
                    for line in lines:
                        try:
                            n,s=line.strip().split(',')
                            l.append((n,int(s)))
                        except ValueError:
                            print(f"bad line:{line.strip()}")
        elif f.endswith('.json'):
            with open(f,'r') as file:
                data =json.load(file)
                for item in data:
                    if isinstance(item,dict) and "name" in item and "score" in item:
                        l.append((item["name"],int(item["score"])))
        


    except Exception as e:
        print(f"error:{e}")
    return l
def inp():
    name= str(input("enter name"))
    while True:
        try:
            score= int(input("enter score"))
            break
        except ValueError:
            print("invalid score")
    return name,score
def save_scores(f,l):
    try:
        if f.endswith('.csv'):
                with open(f,'w') as file:
                    for i in l:
                        s,t=i[0],i[1]
                        file.write(f"{s},{t}\n")
        elif  f.endswith('.json'):
            with open(f,'w') as file:
                json.dump([{"name": name, "score": score} for name, score in l], file, indent=2)
    

    except Exception as e:
        print("error:",e)
    

def add_score(l,name,score,f):
    
    l.append((name,score))
    save_scores(f,l)
    

def top_n(l):
    try:
        n = int(input("Enter number of top scores"))
        sorted_list = sorted(l, key=lambda x: x[1], reverse=True)
        return sorted_list[:n]
    except ValueError:
        print("Invalid input.")
        return []

    
def delete(f):
    with open(f,'w') as file:
        if f.endswith('.json'):
            file.write('[]')
        else:
            file.write('')
    
            


def quiz(f):
    
    

    while True:

        try:
            n= int(input("press:\n 1)Show the top N scores \n 2)add new score \n 3)exit  4)delete\n"))
        except ValueError:
            print("invalid choice")
            continue
        l=load_scores(f)
        match n:
            case 1:
                
                t=top_n(l)
                print("top scores:\n")
                for name,score in t:
                    print(f"{name},{score}\n")
                
            case 2: 
                name,score=inp()
                add_score(l,name,score,f)
                print("score saved")
            case 3:
                return 
            case 4:
                delete(f)
                l=[]
                print("score deleted")
            case _:
                print("invalid choice")
        
    

    

if __name__ == "__main__" :
    
    f= input("enter filename").strip()
    quiz(f)
