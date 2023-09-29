import json


class ProductScrapped:
    name = None
    price = None
    store_id = None
    photo = None

    def __init__(self, name="", price="0.0", store_id=0, photo=""):
        self.name = name
        self.price = price
        self.store_id = store_id
        self.photo = photo
        pass

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "store_id": self.store_id,
            "photo": self.photo
        }


class IScrapperQuery:
    """ InterfaceQuery for prepare query """
    query = None

    def __init__(self, query="acetaminofen"):
        self.query = query
        print("\nInterfaceQuery: " + self.query)
        pass

    def execute_query(self):
        """ run all routines in order to success scrap needed """

    def get_result(self) -> ProductScrapped:
        """ get data from response
        Returns
        -------
        ProductScrapped
            Class product for getting data
        """


