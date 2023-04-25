from googletrans import Translator

async def googler(word_or_str):
    trans = Translator()
    t = trans.translate(word_or_str, dest='uz')
    
    if t.src == 'uz':
        t = trans.translate(word_or_str)
    
    uzword = t.text
        
    # if ' ' not in word_or_str:           # User yuborgan string bitta so'zgan iborat bo'lsa:
    #     uzword = uzword.capitalize()
    
    return uzword.capitalize()
