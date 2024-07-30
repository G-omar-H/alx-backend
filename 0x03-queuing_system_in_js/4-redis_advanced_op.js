import redis from 'redis';

const client = redis.createClient();

client.on('error', (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
});

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

const values = {
    Portland: '50',
    Seattle: '80',
    'New York': '20',
    Bogota: '20',
    Cali: '40',
    Paris: '2'
};

client.del('HolbertonSchools', (err, response) => {
    if (err) {
        console.error('Error deleting hash:', err);
    } else {
        Object.keys(values).forEach((key) => {
            client.hset('HolbertonSchools', key, values[key], (err, res) => {
                if (err) {
                    console.error('Error setting hash field:', err);
                } else {
                    console.log('Field set response:', res);
                }
            });
        });

        client.hgetall('HolbertonSchools', (err, data) => {
            if (err) {
                console.error(err);
            } else {
                console.log('Hash data:', data);
            }
            
            client.quit();
        });
    }
});
