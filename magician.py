
#!/usr/bin/python
from Bot import Bot
from Keys import Keys
import sched
import threading
import random
import time

bot = Bot()

def job(key):
    bot.click(Keys.key[key], 0.2)
    bot.click(Keys.key[key], 0.2)

def buffing():
    s = sched.scheduler(time.time, time.sleep)
    s.enter(45, 1, job, ('s',))
    s.enter(40, 1, job, ('d',))
    s.enter(120, 1, job, ('f',))
    s.enter(120, 1, job, ('3',))
    s.enter(180, 1, job, ('4',))
    # s.enter(180, 1, job, ('5',))
    s.enter(240, 1, job, ('2',))
    s.enter(240, 1, job, ('1',))
    s.enter(360, 1, job, ('6',))
    s.enter(10, 1, job, ('LSHIFT',))
    s.enter(120, 1, job, ('g',))
    s.enter(60, 1, job, ('h',))
    s.run()

def roaming():
    while True:
        steps_clicks = 0
        ctrl_clicks = 0

        for i in range(50):
            if random.random() < 0.1:
                bot.click(Keys.key['LEFT'], 1)
            else:
                bot.click(Keys.key[random.choice(['CTRL', 'x'])], 0.2)
                ctrl_clicks += 1

            steps_clicks += 1
            if steps_clicks >= 3 and ctrl_clicks >= 5:
                break

        steps_clicks = 0
        ctrl_clicks = 0

        for i in range(50):
            if random.random() < 0.1:
                bot.click(Keys.key['RIGHT'], 1)
            else:
                bot.click(Keys.key[random.choice(['CTRL', 'x'])], 0.2)
                ctrl_clicks += 1

            steps_clicks += 1
            if steps_clicks >= 3 and ctrl_clicks >= 5:
                break

        if random.random() < 0.3:
            bot.jump(Keys.key['v'], Keys.key['b'], 2)

def main():
    time.sleep(1)

    t1 = threading.Thread(target=buffing)
    t2 = threading.Thread(target=roaming)
    t1.start()


if __name__ == "__main__":
    main()
