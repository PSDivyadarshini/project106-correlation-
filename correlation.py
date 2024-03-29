import plotly_express as px
import csv
import numpy as  np

def getDataSource(data_path):
    marks=[]
    daysPresent=[]
    with open (data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)  
        for row in csv_reader:
            marks.append(float(row["Marks In Percentage"]))  
            daysPresent.append(float(row["Days Present"]))  

    return {"x":daysPresent,"y":marks}  

def findCorrelation(data_source):
    correlation=np.corrcoef(data_source["x"],data_source["y"])
    print("the correlation 'between Marks In Percentage' and 'Days Present' :",correlation[0,1])

def setUp():
    data_path = "106project.csv"
    data_source = getDataSource(data_path)
    findCorrelation(data_source)

    setUp(sssss)



