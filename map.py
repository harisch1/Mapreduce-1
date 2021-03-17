""" Map(key, value) {
    // key1: Child,
    // value1: Parent
    // key 2: Parent
    // value: Child
    //Adding 1 to parent and 2 to child to be able to distinguish
    //Same key will mean parent_1 is grandparent of child_2
    
    For each parent, child in table:
        emit(child, parent+"_1");
        emit(parent, Child+"_2");
} """

import sys
def map():
    for line in sys.stdin: 
    
        names = line.split("\t")

        #print(names)
        key = names[0].strip()
        value = names[1].strip()
        print(key, value + "_1")
        print(value, key+ "_2")

if __name__ == "__main__":
    map()
