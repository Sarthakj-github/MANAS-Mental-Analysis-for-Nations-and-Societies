from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
import json
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
import model


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def hello():
    return "Hello"

@app.get("/api/data/mentalhealth")
async def mentaldata():
    file_path = "data.json"
    with open(file_path, 'r') as json_file:
        data = json.load(json_file)
    return data

@app.post("/data/disorders")
async def get_mental_health_data(request: Request):
    data  = await request.json()
    try:
        output_file_path = "fetchedData/input.json"
        with open(output_file_path, 'w') as json_file:
            json.dump(data, json_file)

        model.master_function(output_file_path)

        updated_data = await mentaldata()

        return JSONResponse(content=updated_data, status_code=200)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to save data: {str(e)}")

if __name__=='__main__':
    uvicorn.run(app, reload=True,host="localhost", port=5000)
