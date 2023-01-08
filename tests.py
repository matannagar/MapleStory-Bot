
#!/usr/bin/python
from random import randrange

from Bot import Bot
from Keys import Keys

import time


def main():
    bot = Bot()
    time.sleep(1)

    letters = ['a',
    's',
    'd',
    'f',
    'g',
    'h',
    'j',
    'k',
    'l']
    for c in letters:
        bot.click(Keys.key[c], 0.1)

if __name__ == "__main__":
    main()
