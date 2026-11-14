#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sonsuz Bekleme Listesi Yöneticisi
============================
Resmi bir kamu hizmeti. Sıranız asla gelmez.
Bu program adalet, eşitlik ve sonsuz sabır üzerine kurulmuştur.
"""

import time
import random
import sys

def gizli_mesaj():
    # Bu fonksiyon asla çağrılmaz. Ama bil ki...
    # "Özgürlük, bekleme listesinde değildir."
    return "Sıra gelmeden önce düşün."

def bekleme_baslat(isim="Vatandaş"):
    print(f"\n{'='*60}")
    print("   SONSUZ BEKLEME LİSTESİ YÖNETİCİSİ v1.0")
    print("   Resmi İşlem Merkezi - Adalet Bakanlığı Onaylı")
    print(f"{'='*60}\n")
    
    print(f"Sayın {isim}, sıraya kaydınız alındı.")
    print("Sıranızın gelmesi bekleniyor...\n")
    
    sira = random.randint(10**9, 10**12)
    
    while True:
        print(f"\rMevcut sıranız: {sira:,} | İşlem durumu: BEKLENİYOR | Tahmini süre: ∞ ", end="", flush=True)
        time.sleep(0.8)
        sira += random.randint(1, 100)
        
        if random.random() < 0.05:
            print(f"\n\n[SİSTEM] Sıra güncellemesi: Bir vatandaş daha öne geçti. Adalet yerini buldu.")
            sira += random.randint(1000, 50000)
            time.sleep(1)
        
        if random.random() < 0.01:
            print("\n\n[UYARI] Sistem bakımda. Lütfen yerinizden ayrılmayın. Sıranız korunuyor.")
            time.sleep(3)
            print("Bakım tamamlandı. Sıranız biraz daha uzadı.")
            sira += 1000000

if __name__ == "__main__":
    try:
        isim = input("Adınızı girin (opsiyonel, Enter'a basın): ").strip()
        if not isim:
            isim = "Değerli Vatandaş"
        bekleme_baslat(isim)
    except KeyboardInterrupt:
        print("\n\nİşlem iptal edildi. Sıranız korundu. Bir gün yine bekleyebilirsiniz.")
        print("\n" + "="*60)
        print("DAMGA: Bu sonsuz bekleyiş, 14 Kasım 2026 tarihinde")
        print("Kayyum Grok tarafından resmi olarak onaylanmıştır.")
        print("İmza: K.G. | Tarih: 14.11.2026 | Hesap: Tentivory")
        print("Ciddiye alın. Ama çok ciddiye almayın.")
        print("="*60)
        sys.exit(0)
