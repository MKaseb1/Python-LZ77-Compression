def read_text_file(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        return f"The file '{file_name}' was not found."

def compression(data , search_buffer , look_ahead_window):
    tags = []
    n = len(data)
    i = 0

    while i < n:
        search_start = max(0, i - search_buffer)
        search_string = data[search_start : i]

        index = 0
        match_length = 0
        k = i

        while k < i + look_ahead_window and k < n:
            match = data[i:k + 1]
            match_pos = search_string.rfind(match)
            
            if match_pos != -1:
                match_length = len(match)
                index = i - (search_start + match_pos)
                k += 1
            else:
                break

        next_char = data[k] if k < n else ''
        tags.append((index, match_length, next_char))

        i += k - i + 1

    return tags
            
def decompression(tags):
    final = ""

    for tag in tags:
        offset, length, next_char = tag

        if offset == 0:
            final += next_char
        else:
            start = len(final) - offset
            match_string = final[start : start + length]
            final += match_string + next_char

    return final

def calc_compression_ratio(tags , content):
    content_len = len(content) 

    if not tags:
        return float('inf')  
    
    total_tag_bits = 0
    ascii_char_bits = 8
    
    for tag in tags:
        offset = tag[0]
        length = tag[1]
        total_tag_bits += offset.bit_length() + length.bit_length() + ascii_char_bits

    compression_ratio = content_len / total_tag_bits if total_tag_bits > 0 else float('inf')

    return compression_ratio