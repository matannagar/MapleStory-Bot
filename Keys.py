class Keys:
  # Coordinates of the keys on osk.png
  key = {}

  # Add digits 1-9
  key[str(0)] = [595, 100]
  for i in range(1,10):
    key[str(i)] = [90 + 50 * i, 100]

  # Add letters q-p
  for i, letter in enumerate('qwertyuiop'):
    key[letter] = [100 + 50 * i, 150]
  
  # Add letters a-l
  for i, letter in enumerate('asdfghjkl'):
    key[letter] = [115 + 50 * i, 200]
  
  # Add letters z-m
  for i, letter in enumerate('zxcvbnm'):
    key[letter] = [140 + 50 * i, 230]
  
  # Add special keys
  key['ESC'] = [20, 60]
  key['~'] = [100, 90]
  key['.'] = [805, 150]
  key[' '] = [480, 185]
  
  # Add navigation keys
  key['RIGHT'] = [700, 260]
  key['DOWN'] = [650, 260]
  key['LEFT'] = [600, 260]
  key['UP'] = [650, 230]

# Add function keys
  key['BACKSP'] = [1080, 55]
  key['ENTER'] = [1100, 250]
  key['PGUP'] = [1250, 55]
  key['PGDN'] = [1250, 90]
  key['HOME'] = [1180, 55]
  key['END'] = [1180, 90]
  
  # Add modifier keys
  key['LSHIFT'] = [50, 230]
  key['CTRL'] = [90, 260]
  key['ALT'] = [190, 260]
  
  # Add function keys
  key['INS'] = [1180, 125]
  key['DEL'] = [1100, 85]
  key['END'] = [1185, 85]
  key['PRTSCN'] = [1180, 150]
