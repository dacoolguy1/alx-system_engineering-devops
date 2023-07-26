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


class FIFOCache(BaseCaching):
    """Inherits from BaseCaching and is a caching system
    """
    def __init__(self):
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """Must assign to the dictionary
           self.cache_data the item value for the key key

        Args:
            key (_type_): _description_
            item (_type_): _description_
        """
        self.cache_data[key] = item
        if key is None or item is None:
            pass
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Get the first item in the cache
            discarded_key = next(iter(self.cache_data))

            # Remove the first item from the cache
            del self.cache_data[discarded_key]  # deleting this particular key

            # Print the discarded key
            print("DISCARD:", discarded_key)

        print(self.cache_data)

    def get(self, key):
        """Must return the value in self.cache_data linked to key.
        """
        if key is not None:
            return self.cache_data.get(key, None)
        return None


if __name__ == "__main__":
    my_cache = FIFOCache()
    my_cache.put("A", "Hello")
    my_cache.put("B", "World")
    my_cache.put("C", "Holberton")
    my_cache.put("D", "School")
    my_cache.print_cache()
    my_cache.put("E", "Battery")
    my_cache.print_cache()
    my_cache.put("C", "Street")
    my_cache.print_cache()
    my_cache.put("F", "Mission")
    my_cache.print_cache()
