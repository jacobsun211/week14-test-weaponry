import pandas as pd
from fastapi import FastAPI, File, UploadFile
import uvicorn
from fastapi import FastAPI

app = FastAPI(title="weapons")





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
        "inserted_records": added
        }




if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
