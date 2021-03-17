
""" Reduce(key, value):
    
    //Key: all parents
    //Value: With "_1" are grandparent and "_2" are grandchild

    if (key.contains("_1")):
        grandparentlist.append(value)
    else:
        grandchildlist.append(value)
     """
     
import sys

def reduce():

    grandparentlist = []
    grandchildlist = []

    for line in sys.stdin:  
        kv = line.split("_") 
        names = kv[0].strip()  
        num = int(kv[1].strip())
        if(num == 1):
            grandparentlist.append(names)
        else:
            grandchildlist.append(names)
       
    #print(grandchildlist)
    #print(grandparentlist)
    print("Grandchild\tGrandparent")
    for grandchild in grandchildlist:
        key1,namec = grandchild.split(" ")
        for grandparent in grandparentlist:
            key2,namep = grandparent.split(" ") 
            if (key1 == key2):
                print(namec,"\t\t", namep)
            
    
if __name__ == "__main__":
    reduce()
