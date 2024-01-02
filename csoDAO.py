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
        formatted_data = getFormatted(dataset)
        print(json.dumps(formatted_data), file=fp)
        print("Debug: Data written to cso-formatted.json")

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
        result[label0] = {}
        print(label0)

        for dim1 in range(0, sizes[1]):
            currentId = ids[1]
            index = dimensions[currentId]["category"]["index"][dim1]
            label1 = dimensions[currentId]["category"]["label"][index]
            result[label0][label1] = {}

            for dim2 in range(0, sizes[2]):
                currentId = ids[2]
                index = dimensions[currentId]["category"]["index"][dim2]
                label2 = dimensions[currentId]["category"]["label"][index]
                result[label0][label1][label2] = {}

                # Check if there is a dimension at index 3 before accessing it
                for dim3 in range(0, sizes[3]):
                    currentId = ids[3]
                    index = dimensions[currentId]["category"]["index"][dim3]
                    label3 = dimensions[currentId]["category"]["label"][index]
                    result[label0][label1][label2][label3] = {}

                    if len(sizes) > 4:
                        for dim4 in range(0, sizes[4]):
                            currentId = ids[4]
                            index = dimensions[currentId]["category"]["index"][dim4]
                            label4 = dimensions[currentId]["category"]["label"][index]
                            print("\t\t\t",label4, " ", values[valuecount])
                            result[label0][label1][label2][label3][label4] = int(values[valuecount])

                            db_values = (label0, label1, label2, label3, label4, int(values[valuecount]))
                            pointsDAO.create(db_values)

                        valuecount += 1
        
    return result
    
if __name__ == "__main__":
    getFormattedAsFile("PPA04")