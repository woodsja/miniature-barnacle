import tensorflow as tf

# queue up file names
filename_queue = tf.train.string_input_producer(
    tf.train.match_filenames_once("./training/*.png"))

# read an image
image_reader = tf.WholeFileReader()

# read a file from the queue, ignoring the first value in the tuple
_, image_file = image_reader.read(filename_queue)

# decode image from PNG to a tensor
image = tf.image.decode_png(image_file)

# start a session with example output
with tf.Session() as sess:
    tf.initialize_all_variables().run()

    image_tensor = sess.run([image])
    print(image_tensor)

    coord.request_stop()
    coord.join(threads)


