from product import Product
import mysql.connector
import pytest

def test_fetchAll():
    assert type(Product.fetchAll()) is list
    for p in Product.fetchAll():
        assert isinstance(p, Product)

def test_find():
    assert isinstance(Product.find(1), Product)
    assert Product.find(1).nome == "tosaerba"
    assert Product.find(1).prezzo == 289.99
    assert Product.find(1).marca == "marca"

def test_create():
    product = {
                "marca": "nonloso",
                "nome": "prodotto",
                "prezzo": 111
            }
    creato = Product.create(product)
    assert isinstance(creato, Product)
    assert creato.nome == product["nome"]
    assert creato.marca == product["marca"]
    assert creato.prezzo == product["prezzo"]

def test_update():
    params = {
                "marca": "prova",
                "nome": "nomeProdotto",
                "prezzo": 222
            }
    product = Product.find(2)
    assert product.update(params)
    assert product.nome == params["nome"]
    assert product.marca == params["marca"]
    assert product.prezzo == params["prezzo"]

def test_delete():
    product = Product.find(3)
    product.delete()
    try:
        product.find(2)
        assert False
    except mysql.connector.Error:
        assert True
