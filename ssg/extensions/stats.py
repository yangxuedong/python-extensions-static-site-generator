from ssg import hooks
import time

start_time = None
total_written = 0


@hooks.register("start_build")
def start_build():
    global start_time
    start_time = datetime.now()


@hooks.register("written")
def written():
    global total_written
    total_written += total_written


@hooks.register("stats")
def stats():
    final_time = datetime.now() - start_time
    average = final_time / total_written if total_written != 0 else average = None
    report = "Converted: {} . Time: {:.2f} sec . Avg: {:,4f} sec/file"
    print(report.format(total_written, final_time, average))




