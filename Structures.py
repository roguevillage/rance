class Structures:

    def __init__(self):
        self.simple = [ "NVL", "NLV", "L,NV", "ANLV", "LANV", "ANVL", "ANV", "NV", "N&NV",
                      "UNV", "UQNV", "QNV", "VL", "VL&L"]

        self.complex = ["N,N&NV", "VLPtN", "A,ANV", "NVPtN", "L,N&NV", "N&NVL", "N&NLV", "A,ANVL", "A,ANLV", "ANVPtN", "NVLPtN", "NVCNV", "ANVL&L",
                      "AN&ANV", "N,N&NVLPtN", "L,N,N&NPtN", "L,A&ANV", "LNV", "NVL&L", "L&LNV", 
                     "AN&ANVL", "N,N&NVL", "ANVCNV", "NVLCNV", "L,N&NVPtN", "N,N&NVPtN", "N&NVPtN", "PtN,NV", "N,N&NVPtNL", "AN&ANLV", "PtN,NVL"]


        self.testE = ["N&NLV", "A,ANVL", "A,ANLV", "ANVPtN", "NVLPtN", "NVCNV", "ANVL&L", "AN&ANV", "N,N&NVLPtN", "L,N,N&NPtN", "L,A&ANV",
                     "AN&ANVL", "N,N&NVL", "ANVCNV", "NVLCNV", "L,N&NVPtN", "N,N&NVPtN", "N&NVPtN", "PtN,NV", "N,N&NVPtNL", "AN&ANLV",
                      "PtN,NVL", "NVL", "NLV", "LNV", "ANLV", "LANV", "ANVL", "ANV", "NV", "NVL&L", "L&LNV", "L,N&NV", "N&NVL", "N&NV",
                      "N,N&NV", "NVPtN", "UNV", "UQNV", "QNV", "VLPtN", "VL", "VL&L", "A,ANV"]

        self.test2E = ["NVL", "ANV", "NLV", "N&NV", "NV", "L,NV", "ANLV"]
