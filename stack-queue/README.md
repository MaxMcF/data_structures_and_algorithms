# Stacks and Queues

# By Max McFarland

# Purpose
This application is meant to show the application and usefullness of stacks and queues. The base of both classes come from the singlely linked list model, which uses nodes that have a linked value associated with them.

# Using Stacks
You can initialize a new stack by creating a new stack object. If you have a preexisting list of values that you wish to put into the stack, you can pass in an iterable on initialization. 
To put a new value onto the stack, use the push method, which sets the top of the stack equal to the inputted value, and links the previous top to the new top. 
To remove a value from the stack, use the pop method, which takes the top of the stack off and returns the node. The second from the top becomes the new stack top.

# Using Queues
You can initialize a new queue by creating a new queue object. If you have a prexising list of values that you wish to put into the queue, you can pass an iterable in on initialization.
Queues use the first in first out methodology, meaning when you enqueue a value, it puts it at the end of the queue, and likewise when you remove a value, it gets removed from the front of the queue. This means the values that have been in the queue the longest will get removed frist.

# Testing
To test the functionality of the stack and queue methods, pytest needs to be installed in your virtual environment. This can be done using pip, or any other virtual environment module. Running pytest on either queue.py or stack.py will run the various tests that have been written to test the functionality of the two files. 