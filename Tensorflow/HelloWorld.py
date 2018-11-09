#####################################################
# Just disables the warning, doesn't enable AVX/FMA #
#####################################################
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

#####################################################
# Programa: Python TensorFlow prueba                #
#####################################################
import tensorflow as tf
hello = tf.constant('Hello, TensorFlow!')
sess = tf.Session()
print(sess.run(hello))
