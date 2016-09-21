class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update


class MappingSubclass(Mapping):

    def update(self, keys, values):
        for item in zip(keys, values):
            self.items_list.append(item)

mapping = Mapping(['a','b','c'])
mappingSubclass = MappingSubclass([])
mappingSubclass.update([3,4,5],['5','6','7'])
print(mapping.items_list)
print(mappingSubclass.items_list)