from PIL import Image
import numpy as np
from skimage import transform
import tensorflow as tf
from tensorflow.keras.models import Sequential, Model, load_model
from tensorflow.keras.layers import InputLayer, Input
from tensorflow.keras.layers import Conv2D, Dense, Flatten, Dropout, Activation
from tensorflow.keras.layers import BatchNormalization, Reshape, MaxPooling2D,\
    GlobalAveragePooling2D, GlobalMaxPooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint, ReduceLROnPlateau
from tensorflow.keras.applications.inception_v3 import InceptionV3
from tensorflow.keras.applications import DenseNet201, ResNet152V2
import efficientnet.tfkeras as enet


class ModelHandler:
    def __init__(self, model_path):
        self.model = load_model(model_path)

    def load_image(self, filename: str) -> np.array:
        """
        load image
        """
        np_image = Image.open(filename)
        np_image = np.array(np_image).astype('float32')/255
        np_image = transform.resize(np_image, (300, 300, 3))
        np_image = np.expand_dims(np_image, axis=0)
        return np_image

    def predict(self, filename: str) -> np.int:
        """
        predict image
        """
        np_image = self.load_image(filename=filename)
        pred_proba = self.model.predict(np_image)
        pred = np.argmax(pred_proba)
        return pred
