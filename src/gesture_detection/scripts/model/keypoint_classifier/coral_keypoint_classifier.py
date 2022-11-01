#!/home/pumid/Desktop/athome/bin/python3
# -*- coding: utf-8 -*-
import numpy as np
import sys
import os
from pycoral.utils.edgetpu import make_interpreter
# import tensorflow as tf

class CoralKeyPointClassifier(object):
    def __init__(self, model_path='src/gesture_detection/scripts/model/keypoint_classifier/keypoint_classifier.tflite'):
        try:
            self.interpreter = make_interpreter(model_path_or_content= model_path)
        except ValueError:
            print('please connect your TPU device')
            exit()
        # self.interpreter = tf.lite.Interpreter(model_path=model_path, num_threads=1)
        self.interpreter.allocate_tensors()
        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()

    def __call__(self, landmark_list,):
        input_details_tensor_index = self.input_details[0]['index']
        self.interpreter.set_tensor(
            input_details_tensor_index,
            np.array([landmark_list], dtype=np.float32))
        self.interpreter.invoke()

        output_details_tensor_index = self.output_details[0]['index']

        result = self.interpreter.get_tensor(output_details_tensor_index)

        result_index = np.argmax(np.squeeze(result))

        return result_index