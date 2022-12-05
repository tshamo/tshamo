# File objects

# USE THIS MODE - Copies test to test_copy
with open('daddy.jpg', 'rb') as rf:             # in binary b
    with open('daddy_copy.jpg', 'wb') as wf:    # in binary b
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)