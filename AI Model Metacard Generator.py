class AI:
    def __init__(self,model_name,Domain,Alg_type,Accuracy,Data,dep_status):
        self.model_name = model_name
        self.Domain = Domain
        self.Alg_type = Alg_type
        self.Accuracy = Accuracy
        self.Data = Data
        self.dep_status = dep_status

    def display(self):
        print("\n Welcome to the AI Model MetaCard Generator!! \n")
        print(f" The model of the AI is : {self.model_name}")
        print(f"The Domain of the Model is :{self.Domain}")
        print(f"The algorithm of the model is :{self.Alg_type}")
        print(f"The Data of the model is :{self.Data}")
        print(f"The accuracy of the model is :{self.Accuracy}")
        print(f"The deployment status of the model is :{self.dep_status}")


model_name = input("Enter your AI model name :")

Domain = (input("Select you domain : 1. Education 2. healthcare 3.Management  4.transport"))
if Domain == "1" :
    Domain = "Education "
    print(Domain)
elif Domain == "2":
    Domain = "Healthcare"
    print(Domain)
elif Domain == "3" :
    Domain = "Management"
    print(Domain)
elif Domain == "4":
    Domain = "transport"
    print(Domain)

Alg_type = (input("Enter the algorithm type : 1.prediction 2.classification 3.Regression 4.Decision tree"))
if Alg_type == "1":
    Alg_type = "prediction"
    print(Alg_type)
elif Alg_type == "2":
    Alg_type = "classification"
    print(Alg_type)
elif Alg_type == "3":
    Alg_type = "Regression"
    print(Alg_type)
elif Alg_type == "4" :
    Alg_type = "Decision Tree classifier"
    print(Alg_type)
Data = 1
if Data :
     Data = (" The Data is  a processed Data")
else :
    Data = ("The data is a raw data")
Accuracy = float(input("Enter the Accuracy of the model :"))

dep_status = [100,200,300,400] # consider by the avg of the model trained
if dep_status :
    dep_status = ("The model is trained more than 300 times")
else:
    dep_status =(" the model is not yet trained")

AI_mod = AI(model_name,Domain,Alg_type,Accuracy,Data,dep_status)
AI_mod.display()
