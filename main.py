from lz77_compressor import read_text_file, compression, decompression, calc_compression_ratio

def main():
    file_name = "text.txt"  
    content = read_text_file(file_name)

    if "not found" in content:
        print(content)
        return

    search_buffer = 12
    look_ahead_window = 11

    print("Data:", content)

    compressed_data = compression(content, search_buffer, look_ahead_window)
    print("\nCompressed Data (Tags):", compressed_data)

    decompressed_data = decompression(compressed_data)
    print("\nDecompressed Data:", decompressed_data)

    if decompressed_data == content:
        print("\nDecompression successful! The original content was correctly restored.")
        compression_ratio = calc_compression_ratio(compressed_data, content)
        print(f"\nCompression Ratio: {compression_ratio:.2f}")

if __name__ == "__main__":
    main()
