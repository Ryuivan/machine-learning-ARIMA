# Dictionary untuk menyimpan provinsi dan pulau
pulau_dict = {
    'Sumatera': [
        'ACEH',
        'SUMATERA UTARA',
        'SUMATERA BARAT',
        'RIAU',
        'JAMBI',
        'SUMATERA SELATAN',
        'BENGKULU',
        'LAMPUNG',
        'KEP. BANGKA BELITUNG',
        'KEP. RIAU'
    ],
    'Jawa': [
        'DKI JAKARTA',
        'JAWA BARAT',
        'JAWA TENGAH',
        'DI YOGYAKARTA',
        'JAWA TIMUR',
        'BANTEN'
    ],
    'Bali': [
        'BALI'
    ],
    'Nusa Tenggara': [
        'NUSA TENGGARA BARAT',
        'NUSA TENGGARA TIMUR'
    ],
    'Kalimantan': [
        'KALIMANTAN BARAT',
        'KALIMANTAN TENGAH',
        'KALIMANTAN SELATAN',
        'KALIMANTAN TIMUR',
        'KALIMANTAN UTARA'
    ],
    'Sulawesi': [
        'SULAWESI UTARA',
        'SULAWESI TENGAH',
        'SULAWESI SELATAN',
        'SULAWESI TENGGARA',
        'GORONTALO',
        'SULAWESI BARAT'
    ],
    'Maluku': [
        'MALUKU',
        'MALUKU UTARA'
    ],
    'Papua': [
        'PAPUA BARAT',
        'PAPUA BARAT DAYA',
        'PAPUA',
        'PAPUA SELATAN',
        'PAPUA TENGAH',
        'PAPUA PEGUNUNGAN'
    ]
}

# Kategorikan provinsi berdasarkan pulau
kategori_provinsi = {pulau: provinsi for pulau, provinsi in pulau_dict.items()}

# Tampilkan hasil
for pulau, provinsi in kategori_provinsi.items():
    print(f"Pulau: {pulau}")
    print("Provinsi:", ", ".join(provinsi))
    print()
