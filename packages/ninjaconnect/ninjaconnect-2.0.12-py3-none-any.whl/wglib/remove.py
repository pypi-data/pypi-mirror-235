import secrets
import base64

def generate_base64_key():
    key = secrets.token_bytes(44)  # Generate a random 16-byte key
    key_base64 = base64.b64encode(key).decode('utf-8')
    return key_base64

generated_key = generate_base64_key()
print(generated_key)
