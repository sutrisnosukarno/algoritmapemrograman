# ==============================
# PROGRAM PENGGAJIAN KARYAWAN
# ==============================

# Data karyawan
nama = input("Nama karyawan        : ")
jabatan = input("Jabatan              : ")

# Data gaji
gaji_pokok = float(input("Gaji pokok           : "))
tunjangan = float(input("Tunjangan             : "))
bonus = float(input("Bonus                 : "))

# Data potongan
potongan_bpjs = float(input("Potongan BPJS        : "))
potongan_pajak = float(input("Potongan pajak       : "))

# Perhitungan
total_pendapatan = gaji_pokok + tunjangan + bonus
total_potongan = potongan_bpjs + potongan_pajak
gaji_bersih = total_pendapatan - total_potongan

# Output
print("\n==============================")
print("       DATA PENGGAJIAN")
print("==============================")

print(f"Nama              : {nama}")
print(f"Jabatan           : {jabatan}")
print(f"Gaji Pokok        : Rp {gaji_pokok}")
print(f"Tunjangan         : Rp {tunjangan}")
print(f"Bonus             : Rp {bonus}")

print("------------------------------")

print(f"Total Pendapatan  : Rp {total_pendapatan:,.0f}")
print(f"Potongan BPJS     : Rp {potongan_bpjs:,.0f}")
print(f"Potongan Pajak    : Rp {potongan_pajak:,.0f}")
print(f"Total Potongan    : Rp {total_potongan:,.0f}")

print("------------------------------")

print(f"Gaji Bersih       : Rp {gaji_bersih:,.0f}")
print("==============================")