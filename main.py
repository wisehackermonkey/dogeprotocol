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
        
        FieldLenField("bottomtext_len", None, count_of="bottomtext"),

        StrField("bottomtext",None, fmt="H"),
        ByteEnumField("gotum", 2, {1:"uhh",2:"deez-nuts"}),
        StrFixedLenField("doge_png",34332),
        XShortField("do_you_get_it",None)#aka checksum
    ]
    def addfield(self, pkt, s, val):
        return s+self.i2m(pkt, val)
    def do_dissect(self, s):
        flist = self.fields_desc[:]
        flist.reverse()
        while s and flist:
            f = flist.pop()
            s,fval = f.getfield(self, s)
            self.fields[f] = fval
        return s
class StrFixedLenField(StrField):
    def addfield(self, pkt, s, val):
        return s+struct.pack("%is"%self.length,self.i2m(pkt, val))
class StrFixedLenField(StrField):
    def getfield(self, pkt, s):
        return s[self.length:], self.m2i(pkt,s[:self.length])