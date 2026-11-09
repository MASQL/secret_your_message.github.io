def caesar_encrypt(plaintext: str, shift: int) -> str:
    """Mengenkripsi plaintext menjadi ciphertext menggunakan rumus C = (P + K) mod 26."""
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr((ord(char) - start + shift) % 26 + start)
            ciphertext += encrypted_char
        else:
            ciphertext += char
    return ciphertext


def main():
    print("=== PROGRAM ENKRIPSI CAESAR CIPHER (PEMBUAT CIPHERTEXT) ===")
    plaintext = input("Masukkan Teks Asli (Plaintext): ").strip()

    if not plaintext:
        print("Teks tidak boleh kosong.")
        return

    try:
        kunci = int(input("Masukkan Nilai Kunci Pergeseran (K), misal 3: "))

        # Proses enkripsi
        ciphertext = caesar_encrypt(plaintext, kunci)

        print("\n" + "=" * 55)
        print(f"[+] Plaintext  : {plaintext}")
        print(f"[+] Kunci (K)  : +{kunci}")
        print(f"[+] Ciphertext : {ciphertext}")
        print("=" * 55)

    except ValueError:
        print("Error: Kunci harus berupa angka bulat (integer).")


if __name__ == "__main__":
    main()