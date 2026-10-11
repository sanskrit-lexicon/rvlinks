# coding=utf-8
# Py3 port of the rvtest.py temp5/temp6/temp7 chain (H6477, avlinks treatment):
#   temp5: private-use char U+F003 (57347) after an accent mark ->
#          visarga U+0903 reordered after the accent
#   temp6: '1'/'3' + U+F009 (57353) + U+F007 (57351) ->
#          Devanagari digit one/three + anudatta + udatta
#   temp7: normalize to unix line endings (strip \r\n, drop mid-line \r)
# Usage: python3 prep_source.py RV_sa-hn-ru-de-en_1.html temp_RV_sa-hn-ru-de-en_5.html
import sys,codecs
if hasattr(sys.stdout,'reconfigure'):
 sys.stdout.reconfigure(encoding='utf-8')

def pass5(lines):
 visarga = u"\u0903"
 ordudatta = 2385   # U+0951
 ordanudatta = 2386 # U+0952
 nfound = 0
 out_lines = []
 for lnum,line in enumerate(lines,1):
  out = []
  found = False
  for ix,x in enumerate(line):
   if ord(x) == 57347:
    xprev = line[ix-1]
    if ord(xprev) in [ordudatta,ordanudatta]:
     prev = out.pop()  # udatta or anudatta
     out.append(visarga)
     out.append(prev)
    else:
     print("Unexpected char before bad visarga %s" %(ord(xprev)))
     print("@ line",lnum)
     exit(1)
    found = True
   else:
    out.append(x)
  if found:
   nfound = nfound + 1
  out_lines.append(''.join(out))
 print(nfound,"bad visargas changed")
 return out_lines

def pass6(lines):
 visarga = u"\u0903"
 udatta = u"\u0951"
 anudatta = u"\u0952"
 devaOne = u"\u0967"
 devaThree = u"\u0969"
 nfound = 0
 out_lines = []
 for line in lines:
  out = []
  found = False
  n = len(line)
  for ix,x in enumerate(line):
   if x in ['1','3'] and (ix+2<n) and (ord(line[ix+1])==57353) and (ord(line[ix+2])==57351):
    found = True
    if x == '1':
     out.append(devaOne)
    else:
     out.append(devaThree)
    out.append(anudatta)
    out.append(udatta)
   elif ord(x) in [57353,57351]:
    pass # skip these
   else:
    out.append(x)
  if found:
   nfound = nfound + 1
  out_lines.append(''.join(out))
 print(nfound,"digit+PUA lines changed")
 return out_lines

def pass7(lines):
 nfound = 0
 out_lines = []
 for line in lines:
  line = line.rstrip('\r\n')
  if '\r' in line:
   line = line.replace('\r','')
   nfound = nfound + 1
  out_lines.append(line + '\n')
 print(nfound,"lines changed with intermediate carriage returns")
 return out_lines

if __name__ == "__main__":
 filein = sys.argv[1]
 fileout = sys.argv[2]
 # text-mode read keeps universal-newline behavior of the original py2
 # codecs.open(...) chain (\r\n and lone \r arrive as \n; pass7 is then a no-op)
 with codecs.open(filein,"r","utf-8",errors='strict') as f:
  lines = f.readlines()
 print(len(lines),"lines read from",filein)
 lines = pass5(lines)
 lines = pass6(lines)
 lines = pass7(lines)
 with codecs.open(fileout,"w","utf-8") as f:
  for line in lines:
   f.write(line)
 print(len(lines),"lines written to",fileout)
