def get_soundex(token):
    """Get the soundex code for the string"""
    token = token.upper()

    soundex = ""
    
    # first letter of input is always the first letter of soundex
    soundex += token[0]
    
    # create a dictionary which maps letters to respective soundex codes. Vowels and 'H', 'W' and 'Y' will be represented by '.'
    dictionary = {"BFPV": "1", "CGJKQSXZ":"2", "DT":"3", "L":"4", "MN":"5", "R":"6", "AEIOUHWY":"."}
    
    for char in token[1:]:
        for key in dictionary.keys():
            if char in key:
                code = dictionary[key] 
                if code != '.': 
                    if code != soundex[-1]: 
                        soundex += code 
                    
    
    # trim or pad to make soundex a 4-character code
    soundex = soundex[:4].ljust(4, "0")
        
    return soundex

# get dict of location with their Soundex code
def get_soundex_location(locationlist):
    loc_soundex = []
    for loc in locationlist:
        loc_soundex.append(get_soundex(loc))
    res = dict(zip(locationlist, loc_soundex))
    return res

def spellcheck(locip,loc_codes):
    loc_code = get_soundex(locip)
    location = [k for k, v in loc_codes.items() if v == loc_code]
    if(len(location)>0):
        loc = location[0]
    else:
        loc = locip
    return loc