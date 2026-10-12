import glob,os
base='/Users/mac/Documents/GitHub/DCS-conllu/files'
N=25040
for name in ['Ṛgveda','Rāmāyaṇa','Mahābhārata','Hitopadeśa']:
    toks=0; forms=set()
    files=sorted(f for f in glob.glob(os.path.join(base,name,'*.conllu')) if not f.endswith('_parsed.conllu'))
    for f in files:
        if toks>=N: break
        for line in open(f,encoding='utf-8'):
            if line[0].isdigit():
                c=line.split('\t')
                if len(c)<10 or '-' in c[0]: continue
                toks+=1; forms.add(c[1])
                if toks>=N: break
    print(f'{name}: TTR@{N} = {len(forms)/N:.4f} ({len(forms)} forms)')
