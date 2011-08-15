import logging
from Queue import Queue
from threading import Thread

def threaded(items, func, num_threads=10, max_queue=200):
    """ Run a function against each output of a given 
    generator, distributing load over a given number of 
    threads. A queue size can be specfied to define the 
    number of items that will at most be stored on the 
    task queue before blocking the generator.
    """
    def queue_consumer():
        # This closure will be run as the main loop of each 
        # thread, handling exceptions in a slightly brutal 
        # manner (i.e. you may want to document them in a 
        # seperate table of the database you scrape into).
        while True:
            item = queue.get(True)
            try:
                func(item)
            except Exception, e:
                logging.exception(e)
            queue.task_done()

    queue = Queue(maxsize=max_queue)

    for i in range(num_threads):
        # Create the worker threads.
        t = Thread(target=queue_consumer)
        t.daemon = True
        t.start()

    for item in items:
        # Fill up the queue. This will block when max_size 
        # has been reached and only continue when items 
        # have been processed off the queue. This means that
        # when you are scraping a (quasi-)infinite listing,
        # only the required section of the listing will be 
        # read.
        queue.put(item, True)

    # wait for all tasks to be processed.
    queue.join()
