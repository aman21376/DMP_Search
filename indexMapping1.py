index_mapping1 = {
        "properties": {
            "uniq_id": {"type": "keyword"},
            "crawl_timestamp": {"type": "date", "format": "yyyy-MM-dd HH:mm:ss Z"},
            "product_url": {"type": "keyword"},
            "product_name": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}}
            },
            "product_category_tree": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}}
            },
            "pid": {"type": "keyword"},
            "retail_price": {"type": "float"},
            "discounted_price": {"type": "float"},
            "image": {"type": "keyword"},
            "is_FK_Advantage_product": {"type": "boolean"},
            "description": {"type": "text"},
            "product_rating": {"type": "keyword"},
            "overall_rating": {"type": "keyword"},
            "brand": {"type": "keyword"},
            "product_specifications": {
                "type": "text",
                "fields": {"keyword": {"type": "keyword", "ignore_above": 256}}
            },
            "DescriptionVector": {
                "type": "dense_vector",
                "dims": 768,
                "index": True,
                "similarity": "cosine"
            }
        }
    }

