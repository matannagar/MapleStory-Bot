
#!/usr/bin/python
from Bot import Bot
from Keys import Keys

import time

def main():
    bot = Bot()
    time.sleep(1)
    for _ in range(5):
        bot.jump(Keys.key['v'], Keys.key['b'], 2)
        time.sleep(1)

if __name__ == "__main__":
    main()
