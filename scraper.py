import requests
import pandas as pd

url = "https://www.jaspermorrisonshop.com/products.json?limit=250&page1"

r = requests.get(url)
data = r.json()

product_list = []

for item in data['products']:
  title = item['title']
  body_html = item['body_html']
  handle = item['handle']
  created = item['created_at']
  product_type = item['product_type']
  published_at = item['published_at']
  created_at = item['created_at']
  updated_at = item['updated_at']
  vendor = item['vendor']
  tags = ', '.join(item['tags']) if item['tags'] else 'None'

  if item['images']:
        imageSrc = item['images'][0]['src']
        imagePosition = item['images'][0]['position']
  else:
        imagesrc = 'None'

  for variant in item['variants']:
    price = variant['price']
    sku = variant['sku']
    available = variant['available']

    product = {
      'Title': title,
      'Handle': handle,
      'Vendor': vendor,
      'created': created,
      'product_type': product_type,
      'published_at': published_at,
      'created_at' : created_at,
      'updated_at' : updated_at,
      'price': price,
      'sku': sku,
      'Tags': tags,
      'available': available,
      'Image Src': imageSrc,
      'Image Position': imagePosition,
      'Body (HTML)': body_html
    }

    product_list.append(product)
    
    print(product)
    df = pd.DataFrame(product_list)
    df.to_csv('products.csv')
