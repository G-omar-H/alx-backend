const kue = require('kue');

const queue = kue.createQueue();

const job = queue.createJob('push_notification_code', {
    phoneNumber: 'string',
    message: 'string',
  }).save((err) => {
    if (!err) {
        console.log(`Notification job created: ${job.id}`);
    }
  });

job.on('complete', (result) => {
    console.log('Notification job completed');
}).on('failed', (err) => {
    if (err) {
        console.log('Notification job failed');
    };
});
