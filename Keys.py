class Keys:
  # Coordinates of the keys on osk.png
  key = {}

  # Add digits 0-9
  for i in range(10):
    key[str(i)] = [190 + 70 * i, 55]

  # Add letters q-p
  for i, letter in enumerate('qwertyuiop'):
    key[letter] = [100 + 75 * i, 85]
  
  # Add letters a-l
  for i, letter in enumerate('asdfghjkl'):
    key[letter] = [115 + 25 * i, 200]
  
  # Add letters z-m
  for i, letter in enumerate('zxcvbnm'):
    key[letter] = [140 + 60 * i, 350]
  
  # Add remaining keys
  key['ESC'] = [20, 60]
  key['~'] = [100, 90]
  key['.'] = [805, 150]
  key[' '] = [480, 185]
  key['BACKSP'] = [1080, 55]
  key['ENTER'] = [1100, 250]
  key['LSHIFT'] = [90, 150]
  key['CTRL'] = [115, 380]
  key['INS'] = [1180, 125]
  key['DEL'] = [1100, 85]
  key['END'] = [1185, 85]
  key['RIGHT'] = [1110, 380]
  key['LEFT'] = [950, 380]
  key['UP'] = [950, 150]
  key['DOWN'] = [950, 185]
  key['PGUP'] = [1250, 55]
  key['PGDN'] = [1250, 90]
  key['HOME'] = [1180, 55]
  key['END'] = [1180, 90]
  key['ALT'] = [260, 185]
  key['PRTSCN'] = [1180, 150]
