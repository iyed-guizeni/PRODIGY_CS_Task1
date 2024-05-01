import re
def encryption(message,shift):
    message_for_encyption=message.split(" ")
    list_encrypted=[]
    for word in message_for_encyption:

        encypted_word=""
        for alpha in word:

            #traiting upper alphabet
            if re.match(r'[A-Z]', alpha):
                #print("yes")
                ascii_code = ord(alpha)
                ascii_alpha_shifted = ascii_code + shift
                #print(ascii_alpha_shifted)
                if ascii_alpha_shifted > 90 :
                    aux = ascii_alpha_shifted - 90
                    ascii_caeser_alpha = 64 + aux
                    encypted_word+=chr(ascii_caeser_alpha)
                else:
                    encypted_word += chr(ascii_alpha_shifted)

            #traiting lower alphabet
            elif re.match(r'[a-z]', alpha):
                ascii_code = ord(alpha)
                ascii_alpha_shifted = ascii_code + shift
                if ascii_alpha_shifted > 122:
                    aux = ascii_alpha_shifted - 122
                    ascii_caeser_alpha = 96 + aux
                    encypted_word+=chr(ascii_caeser_alpha)
                else:
                    encypted_word += chr(ascii_alpha_shifted)
            else:
                encypted_word += alpha
        list_encrypted.append(encypted_word)
    return ' '.join(list_encrypted)


def decryption(message,shift):
    message_for_decyption=message.split(" ")
    list_decrypted=[]
    for word in message_for_decyption:

        decypted_word=""
        for alpha in word:

            #traiting upper alphabet
            if re.match(r'[A-Z]', alpha):
                #print("yes")
                ascii_code = ord(alpha)
                ascii_alpha_shifted = ascii_code - shift
                #print(ascii_alpha_shifted)
                if ascii_alpha_shifted < 65 :
                    aux = 65 - ascii_alpha_shifted
                    ascii_caeser_alpha = 91 - aux
                    decypted_word+=chr(ascii_caeser_alpha)
                else:
                    decypted_word += chr(ascii_alpha_shifted)

            #traiting lower alphabet
            elif re.match(r'[a-z]', alpha):
                ascii_code = ord(alpha)
                ascii_alpha_shifted = ascii_code - shift
                if ascii_alpha_shifted < 97:
                    aux = 97 - ascii_alpha_shifted
                    ascii_caeser_alpha = 123 - aux
                    decypted_word+=chr(ascii_caeser_alpha)
                else:
                    decypted_word += chr(ascii_alpha_shifted)
            else:
                decypted_word += alpha
        list_decrypted.append(decypted_word)
    return ' '.join(list_decrypted)

choice = input("choice : \n for encryption : e \n for decryption : d \n")
message = input("enter message   ")
shift = int(input("enter the shift"))
if choice == 'e':
    encryption =  encryption(message,shift)
    print("after encyption : " , encryption)
else:
    decryption = decryption(message, shift)
    print("after decyption : " , decryption)


























