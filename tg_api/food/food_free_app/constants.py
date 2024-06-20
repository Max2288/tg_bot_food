ADRESES = [
    {
        'id': 1,
        "country": "Russia",
        "city": "Moscow",
        "street": "Arbat",
        "building_num": 23,
        "entrance": 1,
        "floor": 5,
        "apartment_number": 12,
        "coordinates": "POINT (37.604050 55.751244)"
    },
    {
        'id': 2,
        "country": "USA",
        "city": "New York",
        "street": "Broadway",
        "building_num": 100,
        "entrance": 2,
        "floor": 10,
        "apartment_number": 45,
        "coordinates": "POINT (-73.985130 40.758896)"
    },
    {
        'id': 3,
        "country": "UK",
        "city": "London",
        "street": "Baker Street",
        "building_num": 221,
        "entrance": 1,
        "floor": 3,
        "apartment_number": 10,
        "coordinates": "POINT (-0.158555 51.523763)"
    },
    {
        'id': 4,
        "country": "Canada",
        "city": "Toronto",
        "street": "King Street",
        "building_num": 50,
        "entrance": 3,
        "floor": 8,
        "apartment_number": 23,
        "coordinates": "POINT (-79.383186 43.653225)"
    },
    {
        'id': 5,
        "country": "Australia",
        "city": "Sydney",
        "street": "George Street",
        "building_num": 200,
        "entrance": 4,
        "floor": 15,
        "apartment_number": 50,
        "coordinates": "POINT (151.209900 -33.865143)"
    },
    {
        'id': 6,
        "country": "Germany",
        "city": "Berlin",
        "street": "Unter den Linden",
        "building_num": 5,
        "entrance": 2,
        "floor": 4,
        "apartment_number": 16,
        "coordinates": "POINT (13.400000 52.517036)"
    },
    {
        'id': 7,
        "country": "France",
        "city": "Paris",
        "street": "Champs-Élysées",
        "building_num": 10,
        "entrance": 1,
        "floor": 6,
        "apartment_number": 30,
        "coordinates": "POINT (2.303765 48.868651)"
    },
    {
        'id': 8,
        "country": "Italy",
        "city": "Rome",
        "street": "Via del Corso",
        "building_num": 50,
        "entrance": 2,
        "floor": 7,
        "apartment_number": 20,
        "coordinates": "POINT (12.479400 41.902783)"
    },
    {
        'id': 9,
        "country": "Spain",
        "city": "Madrid",
        "street": "Gran Vía",
        "building_num": 18,
        "entrance": 1,
        "floor": 5,
        "apartment_number": 14,
        "coordinates": "POINT (-3.703790 40.416775)"
    },
    {
        'id': 10,
        "country": "Japan",
        "city": "Tokyo",
        "street": "Shibuya",
        "building_num": 1,
        "entrance": 3,
        "floor": 9,
        "apartment_number": 45,
        "coordinates": "POINT (139.691706 35.689487)"
    },
    {
        'id': 11,
        "country": "Russia",
        "city": "Sirius",
        "street": "Listopadnaya",
        "building_num": 57,
        "entrance": 2,
        'floor': 1,
        'apartment_number': 1,
        'coordinates': 'POINT (43.405125 39.981354)'
    }
]


SHOPS = [
    {
        "id": 1,
        "name": "Moscow Mart",
        "description": "A popular shopping destination in Moscow.",
        "image": "moscow_mart.png",
        "address": 1
    },
    {
        "id": 2,
        "name": "Broadway Boutique",
        "description": "Trendy boutique in the heart of New York.",
        "image": "broadway_boutique.png",
        "address": 2
    },
    {
        "id": 3,
        "name": "London Emporium",
        "description": "Elegant emporium on Baker Street.",
        "image": "london_emporium.png",
        "address": 3
    },
    {
        "id": 4,
        "name": "Toronto Treasures",
        "description": "Hidden gems of Toronto's King Street.",
        "image": "toronto_treasures.png",
        "address": 4
    },
    {
        "id": 5,
        "name": "Sydney Souvenirs",
        "description": "Unique souvenirs from Sydney.",
        "image": "sydney_souvenirs.png",
        "address": 5
    },
    {
        "id": 6,
        "name": "Berlin Bazaar",
        "description": "Diverse market in Berlin.",
        "image": "berlin_bazaar.png",
        "address": 6
    },
    {
        "id": 7,
        "name": "Parisian Paradise",
        "description": "Luxury items on Champs-Élysées.",
        "image": "parisian_paradise.png",
        "address": 7
    },
    {
        "id": 8,
        "name": "Roman Relics",
        "description": "Historic finds on Via del Corso.",
        "image": "roman_relics.png",
        "address": 8
    },
    {
        "id": 9,
        "name": "Madrid Market",
        "description": "Vibrant market on Gran Vía.",
        "image": "madrid_market.png",
        "address": 9
    },
    {
        "id": 10,
        "name": "Tokyo Treasures",
        "description": "Exclusive items from Shibuya.",
        "image": "tokyo_treasures.png",
        "address": 10
    },
    {
        'id': 11,
        'name': 'Пятёрочка',
        'description': 'Интересный магазин',
        'image': 'some_image_here',
        'address': 11
    }
]


PRODUCTS = [
    {
        'id': 1,
        'name': 'Product 1',
        'description': 'Description for Product 1',
        'price': 9.99,
        'quantity': 50,
        'image': 'product1.jpg',
        'is_hot': True,
        'shop_id': 11,  # Assuming shop ID is 11 for all products
    },
    {
        'id': 2,
        'name': 'Product 2',
        'description': 'Description for Product 2',
        'price': 19.99,
        'quantity': 30,
        'image': 'product2.jpg',
        'is_hot': False,
        'shop_id': 11,
    },
    {
        'id': 3,
        'name': 'Product 3',
        'description': 'Description for Product 3',
        'price': 14.50,
        'quantity': 20,
        'image': 'product3.jpg',
        'is_hot': True,
        'shop_id': 11,
    },
]