class Solution:
    def addBinary(self, a: str, b: str) -> str:
        decimala = 0
        lista = list(a)
        position = 1
        for i in range(len(a)):
            decimala += position* int(lista[-1])
            lista.pop()
            position *=2
        decimalb = 0
        listb = list(b)
        position = 1
        for i in range(len(b)):
            decimalb += position* int(listb[-1])
            listb.pop()
            position *=2
        return bin(decimala+decimalb)[2:]
        
        
#         mysum = []
#         if len(a) != len(b):
#             while len(a) > len(b):
#                 b = "0" + b
#             while len(b) > len(a):
#                 a = "0" + a
#         lista = list(a)
#         lista.reverse()
#         listb = list(b)
#         listb.reverse()
#         remain = 0
#         print(lista,listb)
        
#         for i in range(len(a)):
#             total = int(lista[0])+int(listb[0])+remain
#             toadd = total%2
#             print(total)
#             lista.pop(0)
#             listb.pop(0)
#             mysum.append(str(toadd))
            
#             if total>1:
#                 remain = 1
#             else:
#                 remain = 0
#         if remain ==1:
#             mysum.append(str(remain))
#         mysum.reverse()
#         toreturn = "".join(mysum)
#         return toreturn
        
        
        