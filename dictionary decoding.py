
cd={"/":"a","e":"b","f":"c","g":"d","c":"e","b":"f","a":"g","(":"h","*":"i","&":"j",
    "^":"k","9":"l","8":"m","7":"n","6":"o","n":"p","%":"q","$":"r","#":"s","@":"t",
    "!":"u","1":"v","2":"w","3":"x","4":"y","5":"z","-":" "}
cnvf2=""
dcp=""

en=input("\nEnter Filename To Decode : ").lower()
enp=f"{en}.txt"
with open(enp,"r") as f:
    l=f.read()
    print(f"\nEncoaded Value Is : {l}")
    str=str(l)
for j in str:
    # print(cd[j])
    cnvf2=(cd[j]) #s converted  dictionary
    dcp=(dcp+cnvf2) 
print(f"\nDecoded Value Is : {dcp}")  

save=input("\nEnter Filename To Save Decoaded data : ").lower()
sv=f"{save}.txt"

with open(sv,"w") as f:
    f.write(dcp)
print(f"\nFile Is Successfully Saved In {sv}")