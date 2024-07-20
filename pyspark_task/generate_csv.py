import csv, random

products = [
    {"product_id": 1, "product_name": "Product A"},
    {"product_id": 2, "product_name": "Product B"},
    {"product_id": 3, "product_name": "Product C"},
    {"product_id": 4, "product_name": "Product D"},
]

categories = [
    {"category_id": 1, "category_name": "Category X"},
    {"category_id": 2, "category_name": "Category Y"},
    {"category_id": 3, "category_name": "Category Z"},
]

def product_category_generator(products, categories):
    product_category = []
    for product in products:
        num_categories = random.randint(0, len(categories))
        selected_categories = random.sample(categories, num_categories)
        for category in selected_categories:
            product_category.append({
                "product_id": product["product_id"],
                "category_id": category["category_id"]
            })
    return product_category


product_category = product_category_generator(products, categories)

def write_csv(filename, data, fieldnames):
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

if __name__ == '__main__':
    write_csv('pyspark_task/csv/products.csv', products, fieldnames=['product_id', 'product_name'])
    write_csv('pyspark_task/csv/categories.csv', categories, fieldnames=['category_id', 'category_name'])
    write_csv('pyspark_task/csv/product_category.csv', product_category, fieldnames=['product_id', 'category_id'])
