import json, sys

if len(sys.argv) > 2:
    
    import csv
    
    with open(sys.argv[2], mode='r', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        with open('coors_new.csv', mode='w') as outfile:
            writer = csv.writer(outfile)
            mydict = {rows[0]:rows[3] for rows in reader}


text = ''

with open(sys.argv[1], encoding='utf-8') as f:
    
    data = json.load(f)
    
    for pages in data['CreditsPages']:
        
        for credit in pages['Credits']:
        
            job = credit['JobTitle']
        
            if not job.strip() == '':
        
                if len(sys.argv) > 2 and job in mydict:
                
                    job = mydict[job]
                    
                #print(job)
        
                text += '\n' + job + '\n'
            
            for name in credit['Names']:
                
                if not name.strip() == '':
                
                    text += name + '\n'
    
text = text.strip()

with open(sys.argv[1] + '_moby.txt', 'w', newline='', encoding='utf-8') as f:
    f.write(text)
