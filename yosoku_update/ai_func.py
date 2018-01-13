import tensorflow as tf
import json
from urllib2 import urlopen
import api_func

#ai_func
class ai_funcClass:
	def __init__(self):
		print ""

	def proc_run(self ,key ,field ):
		cls = api_func.api_funcClass()
		#get_apiData()
		#exit()
		# Model parameters
		W = tf.Variable([0.0], dtype=tf.float32)
		b = tf.Variable([0.0], dtype=tf.float32)
		# Model input and output
		x = tf.placeholder(tf.float32)
		y = tf.placeholder(tf.float32)
		linear_model = W*x + b

		# loss
		loss = tf.reduce_sum(tf.square(linear_model - y)) # sum of the squares
		# optimizer
		optimizer = tf.train.GradientDescentOptimizer(0.01)
		train = optimizer.minimize(loss)

		# training data
		y_train = cls.get_apiData(key, field  )
		cDim=[]
		iCt=0
		for xRow in range(len(y_train ) ):
			cDim.append( float(iCt)/100.0 )
			iCt +=1
	#	x_train = [0.01, 0.02 , 0.03, 0.04, 0.05 ]
		x_train = cDim
		print(x_train)
		print(y_train)
	#	y_train = [0.13, 0.12 , 0.06, 0.11, 0.13 ]
		# training loop
		print('#Start traning.')
		init = tf.global_variables_initializer()
		sess = tf.Session()
		sess.run(init) # reset values to wrong
		for i in range(1000):
			sess.run(train, {x: x_train, y: y_train})
			if i % 100 == 0:
				print( i, sess.run(W), sess.run(b) )

		# evaluate training accuracy
		curr_W, curr_b, curr_loss = sess.run([W, b, loss], {x: x_train, y: y_train})
		
		if(len(curr_W)) >0:
			print('W=' + str(curr_W[0]))
		if(len(curr_b ) >0):
			print( 'b='+ str(curr_b[0] ))
		print("W: %s b: %s loss: %s"%(curr_W, curr_b, curr_loss))
		#update
		if((len(curr_W) > 0) and (len(curr_b) > 0)):
			cls.update(key, field , curr_W[0],curr_b[0] )
	