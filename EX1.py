from progress.bar import Bar
import time

bar = Bar('Как сильно я тебя люблю?', max=100)

for i in range(1000):
    time.sleep(0.01)
    bar.next()
bar.finish()