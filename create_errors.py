from error_generator import Explicit_Missing_Value
from error_generator import Implicit_Missing_Value
from error_generator import Typo_Butterfingers
from error_generator import List_selected
from error_generator import Error_Generator
from error_generator import Read_Write
from error_generator.strategies.switch_value.outlier_integer.outlier_integer import Outlier_Integer
from error_generator.strategies.switch_value.switch_relationship.Switch_Relationship import Switch_Relationship
from error_generator.strategies.switch_value.random_domain.Random_Domain import Random_Domain

dataset,dataframe = Read_Write.read_csv_dataset("../datasets/adults/adults_clean.csv")


def create_typos(dataset):
    myselector=List_selected()
    mygen=Error_Generator()

    mymethod=Typo_Butterfingers(prob=0.15)
    new_dataset=mygen.error_generator(method_gen=mymethod,selector=myselector,percentage=45,dataset=dataset,mute_column=[0, 1, 9])

    Read_Write.write_csv_dataset("../datasets/adults/adults_dirty_typos.csv", new_dataset)


def create_missing_data(dataset):
    myselector=List_selected()
    mygen=Error_Generator()

    mymethod=Implicit_Missing_Value(dic={
                "0":"",
                "1":"null",
                "2":"?",
                "3":"NULL",
                "4":"unknown",
                "5":'""',
                "6":'N/A',
    })

    new_dataset=mygen.error_generator(method_gen=mymethod,selector=myselector,percentage=30,dataset=dataset,mute_column=[0])

    Read_Write.write_csv_dataset("../datasets/adults/adults_dirty_missing.csv", new_dataset)

def create_outlier(dataset):
    myselector=List_selected()
    mygen=Error_Generator()

    mymethod=Outlier_Integer()
    new_dataset=mygen.error_generator(method_gen=mymethod,selector=myselector,percentage=30,dataset=dataset,mute_column=[0, 2, 3, 4, 5, 6, 7, 8, 10, 11])

    Read_Write.write_csv_dataset("../datasets/adults/adults_dirty_outliers.csv", new_dataset)

def create_fn(dataset):
    myselector=List_selected()
    mygen=Error_Generator()

    mymethod=Switch_Relationship()
    new_dataset=mygen.error_generator(method_gen=mymethod,selector=myselector,percentage=30,dataset=dataset,mute_column=[0, 1, 2, 3, 4, 5, 7, 8, 9, 10, 11])

    Read_Write.write_csv_dataset("../datasets/adults/adults_dirty_fn.csv", new_dataset)

def create_domain(dataset):
    myselector=List_selected()
    mygen=Error_Generator()

    mymethod=Random_Domain()
    new_dataset=mygen.error_generator(method_gen=mymethod,selector=myselector,percentage=30,dataset=dataset,mute_column=[0])

    Read_Write.write_csv_dataset("../datasets/adults/adults_dirty_domain.csv", new_dataset)

# create_typos(dataset)
# create_missing_data(dataset)
# create_outlier(dataset)
# create_fn(dataset)
# create_domain(dataset)