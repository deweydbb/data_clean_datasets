from error_generator import Explicit_Missing_Value
from error_generator import Implicit_Missing_Value
from error_generator import Typo_Butterfingers
from error_generator import List_selected
from error_generator import Error_Generator
from error_generator import Read_Write

dataset,dataframe = Read_Write.read_csv_dataset("../datasets/adults/adults_clean.csv")

myselector=List_selected()
mygen=Error_Generator()
mymethod=Implicit_Missing_Value(dic={
                "phone number":"11111111",
                "education":"Some college",
                "Blood Pressurse":"0",
                "workclass":"?",
                "date":"20010101",
                "Ref_ID":"-1",
                "age":"0",
                "Birthday":"20010101",
                "EVENT_DT":"20030101",
            })

new_dataset=mygen.error_generator(method_gen=mymethod,selector=myselector,percentage=5,dataset=dataset,mute_column=[0, 3, 10])

mymethod=Implicit_Missing_Value(dic={
                "city":"New York"
            })

new_dataset=mygen.error_generator(method_gen=mymethod,selector=myselector,percentage=0.5,dataset=new_dataset,mute_column=[0,1,2,3,4,5,6,7,8,9,11])

mymethod=Implicit_Missing_Value(dic={
                "city":"Alabama",
            })

new_dataset=mygen.error_generator(method_gen=mymethod,selector=myselector,percentage=0.5,dataset=new_dataset,mute_column=[0,1,2,3,4,5,6,7,8,9,11])


mymethod=Explicit_Missing_Value()

new_dataset=mygen.error_generator(method_gen=mymethod,selector=myselector,percentage=5,dataset=new_dataset,mute_column=[0])







mymethod=Typo_Butterfingers(prob=0.03)
new_dataset=mygen.error_generator(method_gen=mymethod,selector=myselector,percentage=8,dataset=new_dataset,mute_column=[0])


Read_Write.write_csv_dataset("../datasets/adults/dirty.csv".format(mymethod.name), new_dataset)