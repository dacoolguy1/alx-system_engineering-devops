#!/usr/bin/env python3
class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError("""put must be
                                  implemented in your cache class""")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError("""get must be
                                  implemented in your cache class""")


class BasicCache(BaseCaching):
    """ a class BasicCache that inherits
    from BaseCaching and is a caching system:
    """

    def __init__(self):
        """initialization
        """
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """Add an item to the dictionary Cach

        """
        # dict_obj = self.cache_data
        # dict_obj.key = key
        # dict_obj.value = item
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """Must return the value in self.cache_data linked to key.
        """
        if key is not None:
            return self.cache_data.get(key, None)
        return None
        # return self.cache_data.get(key, None)
    # put("A", "Hello")
# BasicCache().put("A", "Hello")
# BasicCache().print_cache()


if __name__ == "__main__":
    basic_cache = BasicCache()
    basic_cache.put("A", "Hello")
    basic_cache.get('B')
    basic_cache.print_cache()
