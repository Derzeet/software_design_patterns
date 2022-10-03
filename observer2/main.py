from Subject import Shop
from Observer import Client

if __name__ == "__main__":
    shop = Shop()
    shop.updateShop("IPhon 14 Pro")
    client = Client()
    shop.add(client)
    shop.updateShop("IPhon 14 Pro Max")
