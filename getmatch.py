import difflib
import sys
file1= sys.argv[1]
file2= sys.argv[2]

with open(file1, 'r') as f1:    
  str_list1 = [line.strip() for line in f1]

with open(file2, 'r') as f2:    
  str_list2 = [line.strip() for line in f2]

best_match = difflib.get_close_matches(str_list1[0],str_list2,1)[0]
#score = difflib.SequenceMatcher(None, my_str, best_match).ratio()
print best_match
