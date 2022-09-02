#Misalkan prosedur lelaran : xr+1 = (-x^3 +3 )/ 6  dan r = 0,1,2,3,...
#tingkat toleransi galat 0.00001

xawal = 0.5
xketiga = 0.5 #samakan dengan xawal
iterasi = 0
#prosesnya    
def proses(x):
    xhitung = ((-x)**3 +3)/6
    return xhitung
def selisih(x1,x2):
    return abs(x2-x1)/x2
    
while xketiga > 0.00001 :
    iterasi = iterasi+1
    xkedua = proses(xawal)
    xketiga = selisih(xawal,xkedua)
    xawal = xkedua


print('Ketemu sekian: ',xketiga)
print('Iterasi ke-',iterasi)
    





