from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/writeName")
def write_name(name: str):
    return {"message": "The Code Has Been Changed for {name}"}

if __name__ == "__main__":
    # Uvicorn ile çalıştırıyoruz
    uvicorn.run(app, host="0.0.0.0", port=8000)
