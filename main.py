# bruh
# TODO read in doge.png as raw bytes
import sys
from scapy.all import *
class Doge(Packet):
    name= "DogePacket"
    fields_desc = [
        ByteField("version",4),
        StrFixedLenField("toptext",50),
        StrFixedLenField("bottomtext",50),
        ByteEnumField("gotum", 2, {1:"uhh",2:"deez-nuts"}),
        LongField("doge_png",34332),
        XShortField("do_you_get_it",None)#aka checksum
    ]
