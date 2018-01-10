import tensorflow as tf

file_names = tf.train.match_filenames_once("1.png")

# queue up file names
filename_queue = tf.train.string_input_producer(file_names)

# read an image
reader = tf.WholeFileReader()

# read a file from the queue, ignoring the first value in the tuple
key, value = reader.read(filename_queue)

# decode image from PNG to a tensor
image = tf.image.decode_png(value)

init_op = tf.global_variables_initializer()

# start a session with example output
with tf.Session() as sess:

    # coordinate loading of image files
    coord = tf.train.Coordinator()
    threads = tf.train.start_queue_runners(coord=coord)

    # get an image tensor
    image_tensor = sess.run([image])
    print(image_tensor)

    # finish off filename queue coordinator
    coord.request_stop()
    coord.join(threads)
