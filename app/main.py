import pandas as pd
from fastapi import FastAPI, File, UploadFile
# from db import csv_validate, sort_by_danger_rate, validation_pydantic, save_to_mongodb
import uvicorn
from fastapi import FastAPI

app = FastAPI(title="terrorists")

# @app.post("/top-threats")   
# def top_threats(file: UploadFile | None = File(default=None)):
#     df = csv_validate(file)
#     df = sort_by_danger_rate(df)
#     terrorists_list = validation_pydantic(df)
#     save_to_mongodb(terrorists_list)
#     return {
#         "count": len(terrorists_list),
#         "top": terrorists_list}



from fastapi import FastAPI, File, UploadFile
import pandas as pd
from df_handler import create_risk_level, fill_manufacturer
from db import create_SQL, insert_to_SQL

app = FastAPI()





@app.post("/upload")
def upload_file(file: UploadFile = File(...)):
    df = pd.read_csv(file.file)
    df = pd.DataFrame(df)
    df = create_risk_level(df)
    df = fill_manufacturer(df)
    create_SQL()
    added = insert_to_SQL(df)
    file.file.close()
    return {
"status": "success",
"inserted_records": 20
}




if __name__ == '__main__':
    uvicorn.run("main:app", host="localhost", port=8000)
