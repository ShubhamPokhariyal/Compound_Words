import time

def is_compound(word:str, wordSet:set):
    if(len(word)==0): return True
    for i in range(0,len(word)):
        currentword = word[0:i+1]
        if((currentword in wordSet) and is_compound(word[i+1:],wordSet)):
            return True
    return False


start_time = time.time()
with open("input_02.txt", "r") as file:
    words = [line.strip() for line in file]

words.sort(key=len)

wordSet = set()
l,sl = "",""
for word in words:
    if(is_compound(word,wordSet)):
        if len(word)>len(l):
            sl = l
            l = word
        elif(len(word)>len(sl)):            
            sl = word
    wordSet.add(word)

end_time = time.time()
time_taken = end_time - start_time
print(f"Time taken to process the input file: {time_taken:.4f} seconds")
print(f"largest = {l}\nSecond largest= {sl}")    
