from hashlib import sha256
MAX_NONCE = 100000000000

def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()

def mine(block_number, transactions, previous_hash, prefix_zeros):
    prefix_str = '0'*prefix_zeros
    for nonce in range(MAX_NONCE):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):
            print(f"Yay! Minerou um total de nonce:{nonce}")
            return new_hash

    raise BaseException(f"Não achei nada depois de  {MAX_NONCE} vezes")

if __name__=='__main__':
    transactions='''
    Bruno->Marcelo->20,
    Fernanda->Iroh->45
    '''
    difficulty=4 
    import time
    start = time.time()
    print("start mining")
    new_hash = mine(5,transactions,'0000000xa036944e29568d0cff17edbe038f81208fecf9a66be9a2b8321c6ec7', difficulty)
    total_time = str((time.time() - start))
    print(f"Terminou. A minereção levou: {total_time} segundos")
    print(new_hash)