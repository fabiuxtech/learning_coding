#!/usr/bin/python3

#/start testing

#/end testing

def encodeString(stringVal):
    prevChar = None
    count_char = 0
    encoding = []
    for char in stringVal:
        if char != prevChar:
            count_char = 1
            newChar = (char, count_char)
            encoding.append(newChar)
        else:
            count_char += 1
            encoding.pop()
            sameChar = (char, count_char)
            encoding.append(sameChar)
        prevChar = char
    return encoding

def decodeString(encodeList):
    decodeStr = ''
    for char, numbers in encodeList:
        decodeStr += char * numbers
    return decodeStr

# def ryanEncodeString(stringVal):
#     encodedList = []
#     prevChar = stringVal[0]
#     count = 0
#     for char in stringVal:
#         if prevChar != char:
#             encodedList.append((prevChar, count))
#             count = 0
#         prevChar = char
#         count = count + 1
#     encodedList.append((prevChar, count))
#     return encodedList

art = '''

                                                                                
                                                                                
                               %%%%%%%%%%%%%%%%%%%                              
                        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%                       
                    %%%%%%%%                         %%%%%%%%                   
                %%%%%%%                                   %%%%%%                
              %%%%%%                                         %%%%%%             
           %%%%%%                                               %%%%%           
          %%%%%                                                   %%%%%         
        %%%%%                                                       %%%%%       
       %%%%                 %%%%%              %%%%%                  %%%%      
      %%%%                 %%%%%%%            %%%%%%%                  %%%%     
     %%%%                  %%%%%%%            %%%%%%%                   %%%%    
    %%%%                   %%%%%%%            %%%%%%%                    %%%%   
    %%%%                    %%%%%              %%%%%                     %%%%   
   %%%%                                                                   %%%%  
   %%%%                                                                   %%%%  
   %%%%                                                                   %%%%  
   %%%%                                                      %%%%        %%%%   
    %%%%       %%%%%%                                        %%%%%       %%%%   
    %%%%         %%%%                                       %%%%        %%%%    
     %%%%         %%%%                                     %%%%         %%%%    
      %%%%         %%%%%                                  %%%%         %%%%     
       %%%%%         %%%%%                             %%%%%         %%%%%      
        %%%%%          %%%%%%                        %%%%%          %%%%        
          %%%%%           %%%%%%%               %%%%%%%           %%%%%         
            %%%%%             %%%%%%%%%%%%%%%%%%%%%             %%%%%           
              %%%%%%%                                        %%%%%              
                 %%%%%%%                                 %%%%%%%                
                     %%%%%%%%%                     %%%%%%%%%                    
                          %%%%%%%%%%%%%%%%%%%%%%%%%%%%%                         
                                   %%%%%%%%%%%%                                 
                                                                                
                                                                                 

'''
stringVal = 'AAAAABBBBAAA'
encodeString = encodeString(art)
# encodeString = ryanEncodeString(art)
print(encodeString)
# listVal = [('A',5), ('B',4), ('A',3)]
decodeString = decodeString(encodeString)
print(decodeString)