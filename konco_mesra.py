import sys
import time

def jalanin_lirik () :
    lirik = [
        ("Yen tak sawang sorote...", 0.065),
        ("Mripatmu", 0.09),
        ("Jane ku ngerti ono ati sliramu ", 0.09),
        ("Nanging onone mung se", 0.09),
        ("wates konco", 0.1),
        ("Podo ra wanine ngungkapke tresno", 0.08),
        ("Yen ku pandang gemerlap nyang mripatmu", 0.085),
        ("Terpampar gambar waru ", 0.09),
        ("Ning atimu ", 0.09), 
        ("Nganti kapan abot iku ora mok dukung", 0.08),
        ("Mung dadi konco mesra mergo kependem cinta ", 0.095),  
        ("Sungguh sayang aku tak bisa langsung mengungkapkan ", 0.06), 
        ("Perasaan yang ku simpan buat ku tak tenang ", 0.06), 
        ("Ini semua karena hubungan pertemanan ", 0.085), 
        ("Kau sudah biasa anggap ku sebagai kawan", 0.08), 


    ]

    delay = [0.5, 0.51, 0.36, 0.79, 0.31, 0.61, 0.46, 0.56, 0.41, 0.4, 0.2, 0.45, 0.45, 0.45, 0.45, 0.5, ]
    print("\n==Konco Mesra - Nella Kharisma ==")
    time.sleep(0.1)
    for i, (baris_lagu, delay_karakter) in enumerate(lirik):
        for karakter in baris_lagu :
            print(karakter, end='')
            sys.stdout.flush()
            time.sleep(delay_karakter)
        time.sleep(delay[i])    
        print('')
    print("// Asekk")


jalanin_lirik()
