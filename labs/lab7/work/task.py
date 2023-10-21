import random

def generate_key_hex(word):
    key = ""
    for _ in range(len(word)):
        key += random.choice("0123456789abcdef")  # Генерация случайной шестнадцатеричной цифры
    return key

def encrypt(plaintext, key):
    ciphertext = ""
    for i in range(len(plaintext)):
        char = plaintext[i]
        key_char = key[i % len(key)]
        encrypted_char = chr(ord(char) ^ ord(key_char))  # XOR операция над символами
        ciphertext += encrypted_char
    return ciphertext

def decrypt(ciphertext, key):
    decrypted_text = ""
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        key_char = key[i % len(key)]
        decrypted_char = chr(ord(char) ^ ord(key_char))  # XOR операция над символами
        decrypted_text += decrypted_char
    return decrypted_text

def find_possible_key(ciphertext, fragment):
    possible_keys = []
    for i in range(len(ciphertext) - len(fragment) + 1):
        possible_key = ""
        for j in range(len(fragment)):
            char = ciphertext[i + j]
            fragment_char = fragment[j]
            key_char = chr(ord(char) ^ ord(fragment_char))  # XOR операция над символами
            possible_key += key_char
        possible_keys.append(possible_key)
    return possible_keys

open_text = "С Новым Годом, друзья!"
key = generate_key_hex(open_text)
print("Ключ:", key)

# Шифрование
encrypted_text = encrypt(open_text, key)
print("Зашифрованный текст:", encrypted_text)

# Дешифрование
decrypted_text = decrypt(encrypted_text, key)
print("Дешифрованный текст:", decrypted_text)

# Поиск возможных ключей по шифротексту и фрагменту открытого текста
ciphertext = encrypt(open_text, key)
fragment = "С Новым"
possible_keys = find_possible_key(ciphertext, fragment)
print("Возможные ключи:", possible_keys)
