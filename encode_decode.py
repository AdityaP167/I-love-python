import string
def encode(message,shift,lower_letters):
    result = ['']
    for x in message:
        if x in lower_letters:    
            index = lower_letters.index(x)
            index += shift
            if index > 25:
                index -= 26
            result.append(lower_letters[index])
        elif x == ' ':
            result.append(' ')
        else:
            result.append(x)
    encoded_message = ''.join(result)
    return encoded_message

def decode(message,shift,lower_letters):
    result = ['']
    for x in message:
        if x in lower_letters:
            index = lower_letters.index(x)
            index -= shift
            result.append(lower_letters[index])
        elif x == ' ':
            result.append(' ')
        else:
            result.append(x)
    decoded_message = ''.join(result)
    return decoded_message


lower_letters = list(string.ascii_lowercase)

repeat = 'yes'
while repeat == 'yes':
    operation = input("Type \"encode\" to encrypt, type \"decode\" to decrypt:").lower()
    if operation == 'encode':
        message = input("Type your message:").lower()
        shift = int(input("Type shift number:"))
        print(f"encoded result is: {encode(message,shift,lower_letters)}")

    elif operation == 'decode':
        message = input("Type your message:").lower()
        shift = int(input("Type shift number:"))
        print(f"decoded result is: {decode(message,shift,lower_letters)}")
    again = input("Type 'yes' if you want to go again. Otherwise type 'no'.")
    if again == 'no':
        repeat = 'no'
        
