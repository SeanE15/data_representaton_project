import requests
import json
from pointsDAO import pointsDAO

urlBegining = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/"
urlEnd = "/JSON-stat/2.0/en"

def getAllAsFile(dataset):
    with open("cso.json", "wt") as fp:
        print(json.dumps(getAll(dataset)), file=fp)

def getAll(dataset):   
    url = urlBegining + dataset + urlEnd
    response = requests.get(url)
    return response.json()

def getFormattedAsFile(dataset):
    with open("cso-formatted.json", "wt") as fp:
        print(json.dumps(getFormatted(dataset)), file=fp)
  

def getFormatted(dataset):
    data = getAll(dataset)
    ids = data["id"]
    values = data["value"]
    dimensions = data["dimension"]
    sizes = data["size"]
    valuecount = 0
    result = {}
    
    for dim0 in range(0, sizes[0]):
        currentId = ids[0]
        index = dimensions[currentId]["category"]["index"][dim0]
        label0 = dimensions[currentId]["category"]["label"][index]
        result[label0]={}
        print(label0)
                        
        db_values = (label0, int(values[valuecount]))
        pointsDAO.create(*db_values)
                        
        valuecount+=1
        
    return result
    
if __name__ == "__main__":
    getFormattedAsFile("PPA04")