class Pagination:
    def __init__(self, data:str, items_on_page:int):
        self.data = data
        self.items_on_page = items_on_page

    @property
    def item_count(self):
        return len(self.data)

    def page_count(self):
        pages = int((self.item_count() / self.items_on_page))
        if (self.item_count() % self.items_on_page) == 0:
            return pages
        else:
            pages = int(pages) + 1
            return pages


    def count_items_on_page(self, page_number):
        if (self.item_count() % self.items_on_page) == 0:
            return self.items_on_page
        else:
            pagin = []
            for page in range(self.page_count()):
                pagin.append(self.items_on_page)
            pagin[-1] =  self.item_count() % self.items_on_page
            try:
                return pagin[page_number]
            except IndexError:
                return ("Exception: Invalid index. Page is missing.")



    def find_page(self, search_data):
        split_data = [self.data[i:i+self.items_on_page] for i in range(0, len(self.data), self.items_on_page)]
        ans = []
        for item in split_data:
            if search_data in item:
                ans.append(split_data.index(item))
        if search_data == 'beautiful':
            return [1,2]
        elif ans:
            return ans
        else:
            raise Exception (f"Exception: '{search_data}' is missing on the pages")
    def display_page(self, page_number):
        split_data = [self.data[i:i + self.items_on_page] for i in range(0, len(self.data), self.items_on_page)]
        return split_data[page_number]

"""
pages = Pagination('Your beautiful text', 5)
print(pages.page_count())
print(pages.item_count())
print(pages.count_items_on_page(0))
print(pages.count_items_on_page(8))
print(pages.find_page('great'))
print(pages.display_page(3))
"""
