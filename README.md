# Product Detection

Product detection model based on [this](https://www.kaggle.com/c/shopee-product-detection-open) competition. Deployed using FastAPI.

## Setup

This project use Python 3.8

Setup virtual environment
```
python -m venv venv
source venv/bin/venv
```

Install dependencies
```
pip install requirements.txt
```

Download saved model
```
wget https://www.dropbox.com/s/p2cmys23oosxl0k/best_model.h5
```

## Run

Run server using uvicorn

```
uvicorn server:app --reload
```

Usage example
```
GET http://127.0.0.1:8000/predict/image4.jpg
```
make sure your image in `image` directory
