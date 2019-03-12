import difflib
import sys
my_str = sys.argv[1]
file= sys.argv[2]
with open(file, 'r') as f:    
  str_list = [line.strip() for line in f]
best_match = difflib.get_close_matches(my_str,str_list,1)[0]
score = difflib.SequenceMatcher(None, my_str, best_match).ratio()
