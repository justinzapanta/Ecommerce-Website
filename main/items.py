from seller.models import Item, Cart


class Items():
    def __init__(self):
        self.items = Item.objects.filter(item_quantity__gt=0)
    
    def get_type(self, search=''):
        type_list = []
        items = Item.objects.filter(item_name__icontains=search, item_quantity__gt=0)

        for item in items:
            if item.item_type.title() not in type_list:
                type_list.append(item.item_type.title())

        return type_list

    def search(self, search):
        return Item.objects.filter(item_name__icontains=search, item_quantity__gt=0)
    

    def for_column(self, items):
        item_list = []
        temp_list = []

        for index, item in enumerate(items):
            temp_list.append(item)
                
            if (index + 1) % 3 == 0:
                item_list.append(temp_list)
                temp_list = []
            elif len(items)-1 == index:
                item_list.append(temp_list)

        return item_list
    
