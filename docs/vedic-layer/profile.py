import glob, os, json, sys
base='/Users/mac/Documents/GitHub/DCS-conllu/files'
def stats(folder):
    toks=0; forms=set(); lemmas=set(); freq={}; mantra=0; treebank_lines=0
    files=[f for f in glob.glob(os.path.join(base,folder,'*.conllu')) if not f.endswith('_parsed.conllu')]
    for f in files:
        for line in open(f, encoding='utf-8'):
            if line[0].isdigit():
                c=line.rstrip('\n').split('\t')
                if len(c)<10 or '-' in c[0]: continue
                toks+=1; forms.add(c[1]); lemmas.add(c[2])
                freq[c[2]]=freq.get(c[2],0)+1
                if 'IsMantra=True' in c[9]: mantra+=1
                if c[6].isdigit(): treebank_lines+=1
    return dict(files=len(files),tokens=toks,forms=len(forms),lemmas=len(lemmas),mantra=mantra,treebank=treebank_lines),freq
out={}
freqs={}
for name in ['Ṛgveda','Rāmāyaṇa','Mahābhārata','Hitopadeśa']:
    s,freqs[name]=stats(name); out[name]=s
    print(name,s,file=sys.stderr)
rv=set(freqs['Ṛgveda']); epic=set(freqs['Rāmāyaṇa'])|set(freqs['Mahābhārata'])
out['overlap']={'rv_lemmas':len(rv),'epic_lemmas':len(epic),'shared':len(rv&epic),
 'rv_only':len(rv-epic),'epic_only':len(epic-rv)}
top=lambda d,n: sorted(d.items(),key=lambda x:-x[1])[:n]
out['top_rv']=top(freqs['Ṛgveda'],25); out['top_epic']=top(freqs['Rāmāyaṇa'],10)
json.dump(out,open('/var/folders/17/xycv_hps0w5_b67s84q43vr40000gp/T/opencode/h6062/profile.json','w'),ensure_ascii=False,indent=1)
