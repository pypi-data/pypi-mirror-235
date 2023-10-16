import random
import time

__MAX_CODE_LENGTH = 12

# this __ID_SPACE should NOT be changed in any way as. 
# in total, it has 32 numbers which means we need only 6 bits to encode each 
# character in the space
__ID_SPACE = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789'
__ID_SPACE_MAP = {xter:index for index,xter in enumerate(__ID_SPACE)}

def new(length:int=10, useSeparator:bool=False, xterSet:str=__ID_SPACE) -> str:
    'compexity of the code will be len(__ID_SPACE)^length'
    
    assert(length>0 and length<=__MAX_CODE_LENGTH)
    code = ''
    __ID_SPACE_length = len(xterSet)
    while length:
        code += xterSet[random.randrange(0,__ID_SPACE_length)]
        length -= 1
        
        if useSeparator and length and not(length%4):
            code += '-'
    return code

if __name__=='__mani__':
    pass