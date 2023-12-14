import pandas as pd
import pymongo

uri  = r"mongodb+srv://nikhilsinghxlx:Nikhilsinghxlx@cluster0.9kjhcgg.mongodb.net/?retryWrites=true&w=majority"
DataBase_Name = "Projects" 
Collection_Name = "Cement_Strength"

if __name__=="__main__":
    df = pd.read_csv("Notebooks/cement_data.csv")

    # Rename columns by extracting the first word
    new_columns = ["cement", "slag", "flyash", "water", "superplasticizer", "coaseseaggregate", "fineaggregate", "age", "strength"]
    df.columns = new_columns

    # connection with the database
    client = pymongo.MongoClient(uri)

    # database creation
    db = client[DataBase_Name]

    # collection creation within the database
    collection = db[Collection_Name]

    # converting DataFrame into json fromat
    data_in_json = df.to_dict(orient="records")

    # insert data into collection 
    collection.insert_many(data_in_json)

    print("Data is Successfully Inserted")