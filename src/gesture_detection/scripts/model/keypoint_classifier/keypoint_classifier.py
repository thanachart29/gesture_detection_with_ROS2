#!/home/pumid/Desktop/athome/bin/python3
# -*- coding: utf-8 -*-
import numpy as np
import tensorflow as tf
import os
print("This module is in {}" .format(os.path.dirname(os.path.realpath(__file__))))
print("Your are using Tensorflow library")

class KeyPointClassifier(object):
    def __init__(self, model_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "new_keypoint_classifier.tflite")):
        self.interpreter = tf.lite.Interpreter(model_path=model_path)
        self.interpreter.allocate_tensors()
        self.input_details = self.interpreter.get_input_details()
        self.output_details = self.interpreter.get_output_details()

    def __call__(
        self,
        landmark_list,
    ):
        input_details_tensor_index = self.input_details[0]['index']
        self.interpreter.set_tensor(
            input_details_tensor_index,
            np.array([landmark_list], dtype=np.float32))
        self.interpreter.invoke()

        output_details_tensor_index = self.output_details[0]['index']

        result = self.interpreter.get_tensor(output_details_tensor_index)

        result_index = np.argmax(np.squeeze(result))

        return result_index
