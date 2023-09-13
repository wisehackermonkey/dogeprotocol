# bruh
# TODO read in doge.png as raw bytes
import struct
import sys
from scapy.all import *
# f = open("./doge.png","rb").read()
class Doge(Packet):
    name= "DogePacket"
    
    fields_desc = [
        #https://scapy.readthedocs.io/en/latest/build_dissect.html#simple-datatypes
        ByteField("version",1),
        FieldLenField("toptext_len", None, count_of="toptext"),
        
        StrFixedLenField("toptext",None,length=25),
        StrFixedLenField("bottomtext",None,length=25),
        
        StrFixedLenField("doge_png",default=open("./doge.png","rb").read(),length=3107), 
        ByteEnumField("gotum", 0, {0: "idk", 1:"uhh",2:"deez_nuts"}),
        ShortField("do_you_get_it",None)#aka checksum
    ]
