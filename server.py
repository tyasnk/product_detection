from fastapi import FastAPI
from handler import ModelHandler

app = FastAPI()

app.model_handler = None


@app.on_event("startup")
def startup_event():
    app.model_handler = ModelHandler(model_path="best_model.h5")


@app.get("/")
def ping():
    return "hi"


@app.get("/predict/{filename}")
def predict(filename):
    try:
        # For the data security purpose the category names was desensitized by the
        # comptition author
        category = app.model_handler.predict(f"image/{filename}")
    except FileNotFoundError:
        return {
            "id": filename,
            "status": 404,
            "error": "File not found. Make sure you put the image file in image folder"
        }
    category = int(category)
    return {"id": filename, "category": category, "status": 200}
