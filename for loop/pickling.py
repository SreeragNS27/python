import pickle
students=[{"name":"alice","age":"20"},{"name":"bob","age":"22"}]
with open("students.pkl","wb") as file:
    pickle.dump(students,file)

with open("students.pkl","rb") as file:
    a=pickle.load(file)
print(a)