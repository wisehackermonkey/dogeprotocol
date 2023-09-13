# bruh
# TODO read in doge.png as raw bytes
import struct
import sys
from scapy.all import *
class Doge(Packet):
    name= "DogePacket"
    fields_desc = [
        #https://scapy.readthedocs.io/en/latest/build_dissect.html#simple-datatypes
        ByteField("version",1),
        FieldLenField("toptext_len", None, count_of="toptext"),
        StrField("toptext",None, fmt="H"),
        StrStopField("toptext_end",default="\x09",stop="\x09"),

        StrField("bottomtext",None, fmt="H"),
        StrStopField("bottomtext_end",default="\x09",stop="\x09"),

        ByteEnumField("gotum", 2, {1:"uhh",2:"deez-nuts"}),
        StrFixedLenField("doge_png",34332),
        XShortField("do_you_get_it",None)#aka checksum
    ]
