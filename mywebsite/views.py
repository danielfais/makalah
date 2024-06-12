from django.shortcuts import render

def index(request):
    context = {
        'heading': 'Cryptography Algorithm',
        'input_text_rsa': '',
        'public_key': '',
        'private_key': '',
        'output_text_rsa': '',
    }
    if request.method == 'POST':
        action = request.POST.get('action')

        if action in ['EncryptRSA', 'DecryptRSA']:
            context['input_text_rsa'] = request.POST['message']
            if action == 'EncryptRSA':
                public_key = context['public_key'].split(',')
                e, n = int(public_key[0]), int(public_key[1])
                context['output_text_rsa'] = rsa_encrypt(context['input_text_rsa'], e, n)
            elif action == 'DecryptRSA':
                private_key = context['private_key'].split(',')
                d, n = int(private_key[0]), int(private_key[1])
                context['output_text_rsa'] = rsa_decrypt(context['input_text_rsa'], d, n)

    return render(request, 'index.html', context)

def rsa_encrypt(plaintext, e, n):
    e = int(e)
    n = int(n)
    ciphertext = [pow(ord(char), e, n) for char in plaintext]
    return ' '.join(map(str, ciphertext))

def rsa_decrypt(ciphertext, d, n):
    d = int(d)
    n = int(n)
    ciphertext = list(map(int, ciphertext.split()))
    plaintext = ''.join([chr(pow(char, d, n)) for char in ciphertext])
    return plaintext
