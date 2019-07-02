def alphabet_position(letter):
 high = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
 low = 'abcdefghijklmnopqrstuzwxyz'
 if letter in low:
        return low.index(letter)
 else:
        return high.index(letter)
 

def rotate_char (mess,rot):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    upperalpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    encrypted = ''
    for char in mess:
        if char == ' ':
            encrypted = encrypted + ' '
        
        elif char in alphabet:
               rotated_index = alphabet.index(char) + rot
               if rotated_index < 26:
                    encrypted = encrypted + alphabet[rotated_index]
               else:
                    encrypted = encrypted + alphabet[rotated_index % 26]
        else:
            if char in upperalpha:
                rotated_index = upperalpha.index(char) + rot
                if rotated_index < 26:
                    encrypted = encrypted + upperalpha[rotated_index]
                else:
                    encrypted = encrypted + upperalpha[rotated_index % 26]
        if not char.isalpha():
            encrypted = encrypted + char        
                
                                        
    return encrypted
