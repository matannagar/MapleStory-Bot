
#!/usr/bin/python
from Bot import Bot
from Keys import Keys
import sched
import threading
import random
import time

bot = Bot()

def job(key):
    bot.click(Keys.key[key], 0.1)

def buffing():
    s = sched.scheduler(time.time, time.sleep)
    s.enter(45, 1, job, ('s'))
    s.enter(40, 1, job, ('d'))
    s.enter(120, 1, job, ('f'))
    s.enter(360, 1, job, ('6'))
    s.enter(180, 1, job, ('5'))
    s.enter(180, 1, job, ('4'))
    s.enter(120, 1, job, ('5'))
    s.enter(240, 1, job, ('1'))
    s.enter(240, 1, job, ('2'))
    s.run()
    # sched.scheduler.every(45).seconds.do(buff, 's')
    # sched.scheduler.every(40).seconds.do(buff, 'd')
    # sched.scheduler.every(120).seconds.do(buff, 'f')
    # sched.scheduler.every(360).seconds.do(buff, '6')
    # sched.scheduler.every(180).seconds.do(buff, '5')
    # sched.scheduler.every(180).seconds.do(buff, '4')
    # sched.scheduler.every(120).seconds.do(buff, '5')
    # sched.scheduler.every(240).seconds.do(buff, '1')
    # sched.scheduler.every(240).seconds.do(buff, '2')
    # start_time = time.time()

    # while True:
    #     now = time.time()
    #     if now - start_time > 45:
    #         bot.click(Keys.key['s'], 0.1)
    #     if now - start_time > 40:
    #         bot.click(Keys.key['d'], 0.1)
    #     if now - start_time > 120:
    #         bot.click(Keys.key['f'], 0.1)
    #     if now - start_time > 360:
    #         bot.click(Keys.key['6'], 0.1)
    #     if now - start_time > 180:
    #         bot.click(Keys.key['5'], 0.1)
    #     if now - start_time > 180:
    #         bot.click(Keys.key['4'], 0.1)
    #     if now - start_time > 120:
    #         bot.click(Keys.key['5'], 0.1)
    #     if now - start_time > 240:
    #         bot.click(Keys.key['1'], 0.1)
    #     if now - start_time > 240:
    #         bot.click(Keys.key['2'], 0.1)
    #     now = time.time()


def roaming():
    steps_clicks = 0
    ctrl_clicks = 0

    for i in range(50):
        if random.random() < 0.3:
            bot.click(Keys.key['LEFT'], 2)
        else:
            bot.click(Keys.key[random.choice(['CTRL', 'x'])], 0.2)
            ctrl_clicks += 1

        steps_clicks += 1
        if steps_clicks >= 3 and ctrl_clicks >= 10:
            break

    steps_clicks = 0
    ctrl_clicks = 0

    for i in range(50):
        if random.random() < 0.3:
            bot.click(Keys.key['RIGHT'], 2)
        else:
            bot.click(Keys.key[random.choice(['CTRL', 'x'])], 0.2)
            ctrl_clicks += 1

        steps_clicks += 1
        if steps_clicks >= 3 and ctrl_clicks >= 10:
            break
    
    bot.jump(Keys.key['v'], Keys.key['b'], 2)
    bot.jump(Keys.key['v'], Keys.key['b'], 2)

def main():
    time.sleep(1)

    t1 = threading.Thread(target=buffing)
    t2 = threading.Thread(target=roaming)
    t1.start()
    t2.start()
    


    # for _ in range(random.randint(1, 5)):
    #     bot.click(Keys.key['RIGHT'], 0.1)
    #     bot.click(Keys.key['v'], 0.1)
    #     time.sleep(1)
    # for _ in range(5):
    #     bot.jump(Keys.key['v'], Keys.key['b'], 2)
    #     time.sleep(1)

if __name__ == "__main__":
    main()
