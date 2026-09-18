def dem_ky_tu(Chuoi,ky_tu):
    tong=0
    for i in Chuoi:
        if i==ky_tu:
            tong += 1
    return tong;
print(dem_ky_tu("banana","a"))