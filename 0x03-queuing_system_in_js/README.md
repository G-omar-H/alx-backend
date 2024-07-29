# Queuing System in JS

## Project Overview

Welcome to the **Queuing System in JS** project! This project is part of the **Curriculum Short Specializations** with an average score of **74.33%**. It involves implementing a queuing system using various technologies including Redis, NodeJS, ExpressJS, and Kue.

- **Weight:** 1
- **Start Date:** July 29, 2024, 4:00 AM
- **End Date:** August 1, 2024, 4:00 AM
- **Manual QA Review:** Required (request it upon project completion)

## Resources

### Read or Watch:
- [Redis quick start](https://redis.io/topics/quickstart)
- [Redis client interface](https://github.com/NodeRedis/node-redis)
- [Redis client for Node JS](https://www.npmjs.com/package/redis)
- [Kue](https://github.com/Automattic/kue) (Deprecated but still used in the industry)

## Learning Objectives

By the end of this project, you should be able to:
- Run a Redis server on your machine.
- Perform basic operations using the Redis client.
- Use a Redis client with NodeJS for basic operations.
- Store hash values in Redis.
- Handle async operations with Redis.
- Use Kue as a queue system.
- Build a basic Express app interacting with a Redis server.
- Build a basic Express app interacting with a Redis server and queue.

## Requirements

- **Environment:** Ubuntu 18.04, Node 12.x, Redis 5.0.7+
- **Coding Style:** Files should end with a new line.
- **Files:** A `README.md` file at the root of the project is mandatory.
- **Extension:** Use the `.js` extension for your code.

## Project Structure

### Required Files
- **package.json**

```json
{
  "name": "queuing_system_in_js",
  "version": "1.0.0",
  "description": "Queuing system project using Redis and Kue",
  "main": "index.js",
  "scripts": {
    "start": "node index.js",
    "dev": "nodemon --exec babel-node --presets @babel/preset-env"
  },
  "dependencies": {
    "express": "^4.17.1",
    "kue": "^0.11.6",
    "redis": "^3.1.2"
  },
  "devDependencies": {
    "@babel/core": "^7.11.6",
    "@babel/node": "^7.10.5",
    "@babel/preset-env": "^7.11.5",
    "nodemon": "^2.0.4"
  }
}
```
- **.babelrc**

```json

{
  "presets": ["@babel/preset-env"]
}
```
## Tasks

  1.  Install a Redis Instance
        Download, extract, and compile Redis version higher than 5.0.7.
        Start Redis in the background with src/redis-server &.
        Set and get values in Redis using the Redis client.
        Copy dump.rdb from the Redis directory into the project root.

   2. Node Redis Client
        Install node_redis using npm.
        Create 0-redis_client.js to connect to the Redis server.
        Log connection success or failure messages.

  3.  Node Redis Client and Basic Operations
        Create 1-redis_op.js with functions to set and get values in Redis.
        Use callbacks for operations.

  4.  Node Redis Client and Async Operations
        Create 2-redis_op_async.js using promisify for async/await operations.

  5.  Node Redis Client and Advanced Operations
        Create 4-redis_advanced_op.js to store and display hash values in Redis.

  6.  Node Redis Client Publisher and Subscriber
        Create 5-subscriber.js to subscribe to a Redis channel.
        Create 5-publisher.js to publish messages to the channel.

 7.   Create the Job Creator
        Create 6-job_creator.js to create jobs using Kue.

 8.   Create the Job Processor
        Create 6-job_processor.js to process jobs using Kue.

  9.  Track Progress and Errors with Kue
        Create 7-job_creator.js to handle multiple job data and track progress and errors.

## Getting Started

**Clone the repository:**

```bash

git clone https://github.com/yourusername/alx-backend.git
cd 0x03-queuing_system_in_js
```

**Install dependencies:**

```bash

npm install
```

**Run the Redis server:**

```bash

src/redis-server &
```

**Execute the tasks using npm run dev command:**

```bash

    npm run dev 0-redis_client.js
```

## Repository

    GitHub: alx-backend
    Directory: 0x03-queuing_system_in_js

## Author

OGhazi

