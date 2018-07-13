# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 19:19:07 2018

@author: Chiranjeev
"""

import tensorflow as tf
 
# Creating placeholders
a = tf. placeholder(tf.float32)
b = tf. placeholder(tf.float32)
 
# Assigning multiplication operation w.r.t. a &amp;amp; b to node mul
mul = a*b
 
# Create session object
sess = tf.Session()
 
# Executing mul by passing the values [1, 3] [2, 4] for a and b respectively
output = sess.run(mul, {a: [1,3], b: [2, 4]})
print('Multiplying a b:', output)