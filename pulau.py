import pandas as pd

# Data provinsi
data_provinsi = {
    'Provinsi': [
        'ACEH', 'SUMATERA UTARA', 'SUMATERA BARAT', 'RIAU', 'JAMBI',
        'SUMATERA SELATAN', 'BENGKULU', 'LAMPUNG', 'KEP. BANGKA BELITUNG',
        'KEP. RIAU', 'DKI JAKARTA', 'JAWA BARAT', 'JAWA TENGAH',
        'DI YOGYAKARTA', 'JAWA TIMUR', 'BANTEN', 'BALI',
        'NUSA TENGGARA BARAT', 'NUSA TENGGARA TIMUR', 'KALIMANTAN BARAT',
        'KALIMANTAN TENGAH', 'KALIMANTAN SELATAN', 'KALIMANTAN TIMUR',
        'KALIMANTAN UTARA', 'SULAWESI UTARA', 'SULAWESI TENGAH',
        'SULAWESI SELATAN', 'SULAWESI TENGGARA', 'GORONTALO',
        'SULAWESI BARAT', 'MALUKU', 'MALUKU UTARA', 'PAPUA BARAT',
        'PAPUA BARAT DAYA', 'PAPUA', 'PAPUA SELATAN', 'PAPUA TENGAH',
        'PAPUA PEGUNUNGAN'
    ]
}

# Membuat DataFrame
df = pd.DataFrame(data_provinsi)

# Dictionary untuk kategori pulau
pulau_dict = {
    'Sumatera': [
        'ACEH', 'SUMATERA UTARA', 'SUMATERA BARAT', 'RIAU', 'JAMBI',
        'SUMATERA SELATAN', 'BENGKULU', 'LAMPUNG', 'KEP. BANGKA BELITUNG',
        'KEP. RIAU'
    ],
    'Jawa': [
        'DKI JAKARTA', 'JAWA BARAT', 'JAWA TENGAH', 'DI YOGYAKARTA',
        'JAWA TIMUR', 'BANTEN'
    ],
    'Bali': ['BALI'],
    'Nusa Tenggara': [
        'NUSA TENGGARA BARAT', 'NUSA TENGGARA TIMUR'
    ],
    'Kalimantan': [
        'KALIMANTAN BARAT', 'KALIMANTAN TENGAH', 'KALIMANTAN SELATAN',
        'KALIMANTAN TIMUR', 'KALIMANTAN UTARA'
    ],
    'Sulawesi': [
        'SULAWESI UTARA', 'SULAWESI TENGAH', 'SULAWESI SELATAN',
        'SULAWESI TENGGARA', 'GORONTALO', 'SULAWESI BARAT'
    ],
    'Maluku': ['MALUKU', 'MALUKU UTARA'],
    'Papua': [
        'PAPUA BARAT', 'PAPUA BARAT DAYA', 'PAPUA', 'PAPUA SELATAN',
        'PAPUA TENGAH', 'PAPUA PEGUNUNGAN'
    ]
}

# Fungsi untuk mendapatkan pulau berdasarkan provinsi
def get_pulau(provinsi):
    for pulau, provinsis in pulau_dict.items():
        if provinsi in provinsis:
            return pulau
    return None

# Menambahkan kolom 'Pulau' ke DataFrame
df['Pulau'] = df['Provinsi'].apply(get_pulau)

# Menampilkan DataFrame hasil
print(df)
