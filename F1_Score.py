tp = int(input('Nhập tp là số nguyên: '))
while tp <=0:
    tp = int(input('Nhập lại tp: '))

fp = int(input('Nhập fp là số nguyên: '))
while fp <=0: 
    fp = int(input('Nhập lại fp: '))

fn = int(input('Nhập fn là số nguyên: '))
while fn <= 0:
    fn = int(input('Nhập lại fn: '))


precision = tp/(tp + fp)

recall = tp/(tp + fn)

f1_score = 2*((precision*recall)/(precision+recall))

print(f'Precision is: {precision}\nRecall is: {recall}\nf1_score is: {f1_score}')



    
        

