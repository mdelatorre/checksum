import checksum

header = {}

header[0] = 0x45
import checksum

header = {}

header[0] = 0x45
header[1] = 0x00
header[2] = 0x00
header[3] = 0xe8
header[4] = 0x00
header[5] = 0x00
header[6] = 0x40
header[7] = 0x00
header[8] = 0x40
header[9] = 0x11
header[10] = 0x0
header[11] = 0x0
header[12] = 0x0a
header[13] = 0x86
header[14] = 0x33
header[15] = 0xf1
header[16] = 0x0a
header[17] = 0x86
header[18] = 0x33
header[19] = 0x76

print("Checksum is: %x" % (checksum.ip_checksum(header, len(header)),))
print("Should be BD92")
