inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
"""
Inventory:
12 arrow
42 gold coin
1 rope
6 torch
1 dagger
"""
def DisplayInventory(inv):
    total_item = 0
    print('Inventory:')
    for k, v in inv.items():
        print(str(v) + ' ' + str(k))
        total_item += v
    print('Total number of items: ' + str(total_item))
#DisplayInventory(inventory)

def addToInventory(inventory,lootlist):
#    for i in range(len(lootlist)):
    for i in lootlist:
        if lootlist[i] in inventory:
            inventory[lootlist[i]] = inventory[lootlist[i]] + 1
        else:
            inventory.setdefault(lootlist[i],1)
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
DisplayInventory(inv)
