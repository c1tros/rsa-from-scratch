def is_ascii_and_nonempty(s):
    return all(ord(char) < 128 for char in s) and len(s) != 0

def encode_string_to_chunks(s):
    #Check to ensure the string is valid
    if not is_ascii_and_nonempty(s):
        raise ValueError("Input contains non ASCII characters or is empty")
    #Pad the string so it can be split into 3 didgit chunks
    required_padding = (3-len(s)%3)%3
    s+=" "*required_padding
    #Split the string into three character chunks and append them to a result list
    #Each chunk: 3 characters → 9-digit numeric string (3 digits per char)
    result=[]
    #Itterate through each chunk
    for i in range(0,len(s),3):
        to_append = ""
        #Itterate through each character in the chunk
        for j in range(i,i+3):
            unpadded_string = str(ord(s[j]))
            padded_string = unpadded_string.zfill(3)
            to_append += padded_string
        result.append(int(to_append))
    return result

def decode_chunks_to_string(lst):
    result=""
    #Iterate through each chunk
    for chunk in lst:
        #Convert to string, and pad with leading zeros
        unpadded_chunk = str(chunk)
        full_string = unpadded_chunk.zfill(9)
        chunk_string = ""
        #Iterate through each 3 didgits (one character) in the chunk
        for i in range (0,9,3):
            string_character_code = full_string[i:i+3]
            character_code = int(string_character_code)
            chunk_string += chr(character_code)
        result+=chunk_string
    #Return the result with trailing spaces removed
    return result.strip()

def encrypt_list_of_chunks(lst,public_key):
    e,n = public_key
    result = []
    for chunk in lst:
        result.append(pow(chunk,e,n))
    return result

def decrypt_list_of_chunks(lst,private_key):
    d,n = private_key
    result = []
    for chunk in lst:
        result.append(pow(chunk,d,n))
    return result

if __name__ == "__main__":
    test_string = "This is a test string!"
    print(f"Starting string is: {test_string}")
    test_string_converted=encode_string_to_chunks(test_string)
    print(f"String converted to list of chunks: {test_string_converted}")
    encrypted=encrypt_list_of_chunks(test_string_converted,(65537,9516311845790656153499716760847001433441357))
    print(f"Encrypted list of chunks: {encrypted}")
    decrypted=decrypt_list_of_chunks(encrypted,(5617843187844953170308463622230283376298685,9516311845790656153499716760847001433441357))
    print(f"Decrypted list of chunks: {test_string_converted}")
    print(f"Decoded list of chunks back to string: {decode_chunks_to_string(decrypted)}")