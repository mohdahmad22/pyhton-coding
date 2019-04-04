import tensorflow as tf
a=tf.constant(5.0)
b=tf.constant(6.0)
c=a*b
sess=tf.Session()
File_writer=tf.summary.FileWriter('f:\\pythonc',sess.graph)
print(sess.run(c))
sess.close()
