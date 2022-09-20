import tensorflow as tf
import numpy as np

input_dim = 2
output_dim = 1

x = tf.placeholder("float", [None, input_dim])
b = tf.Variable(tf.random_normal([output_dim]))
W = tf.Variable(tf.random_uniform([input_dim, output_dim], -1.0, 1.0)) #Weight 범위 설정?
y = tf.nn.sigmoid(tf.matmul(x, W) + b) #sigmoid?, Classification?

y_ = tf.placeholder("float", [None, output_dim])
loss = tf.reduce_mean(tf.square(y-y_)) 

train_step = tf.train.MomentumOptimizer(0.01, 0.97).minimize(loss) #Weight 값을 미분해서 찾는 것인데, Local Minimum 값에 수렴하도록 하는 것

init = tf.global_variables_initializer() #선언했던 모든 전역 변수 초기화 작동에 대한 선언
sess = tf.Session() #해당 세션을 받아옴

sess.run(init) #TensorFlow 실행! 실제 모든 변수 초기화

for i in range(100000 + 1):
    batch_xs = np.array([[0.0, 0.0], [0.0, 1.0], [1.0, 0.0], [1.0, 1.0]]) #input, output의 결과를 입력, Supervisor ML
    batch_ys = np.array([[0.0], [0.0], [0.0], [1.0]])
    
    sess.run(train_step, feed_dict = {x:batch_xs, y_:batch_ys}) #단지 선언했던 x, y_에 입력, 출력 데이터를 넣어줌 (학습)
    
    if(i % 500 ==0) :
        print(i)
        print(sess.run(y, feed_dict = {x:batch_xs, y_:batch_ys}))

