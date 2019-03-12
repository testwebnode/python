#curl -LJO https://raw.githubusercontent.com/testwebnode/python/testwebnode-patch-1/getmatch.py
import difflib
import sys
file1= sys.argv[1]
file2= sys.argv[2]

with open(file1, 'r') as f1:    
  str_list1 = [line.strip() for line in f1]

with open(file2, 'r') as f2:    
  str_list2 = [line.strip() for line in f2]

best_match=[]
#print str_list1
for i in range(len(str_list1)):
  #print i
  #print str_list1[i]
  bm=difflib.get_close_matches(str_list1[i],str_list2,1)
  if bm: 
    best_match.append(bm[0])
  else:
    best_match.append("")
  print best_match[i]
