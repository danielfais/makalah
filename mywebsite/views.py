from django.shortcuts import render

def index(request):
    context = {
        'heading': 'Cryptography Algorithm',
        'input_text_vigenere': '',
        'key_vigenere': '',
        'output_text_vigenere': '',
        'input_text_affine': '',
        'key_a': '',
        'key_b': '',
        'output_text_affine': '',
    }

    if request.method == 'POST':
        action = request.POST.get('action')

        if action in ['EncryptVigenere', 'DecryptVigenere']:
            context['input_text_vigenere'] = request.POST['message']
            context['key_vigenere'] = request.POST.get('key', '')

            if action == 'EncryptVigenere':
                context['output_text_vigenere'] = vigenere_encrypt(context['input_text_vigenere'], context['key_vigenere'])
            elif action == 'DecryptVigenere':
                context['output_text_vigenere'] = vigenere_decrypt(context['input_text_vigenere'], context['key_vigenere'])

        elif action in ['EncryptAffine', 'DecryptAffine']:
            context['input_text_affine'] = request.POST['message']
            context['key_a'] = request.POST.get('key_a', '')
            context['key_b'] = request.POST.get('key_b', '')

            if action == 'EncryptAffine':
                context['output_text_affine'] = affine_encrypt(context['input_text_affine'], context['key_a'], context['key_b'])
            elif action == 'DecryptAffine':
                context['output_text_affine'] = affine_decrypt(context['input_text_affine'], context['key_a'], context['key_b'])

    return render(request, 'index.html', context)

def vigenere_encrypt(plaintext, key):
    ciphertext = ""
    key = ''.join(filter(str.isalpha, key)).upper()
    for i in range(len(plaintext)):
        shift = ord(key[i % len(key)]) - 65
        if plaintext[i].isalpha():
            if plaintext[i].isupper():
                ciphertext += chr((ord(plaintext[i]) + shift - 65) % 26 + 65)
            else:
                ciphertext += chr((ord(plaintext[i]) + shift - 97) % 26 + 97)
        else:
            ciphertext += plaintext[i]
    return ciphertext

def vigenere_decrypt(ciphertext, key):
    plaintext = ""
    key = ''.join(filter(str.isalpha, key)).upper()
    for i in range(len(ciphertext)):
        shift = ord(key[i % len(key)]) - 65
        if ciphertext[i].isalpha():
            if ciphertext[i].isupper():
                plaintext += chr((ord(ciphertext[i]) - shift - 65) % 26 + 65)
            else:
                plaintext += chr((ord(ciphertext[i]) - shift - 97) % 26 + 97)
        else:
            plaintext += ciphertext[i]
    return plaintext

def affine_encrypt(plaintext, a, b):
    a = int(a)
    b = int(b)
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                ciphertext += chr(((a * (ord(char) - 65) + b) % 26) + 65)
            else:
                ciphertext += chr(((a * (ord(char) - 97) + b) % 26) + 97)
        else:
            ciphertext += char
    return ciphertext

def affine_decrypt(ciphertext, a, b):
    a = int(a)
    b = int(b)
    plaintext = ""
    a_inv = mod_inverse(a, 26)
    if a_inv is None:
        return "No modular inverse for given a and m"
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                plaintext += chr(((a_inv * ((ord(char) - 65) - b)) % 26) + 65)
            else:
                plaintext += chr(((a_inv * ((ord(char) - 97) - b)) % 26) + 97)
        else:
            plaintext += char
    return plaintext

def mod_inverse(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None
