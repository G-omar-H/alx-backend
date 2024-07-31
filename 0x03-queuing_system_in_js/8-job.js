const kue = require('kue');

function createPushNotificationsJobs(jobs, queue) {
    if (!jobs.constructor == Array) {
        throw new Error('Jobs is not an array')
    };
    jobs.forEach((job) => {
        const pushCode = queue.create('push_notification_code_3', job).save((err) => {
            if (!err) {
                console.log(`Notification job created: ${pushCode.id}`);
            } else console.log(`Notification job ${pushCode.id} failed: ${err}`);
        }).on('progress', (progress) => {
            console.log(`Notification job ${pushCode.id} ${pushCode.progress}% complete`);
        }).on('complete', (result) => {
            console.log(`Notification job ${pushCode.id} completed`);
        });
    });
}
module.exports = createPushNotificationsJobs;
