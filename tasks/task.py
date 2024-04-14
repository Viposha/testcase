class Pagination:
    def __init__(self, data, items_on_page):
        self.data = data
        self.items_on_page = items_on_page

    def item_count(self):
        return len(self.data)

    def page_count(self):
        self.pages = int((self.item_count() / self.items_on_page))
        if (self.item_count() % self.items_on_page) == 0:
            return self.pages
        else:
            self.pages = int(self.pages) + 1
            return self.pages


    def count_items_on_page(self, page_number):
        if (self.item_count() % self.items_on_page) == 0:
            return self.items_on_page
        else:
            self.pagin = []
            for page in range(self.pages):
                self.pagin.append(self.items_on_page)
            self.pagin[-1] =  self.item_count() % self.items_on_page
            try:
                return self.pagin[page_number]
            except IndexError as eror:
                return ("Invalid index. Page is missing")


    def find_page(self, data):
        pass
    
    def display_page(self, page_number):
        pass

pages = Pagination('Your beautiful text111', 3)
print(pages.page_count())
print(pages.item_count())
print(pages.count_items_on_page(0))
print(pages.count_items_on_page(8))
