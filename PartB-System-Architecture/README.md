- Task: The architecture diagram mentioned in task sheet has following services: DNS, Web server, database, object store. Task is to scale it to the millions of requests. We request you draw up a cloud architectural design with the services 
mentioned to migrate this application into a scalable and cost-effective solution.
- You can use any cloud provider you prefer. 
- As an e-commerce application, the backend needs to handle a different type of 
read and write APIs along with some background jobs. 
- The application relies on some external systems for getting/querying the product 
list. 
- The predicted ecommerce traffic is from around the world with variable peak 
hours. 
- Put the diagram in a separate directory in the repo.

ANSWER: Here we have used AWS cloud platform PAAS & SAAS services.

AWS Services used: 

Frontend:
- Beanstalk: VM(beanstalk managed ec2) for web server, Load balancer, Auto Scalling
- S3: For object store

Backend:
- RDS: Database, scallable, automatic backup
- Elastic Cache: for caching purposes
- Amazon MQ: message broker
- Route 53: DNS
- Cloudfront: for CDN (because predicted ecommerce traffic is from around the world with variable peak hours)

Workflow:
- User access the e-commerce application url which is resolved to an end point from route 53
- The end point is in cloudfront, which will cache to serve global audience.
- Then request will go to application load balancer which is part of Beanstalk.
- application load balancer forwards the request to ec2 instance which is in auto scaling group, here web server is running.
- Cloud watch will monitor and scale out or scale in based on requirement.
- There will be s3 bucket for artifact and object storage.
- For backend request will access to Amazon MQ, Elastic Cache and RDS services.
- Amazon MQ for managing communication and coordination between different parts of a distributed system.
- Application code need to handle both read and write operations. This could involve defining appropriate API routes or endpoints for handling different types of requests.