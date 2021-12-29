"""
pickling ==> It is the process of storing python objects in the form of pickle file
"""
import pickle
# pickling a file
Actresses=["Shraddha kapoor","Jacquline fernandis","Kiara advani","Lisa","Shreya"]

with open("Actresses.pkl","wb") as file:
 pickle.dump(Actresses,file)

# Opening a pickle file
with open("Actresses.pkl","rb") as file2:
 actresses=pickle.load(file2)
 print(actresses)