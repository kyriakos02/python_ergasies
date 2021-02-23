def reverse_mirror_ascii(ipasc: str):
    
    # get an ascii text
    ipasc = list(map(ord, list(ipasc) )) 
    
    # convert to ascii mirror character (sum 255)
    mirrors = [255-x for x in ipasc]
    
    # convert back to letters
    mirrors = list(map(chr, mirrors))
    
    # print mirror characters in reverse order
    reversed_mirrors = mirrors[::-1]
    mirrortext = ' '.join(reversed_mirrors)
    print(mirrortext)
    
reverse_mirror_ascii('what do you want?')    