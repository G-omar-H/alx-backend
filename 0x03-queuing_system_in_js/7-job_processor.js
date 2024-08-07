const kue = require('kue');

const blacklist = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
    if (blacklist.includes(phoneNumber)) {
        done(new Error(`Phone number ${phoneNumber} is blacklisted`));
    }
    job.progress(0, 50);
    console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
    job.progress(50, 100);
    return done();
};

const queue = kue.createQueue();
queue.process('push_notification_code_2', 2, (job, done) => {
    sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
