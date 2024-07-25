indexMappingo = {
    "properties":{
        "uniq_id":{
            "type":"long"
        },
        "product_name":{
            "type":"text"
        },
        "brand":{
            "type":"text"
        },
        "retail_price":{
            "type":"long"
        },
        "discounted_price":{
            "type":"long"
        },
        "images":{
            "type":"long"
        },
        "description":{
            "type":"text"
        },
        "DescriptionVector":{
            "type":"dense_vector",
            "dims": 768,
            "index":True,
            "similarity": "l2_norm"
        }

    }
}