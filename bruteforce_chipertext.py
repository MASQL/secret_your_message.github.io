def caesar_decrypt(ciphertext: str, shift: int) -> str:
    """Mendekripsi ciphertext dengan pergeseran tertentu (K)."""
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr((ord(char) - start - shift) % 26 + start)
            plaintext += decrypted_char
        else:
            plaintext += char
    return plaintext


def brute_force_caesar(ciphertext: str):
    """Melakukan brute force perulangan C - k dari k=1 hingga 25."""
    print(f"=== MENDEKRIPSI CIPHERTEXT: '{ciphertext}' ===")
    print(f"{'Shift (k)':<10} | {'Hasil Teks (Plaintext)':<30}")
    print("-" * 45)

    for k in range(1, 26):
        hasil = caesar_decrypt(ciphertext, k)
        print(f"k = {k:<7} | {hasil}")


def main():
    print("=== PROGRAM PEMECAH CIPHERTEXT (CAESAR CIPHER) ===")
    teks = input("Masukkan Ciphertext: ").strip()

    if not teks:
        print("Teks tidak boleh kosong.")
        return

    print("\nPilih Mode Dekripsi:")
    print("1. Brute Force (Tampilkan semua 25 kemungkinan)")
    print("2. Dekripsi Langsung dengan Kunci (K) Tertentu")

    pilihan = input("Masukkan pilihan (1/2): ").strip()

    if pilihan == "1":
        print()
        brute_force_caesar(teks)
    elif pilihan == "2":
        try:
            kunci = int(input("Masukkan nilai kunci K (1-25): "))
            if 1 <= kunci <= 25:
                hasil = caesar_decrypt(teks, kunci)
                print(f"\n[+] Teks Asli (K={kunci}): {hasil}")
            else:
                print("Kunci harus di antara 1 dan 25.")
        except ValueError:
            print("Kunci harus berupa angka integer.")
    else:
        print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()