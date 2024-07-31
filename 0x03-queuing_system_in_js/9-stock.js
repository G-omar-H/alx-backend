const express = require('express');
import redis from 'redis';
import util  from 'util';

const app = express();
const port = 1245;
const client = redis.createClient();

client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`)
});


client.on('connect', () => {
    console.log('Redis client connected to the server');
});

const listProducts = [
    {id: 1, name: 'Suitcase 250', price: 50, stock: 4,},
    {id: 2, name: 'Suitcase 450', price: 100, stock: 10,},
    {id: 3, name: 'Suitcase 650', price: 350, stock: 2,},
    {id: 4, name: 'Suitcase 1050', price: 550, stock: 5,}
];

function getItemById(itemId) {
    let tmp;
    listProducts.forEach((item) => {
        if (item.id === parseInt(itemId)) {
            tmp = item;
        }
    });
    return tmp;
};

app.get('/list_products', (req, res) => {
    const temp = [];
    listProducts.forEach((item) => {
        let obj = {};
        obj.itemId = item.id;
        obj.itemName = item.name;
        obj.price = item.price;
        obj.initialAvailableQuantity = item.stock;
        temp.push(obj);
    });
    res.setHeader('Content-Type', 'application/json');
    res.end(JSON.stringify(temp));
})

function reserveStockById(itemId, stock) {
    client.hset('item', itemId, stock);
}

async function getCurrentReservedStockById(itemId) {
    const getAsync = util.promisify(client.hget).bind(client);
    return getAsync('item', itemId);
}

app.get('/list_products/:itemId', async (req, res) => {
    const itemId = req.params.itemId;
    const item = getItemById(itemId);
    console.log(item);
    if (item) {
        item.currentQuantity = await getCurrentReservedStockById(itemId);
        res.setHeader('Content-Type', 'application/json');
        res.end(JSON.stringify(item));
    } else {
        res.setHeader('Content-Type', 'application/json');
        res.end(JSON.stringify( {"status":"Product not found"} ))
    };
});

app.get('/reserve_product/:itemId', (req, res) => {
    const itemId = req.params.itemId;
    const item = getItemById(itemId);
    if (!item) {
        res.setHeader('Content-Type', 'application/json');
        res.end(JSON.stringify({"status":"Product not found"}));
    } else {
        if (!item.stock) {
            res.setHeader('Content-Type', 'application/json');
            res.end(JSON.stringify({"status":"Not enough stock available","itemId":item.id}));
        } else {
            reserveStockById(item.id, item.stock);
            res.setHeader('Content-Type', 'application/json');
            res.end(JSON.stringify({"status":"Reservation confirmed","itemId":item.id}));
        }
    }
});

app.listen(port);
