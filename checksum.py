#!/usr/bin/python2.7
import struct

data = "45 00 00 47 73 88 40 00 40 06 a2 c4 83 9f 0e 85 83 9f 0e a1"

# a test for the checksum calculation

def _checksum(data):
    #calculate the header sum
    ip_header_sum = sum(struct.unpack_from("6H", data))
    #add the carry
    ip_header_sum = (ip_header_sum & 0xFFFF) + (ip_header_sum >> 16 & 0xFFFF)
    #invert the sum, python does not support inversion (~a is -a + 1) so we have to do
    #little trick: ~a is the same as 0xFFFF & ~a
    ip_header_sum = ~ip_header_sum & 0xFFFF

    return ip_header_sum #should return 0 if correct

data = data.split()
data = map(lambda x: int(x,16), data)
data = struct.pack("%dB" % len(data), *data)

print " ".join(map(lambda x: "0x%02x" % ord(x), data))
print "Checksum: 0x%04x" % _checksum(data)
