import requests
import re

def find_new_version(url, base_url, name_pattern):
    """
    Cari versi terbaru dari link berdasarkan pola tertentu.
    """
    try:
        response = requests.get(base_url, timeout=10)
        if response.status_code == 200:
            # Cari semua link dalam HTML
            links = re.findall(r'href=[\'"]?([^\'" >]+)', response.text)
            for link in links:
                if re.search(name_pattern, link):
                    return f"{base_url.rstrip('/')}/{link}"
        return None
    except requests.RequestException:
        return None

def process_links_with_updates(conf_file, active_file, dead_file):
    # Membuka file konfigurasi dan membaca barisnya
    with open(conf_file, 'r') as file:
        lines = file.readlines()

    # Membuka file untuk menulis link aktif dan laporan link mati
    with open(active_file, 'w') as active_links, open(dead_file, 'w') as dead_links:
        for line in lines:
            # Abaikan baris kosong, komentar, atau pemisah
            if line.strip() == "" or line.strip().startswith("#") or line.strip().startswith("-"):
                active_links.write(line)  # Tetap tuliskan komentar atau baris kosong
                continue

            # Pisahkan nama dan URL
            try:
                name, url = line.split('=')
                name = name.strip()
                url = url.strip()

                # Cek status URL dengan mengikuti redirect
                try:
                    response = requests.head(url, allow_redirects=True, timeout=10)
                    if response.status_code == 200:
                        # Jika aktif, tulis ke file active_links
                        active_links.write(line)
                        print(f"Active: {name}")
                    else:
                        # Jika tidak aktif, cari pengganti
                        print(f"Dead: {name}, mencari link baru...")
                        # Contoh base_url dan pola pencarian
                        base_url = "/".join(url.split("/")[:-1])  # Ambil URL direktori
                        name_pattern = re.escape(name.split('-')[0]) + r".*"
                        new_url = find_new_version(url, base_url, name_pattern)
                        if new_url:
                            # Tulis ke file active_links jika pengganti ditemukan
                            active_links.write(f"{name}={new_url}\n")
                            print(f"Found replacement for {name}: {new_url}")
                        else:
                            # Tulis ke file dead_links jika tidak ada pengganti
                            dead_links.write(f"{name}: {url} (Status: {response.status_code})\n")
                            print(f"No replacement found for {name}")
                except requests.RequestException as e:
                    # Jika ada error koneksi, tulis ke file dead_links
                    dead_links.write(f"{name}: {url} (Error: {str(e)})\n")
                    print(f"Dead: {name} (Error)")
            except ValueError:
                # Jika format line tidak sesuai
                dead_links.write(f"Invalid line format: {line}\n")
                print(f"Invalid line format: {line}")

# Jalankan fungsi
conf_file = "package.conf"  # Nama file konfigurasi asli
active_file = "active_links_with_updates.conf"  # Nama file untuk link aktif (termasuk pengganti)
dead_file = "dead_links_report_with_updates.txt"  # Nama file untuk laporan link mati

process_links_with_updates(conf_file, active_file, dead_file)
