import os
import base64
import hashlib
from cryptography.fernet import Fernet


key_pair_file = "my_key_pairs.txt"
key_file = "my_encryption_key.key"
password_file = "my_password.txt"
password_key = "ThisIsThePasswordKey"

def create_new_password(new_password):
    '''
    Description: Creates a new password

    Args:
      new_password (string): the new password to encrypt
    '''
    # Create Key File id it does not exist
    if not os.path.exists(password_file):
        f = open(password_file, 'w')    
        f.close()

    # Check Password Citeria
    message = {"message":""}
    if len(new_password) < 10: 
        message["message"] = "ERROR: The Password Must Be At Least 10 Characters Long"
        return message

    if " " in new_password:
        message["message"] = "ERROR: The Password Can Not Contain Spaces"
        return message
    
    num_count = 0
    for c in list(new_password):
        try: 
            num = int(c)
            if num in list(range(0,10)):
                num_count+=1
        except:
            pass

    if not num_count >= 4:
        message["message"] = "ERROR: The Password Must Contain At Least 4 Numbers"
        return message
    
    # Get key
    if not os.path.exists(key_file):
        with open(key_file, 'wb') as f:
            f.write(Fernet.generate_key())

    with open(key_file, 'rb') as f:
        key = f.read()

    fernet = Fernet(key)

    # Encode and store password
    encoded_password = fernet.encrypt(new_password.encode())
    with open(password_file, 'a') as f:
        f.write(f'{encoded_password.decode('utf-8')}\n')
        

    message["message"] = "Passoword Created"
    return message

def validate_password(password):
    '''
    Description: Validates a password

    Args:
      password (string): the password to validate
    '''
    with open(key_file, 'rb') as f:
        key = f.read()

    fernet = Fernet(key)
    
    with open(password_file, 'r') as f:
        encoded_passwords = f.readlines()

    message = {"message":""}
    for ep in encoded_passwords:
        ep.strip("\n")
        decoded_password = fernet.decrypt(ep).decode()
        if decoded_password == password:
            message["message"] = "The Password Is Valid"
            return message
    
    message["message"] = "The Password Is Invalid"
    return message


def create_key_pair(password, username):
    '''
    Description: Create a password and key pair
        
    Args:
      password (string): The password to be encrypted
      username (string): the key used to encrypt the password
    '''
    message = {"message":""}

    if len(password) < 10: 
        message["message"] = "ERROR: The Password Must Be At Least 10 Characters Long"
        return message
    if len(username) < 6: 
        message["message"] = "ERROR: The Username Must Be At Least 6 Characters Long"
        return message
    
    if " " in password:
        message["message"] = "ERROR: The Password Can Not Contain Spaces"
    if " " in username:
        message["message"] = "ERROR: The Username Can Not Contain Spaces"

    num_count = 0
    for c in list(password):
        try: 
            num = int(c)
            if num in list(range(0,10)):
                num_count+=1
        except:
            pass

    if not num_count >= 4:
        message["message"] = "ERROR: The Password Must Contain At Least 4 Numbers"
        return message


    hash_digest = hashlib.sha256(username.encode()).digest()
    key = base64.urlsafe_b64encode(hash_digest[:32])
    fernet = Fernet(key)
    encrypted_password = fernet.encrypt(password.encode())

    if not os.path.exists(key_pair_file):
        f = open(key_pair_file, 'w')    
        f.close()

    with open(key_pair_file, 'a') as f:
        f.write(f'{encrypted_password.decode('utf-8')}:{username}\n')

    message["message"] = "Key Pair Successfully Created"
    return message


def validate_key_pairs(password, username):
    '''
    Description: Validates a Key Pair

    Args:
      password (string): The password to validate
      username (string): The username to validate
    '''
    with open(key_pair_file, 'r') as f:
        key_pairs = f.readlines()

    message = {"message":""}
    for p in key_pairs:
        pair = p.split(":")
        this_password = pair[0]
        this_username = pair[1].strip("\n")
        if this_username == username:
            hash_digest = hashlib.sha256(username.encode()).digest()
            key = base64.urlsafe_b64encode(hash_digest[:32])
            fernet = Fernet(key)
            decrypted_password = fernet.decrypt(this_password).decode()
            if decrypted_password == password:
                message["message"] = "Username And Password Are Valid"
            else:
                message["message"] = "Username Was Found But The Password Is Invalid"
            return message
        
    message["message"] = "Username And Password Are Invalid"
    return message



#print(create_new_password("happydays4789"))

print(validate_password("happydays4789"))

#print(create_key_pair("JaneDoe09!2023", "JaneDoe09"))

#print(validate_key_pairs("JaneDoe09!2023","JaneDoe09"))