# In this Section we will Explore about the Continue Statement in for loops
# for i in range(1,10):
#     if i==3 or i==8:
#         continue
#     print(i)
    
item=["Books","stationary","spam","notebook","idcard"]
for i in item:
    if i=="spam":
        continue
    print(i)
        
## Break Statement 
for i in range(2,20):
    if i==9:
        break
    print(i)
    
# Searching using Break statement in List
Items=["Books","Machine","mobile","mouse","leptop","addmin"]
for i in Items:
    if i=="mobile":
        break
    print(i)
   
item_to_found="mobile" 
found_at=None


# searching the element in list 
Items=["Books","Machine","mobile","mouse","leptop","addmin"]
item_to_found="mobile" 
found_at=None

for index in range(len(Items)):
    if Items[index]==item_to_found:
        found_at=index
        break
print("The item you was searching was {0} and is found at {1}".format(item_to_found,found_at))

## Easy aproach to find the Item into the List
Items=["Books","Machine","mobile","mouse","leptop","addmin"]
item_to_found="mouse" 
found_at=None
if item_to_found in Items:
    found_at=Items.index(item_to_found)
    print("item found at position",found_at)