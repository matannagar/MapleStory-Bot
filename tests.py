
#!/usr/bin/python
from Bot import Bot
from Keys import Keys

import time

def main():
    bot = Bot()
    time.sleep(1)

    # for c in 'qwertyuiop':
    #     bot.click(Keys.key[c], 0.1)

    # for c in 'asdfghjkl':
    #     bot.click(Keys.key[c], 0.1)

    # for c in 'zxcvbnm':
    #     bot.click(Keys.key[c], 0.1)

    # # Test digits 0-9
    # for i in range(10):
    #     bot.click(Keys.key[str(i)], 0.1)

    # special_keys = ['ESC', '~', '.', ' ']
    # for i in special_keys:
    #     bot.click(Keys.key[str(i)], 0.1)

    nav_keys = ['RIGHT', 'LEFT', 'UP', 'DOWN']
    for i in nav_keys:
        bot.click(Keys.key[str(i)], 0.1)

    # mod_keys = ['LSHIFT', 'CTRL', 'ALT']
    # for i in mod_keys:
    #     bot.click(Keys.key[str(i)], 0.1)

    # # # 'BACKSP', 'ENTER','PRTSCN','DEL',
    # func_keys = ['HOME','PGUP','END','PGDN','INS']
    # for i in func_keys:
    #     bot.click(Keys.key[str(i)], 0.1)

if __name__ == "__main__":
    main()
