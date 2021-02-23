text = 'python is a programming language'

def get_odd_ascii_asterisc(inptext: str):
    inptext = list(inptext) 
    number = list(map(ord, inptext))  # convert to ASCII
    number = [i for i in number if i % 2 != 0]  # keep only odds

    # for each letter print as many * as the percent of occurences
    # first compute occurence percent and add in a dictionary
    
    letters = list(map(chr, number))
    from collections import Counter
    counts = dict(Counter(letters))
    perc = {k: v*100/len(letters) for k, v in counts.items()}
    
    # percent of occurence of odd letters, within all odd letters of a sentence
    # an asteristic corresponds to 1%
    for key, value in perc.items():
        print(key, ': ', int(round(value)) * '*')
   
get_odd_ascii_asterisc(text)  
