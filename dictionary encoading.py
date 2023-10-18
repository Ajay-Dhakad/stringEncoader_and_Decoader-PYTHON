ch=input("\nEncode manual text(1),\nEncode txt file(2) : ")
if ch=="1":
    str=input("\nEnter Text To Encode : ").lower()
elif ch=="2":
    st=input("Enter Filename To Encode : ")  
    st1=f"{st}.txt"
    with open(st1,"r") as f:
        rd=f.read()
        str=str(rd) 
          

enp=""
cnvf=""

#created a conversion dict.....

dc={"a":"/","b":"e","c":"f","d":"g","e":"c","f":"b","g":"a","h":"(","i":"*","j":"&",
    "k":"^","l":"9","m":"8","n":"7","o":"6","q":"%","r":"$","s":"#","t":"@","u":"!",
    "v":"1","w":"2","x":"3","y":"4","z":"5"," ":"-","p":"n"}

#taking every str character one by one and and converting it thru dict and 

for i in str:
    
    # print(dc[i])
    cnvf=(dc[i])
    enp=(enp+cnvf)  #assembling encoaded value
print(f"\nFile value : {str}") 
print(f"\nEncoded Value : {enp}")

save=input("\nEnter Filename To Save Encoaded data : ").lower()
sv=f"{save}.txt"

#writing in file

with open(sv,"w") as f:
    f.write(enp)
print(f"\nFile Is Successfully Saved In {sv}")    


# inpdc=input(f"WANT TO DECODE YES(Y) NO(N)").lower() #input decoding 2

#         for j in enp:
#             # print(cd[j])
#             cnvf2=(cd[j]) #s converted  dictionary
#             dcp=(dcp+cnvf2) 
#         print(f"decoded Value : {dcp}")               #decoding plus


