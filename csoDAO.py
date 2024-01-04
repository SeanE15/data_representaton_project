import requests
import json
from pointsDAO import pointsDAO

# Base URL for CSO API
urlBeginning = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/"
urlEnd = "/JSON-stat/2.0/en"

def getAllAsFile(dataset):
    # Retrieve data from the CSO API for the given dataset and write it to a JSON file
    with open("cso.json", "wt") as fp:
        data = getAll(dataset)
        # Encapsulate the data in square brackets to create a JSON array
        json.dump([data], fp)

def getAll(dataset):   
    # Retrieve data from the CSO API for the given dataset
    url = urlBeginning + dataset + urlEnd
    response = requests.get(url)
    return response.json()

def getFormattedAsFile(dataset):
    # Retrieve and format data from the CSO API for the given dataset and write it to a JSON file
    with open("cso-formatted.json", "wt") as fp:
        formatted_data = getFormatted(dataset)
        # Encapsulate the formatted data in square brackets to create a JSON array
        json.dump([formatted_data], fp)
        print("Debug: Data written to cso-formatted.json")

def getFormatted(dataset):
    # Format data from the CSO API for the given dataset
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

                for dim3 in range(0, sizes[3]):
                    currentId = ids[3]
                    index = dimensions[currentId]["category"]["index"][dim3]
                    label3 = dimensions[currentId]["category"]["label"][index]
                    result[label0][label1][label2][label3] = {}

                    for dim4 in range(0, sizes[4] if len(sizes) > 4 else 0):
                        currentId = ids[4]
                        index = dimensions[currentId]["category"]["index"][dim4]
                        label4 = dimensions[currentId]["category"]["label"][index]
                        result[label0][label1][label2][label3][label4] = {}

                        # Check if there is a dimension at index 5 before accessing it
                        if len(sizes) > 5:
                            for dim5 in range(0, sizes[5] if len(sizes) > 5 else 0):
                                currentId = ids[5]
                                index = dimensions[currentId]["category"]["index"][dim5]
                                label5 = dimensions[currentId]["category"]["label"][index]
                                print("\t\t\t", label5, " ", values[valuecount])
                                result[label0][label1][label2][label3][label4][label5] = (values[valuecount])

                                db_values = (label0, label1, label2, label3, label4, label5, (values[valuecount]))
                                pointsDAO.create(db_values)
                        
                                valuecount += 1
        
    return result
    
if __name__ == "__main__":
    # Execute the script to retrieve and format data for a specific dataset 'PPA04'.
    getFormattedAsFile("PPA04")
