from QtGraphVisuals import quick_view
import onnx
from tensorflow import keras

onnx_model = onnx.load('my_model.onnx')
keras_model = keras.applications.ResNet50()
quick_view({'onnx': onnx_model, 'keras': keras_model})
