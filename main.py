import ctypes
lib = ctypes.WinDLL( 'lcms2.dll' )
pfun = lib.cmsGetEncodedCMMversion
x = pfun()
print (x)