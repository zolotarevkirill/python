menu = {
  "$id": "http://example.com/example.json",
  "type": "object",
  "definitions": {},
  "$schema": "http://json-schema.org/draft-07/schema#",
  "properties": {
    "type": {
      "$id": "/properties/type",
      "type": "string",
      "title": "The Type Schema ",
      "default": "",
      "examples": [
        "articleList"
      ]
    },
    "group": {
      "$id": "/properties/group",
      "type": "array",
      "items": {
        "$id": "/properties/group/items",
        "type": "object",
        "properties": {
          "title": {
            "$id": "/properties/group/items/properties/title",
            "type": "string",
            "title": "The Title Schema ",
            "default": "",
            "examples": [
              "OZON Гид"
            ]
          },
          "tagline": {
            "$id": "/properties/group/items/properties/tagline",
            "type": "string",
            "title": "The Tagline Schema ",
            "default": "",
            "examples": [
              ""
            ]
          },
          "taglineName": {
            "$id": "/properties/group/items/properties/taglineName",
            "type": "string",
            "title": "The Taglinename Schema ",
            "default": "",
            "examples": [
              ""
            ]
          },
          "items": {
            "$id": "/properties/group/items/properties/items",
            "type": "array",
            "items": {
              "$id": "/properties/group/items/properties/items/items",
              "type": "object",
              "properties": {
                "date": {
                  "$id": "/properties/group/items/properties/items/items/properties/date",
                  "type": "integer",
                  "title": "The Date Schema ",
                  "default": 0,
                  "examples": [
                    1513063447
                  ]
                },
                "name": {
                  "$id": "/properties/group/items/properties/items/items/properties/name",
                  "type": "string",
                  "title": "The Name Schema ",
                  "default": "",
                  "examples": [
                    "Тест [тег1 тег2]"
                  ]
                },
                "text": {
                  "$id": "/properties/group/items/properties/items/items/properties/text",
                  "type": "string",
                  "title": "The Text Schema ",
                  "default": "",
                  "examples": [
                    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
                  ]
                },
                "image": {
                  "$id": "/properties/group/items/properties/items/items/properties/image",
                  "type": "array"
                },
                "path": {
                  "$id": "/properties/group/items/properties/items/items/properties/path",
                  "type": "string",
                  "title": "The Path Schema ",
                  "default": "",
                  "examples": [
                    "/antiques/test-teg1-teg2/"
                  ]
                },
                "categoryName": {
                  "$id": "/properties/group/items/properties/items/items/properties/categoryName",
                  "type": "string",
                  "title": "The Categoryname Schema ",
                  "default": "",
                  "examples": [
                    "Антиквариат, винтаж, искусство"
                  ]
                },
                "categoryLink": {
                  "$id": "/properties/group/items/properties/items/items/properties/categoryLink",
                  "type": "string",
                  "title": "The Categorylink Schema ",
                  "default": "",
                  "examples": [
                    "/antiques/"
                  ]
                }
              }
            }
          }
        }
      }
    }
  }
}


categories = {
  "$id": "http://example.com/example.json",
  "type": "object",
  "definitions": {},
  "$schema": "http://json-schema.org/draft-07/schema#",
  "properties": {
    "id": {
      "$id": "/properties/id",
      "type": "integer",
      "title": "The Id Schema ",
      "default": 0,
      "examples": [
        2
      ]
    },
    "code": {
      "$id": "/properties/code",
      "type": "string",
      "title": "The Code Schema ",
      "default": "",
      "examples": [
        "books"
      ]
    },
    "sort": {
      "$id": "/properties/sort",
      "type": "string",
      "title": "The Sort Schema ",
      "default": "",
      "examples": [
        "date"
      ]
    },
    "nPage": {
      "$id": "/properties/nPage",
      "type": "integer",
      "title": "The Npage Schema ",
      "default": 0,
      "examples": [
        1
      ]
    },
    "cPage": {
      "$id": "/properties/cPage",
      "type": "integer",
      "title": "The Cpage Schema ",
      "default": 0,
      "examples": [
        2
      ]
    },
    "title": {
      "$id": "/properties/title",
      "type": "string",
      "title": "The Title Schema ",
      "default": "",
      "examples": [
        "Книги"
      ]
    },
    "meta": {
      "$id": "/properties/meta",
      "type": "array",
      "items": {
        "$id": "/properties/meta/items",
        "type": "object",
        "properties": {
          "type": {
            "$id": "/properties/meta/items/properties/type",
            "type": "string",
            "title": "The Type Schema ",
            "default": "",
            "examples": [
              "opengraph"
            ]
          },
          "property": {
            "$id": "/properties/meta/items/properties/property",
            "type": "string",
            "title": "The Property Schema ",
            "default": "",
            "examples": [
              "og:image"
            ]
          },
          "content": {
            "$id": "/properties/meta/items/properties/content",
            "type": "string",
            "title": "The Content Schema ",
            "default": "",
            "examples": [
              ""
            ]
          }
        }
      }
    },
    "createDate": {
      "$id": "/properties/createDate",
      "type": "integer",
      "title": "The Createdate Schema ",
      "default": 0,
      "examples": [
        1511418147
      ]
    },
    "breadcrumbs": {
      "$id": "/properties/breadcrumbs",
      "type": "array",
      "items": {
        "$id": "/properties/breadcrumbs/items",
        "type": "object",
        "properties": {
          "name": {
            "$id": "/properties/breadcrumbs/items/properties/name",
            "type": "string",
            "title": "The Name Schema ",
            "default": "",
            "examples": [
              "Главная"
            ]
          },
          "path": {
            "$id": "/properties/breadcrumbs/items/properties/path",
            "type": "string",
            "title": "The Path Schema ",
            "default": "",
            "examples": [
              "/"
            ]
          }
        }
      }
    },
    "content": {
      "$id": "/properties/content",
      "type": "array",
      "items": {
        "$id": "/properties/content/items",
        "type": "object",
        "properties": {
          "type": {
            "$id": "/properties/content/items/properties/type",
            "type": "string",
            "title": "The Type Schema ",
            "default": "",
            "examples": [
              "previewArtile"
            ]
          },
          "id": {
            "$id": "/properties/content/items/properties/id",
            "type": "integer",
            "title": "The Id Schema ",
            "default": 0,
            "examples": [
              348
            ]
          },
          "template": {
            "$id": "/properties/content/items/properties/template",
            "type": "string",
            "title": "The Template Schema ",
            "default": "",
            "examples": [
              "standart"
            ]
          },
          "imagePosition": {
            "$id": "/properties/content/items/properties/imagePosition",
            "type": "string",
            "title": "The Imageposition Schema ",
            "default": "",
            "examples": [
              "top"
            ]
          },
          "createDate": {
            "$id": "/properties/content/items/properties/createDate",
            "type": "integer",
            "title": "The Createdate Schema ",
            "default": 0,
            "examples": [
              1511443130
            ]
          },
          "code": {
            "$id": "/properties/content/items/properties/code",
            "type": "string",
            "title": "The Code Schema ",
            "default": "",
            "examples": [
              "luchshie-knigi-nobelevskogo-laureata-2017-goda-kadzuo-isiguro"
            ]
          },
          "name": {
            "$id": "/properties/content/items/properties/name",
            "type": "string",
            "title": "The Name Schema ",
            "default": "",
            "examples": [
              "Лучшие книги нобелевского лауреата 2017 года Кадзуо Исигуро"
            ]
          },
          "text": {
            "$id": "/properties/content/items/properties/text",
            "type": "string",
            "title": "The Text Schema ",
            "default": "",
            "examples": [
              "Кадзуо Исигуро — британский писатель, японец по происхождению, лауреат Нобелевской премии по литературе в 2017 году."
            ]
          },
          "indexPopular": {
            "$id": "/properties/content/items/properties/indexPopular",
            "type": "integer",
            "title": "The Indexpopular Schema ",
            "default": 0,
            "examples": [
              15
            ]
          }
        }
      }
    }
  }
}