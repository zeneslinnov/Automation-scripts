import subprocess
import sys

def run_command(command):
    """Fungsi untuk menjalankan perintah terminal dan menangkap error-nya"""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error: {result.stderr.strip()}")
        sys.exit(1)
    return result.stdout.strip()

def main():
    print("--- Git Auto-Commit & Push Automation ---")
    
    # 1. Cek status git apakah ada perubahan
    status = run_command("git status --porcelain")
    if not status:
        print("Tidak ada perubahan file yang perlu di-commit. Repo sudah bersih!")
        return
    
    print("\nFile yang berubah:")
    print(status)
    
    # 2. Minta input pesan commit dari user
    commit_message = input("\nMasukkan pesan commit (commit message): ").strip()
    if not commit_message:
        print("Pesan commit tidak boleh kosong. Dibatalkan.")
        return
    
    # 3. Jalankan perintah git add, commit, dan push secara berurutan
    print("\n[1/3] Menambahkan file ke staging area (git add)...")
    run_command("git add .")
    
    print(f"[2/3] Melakukan commit dengan pesan: '{commit_message}'...")
    run_command(f'git commit -m "{commit_message}"')
    
    print("[3/3] Mendorong perubahan ke GitHub (git push)...")
    push_output = run_command("git push")
    
    print("\nBerhasil! Semua perubahan sukses dikirim ke GitHub.")

if __name__ == "__main__":
    main()

