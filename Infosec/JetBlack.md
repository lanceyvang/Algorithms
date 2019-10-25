
# Jetblack
* Jenny Fleiss & Marc Lore
* Text message-based personal concierge service.
* Walmart Store No. 8 incubator
* J ai-assistant

# MVC - Model, View, Controller
![](https://media.geeksforgeeks.org/wp-content/uploads/MVC-Design-Pattern.png)
* Popular way to organize your code by it's function. 
* Design pattern, keeps code DRY and reduce time to develop applications.
* Connects user interface to data models.
* Model - Structure of data in a software application.
* View - Collection of classes of the user interface (buttons, display boxes, etc.)
* Controller - Classes connecting the model and the view
    * Used to communicate between classes in the model and view.

# NoSQL
- **N**ot **O**nly **S**QL
* Doesn't use the tabular schema of rows and columns in most traditional database. 
* What all these data stores have in common is that they don't use a relational model.
    * Most specific in the type of data they support and how data can be queried. 
- Flexible
* Used for big data, real-time apps
* Multiple types:
    * Document 
        * MongoDB, CouchDB 
        * (similar to JSON, key/value pairs)
        * Schema-less and dynamic
    * Column 
        * Apache Cassandra
            * Optimized for reading and writing data in columns instead of rows.
            * Analytics, reduces overall disk I/O requirements and amount of data needed to load from the disk.

    * Key/Value stores
        * Redis
        * Couchbase
        * Huge data set with very simple data
        * Extremely fast but not very customizable, similar to hash
    * Cache Systems
        * Redis
        * Memcache 
    * JSON documents
    * Graphs, edge and vertices
        * Neo4J
* Big Data
    * Data sets that are so large, tradition storage and processing are starting to become inadequate.
    * Due to Social Networks like Facebook
    * Search engines like Google
* Handles a lot of data and does it quickly
* Data model is extremely flexible.
* Don't have to define tables and columns, no tables and columns.
* Cheaper to manage
    * Less system admins, not much to do, less to manage.
* Scaling 
    * Horizontal Scaling (Scale-Out)
        * SQL uses vertical scaling (Scale-In)
    * Cluster of nodes is cheaper than one super high end server.

# SQL (Relational)
* Great for relational data
    * Rows and columns
* MySQL or PostgreSQL
    * Have to structure the data in a predefined schema. 
    * Model tables and fields.
    * Datatype of each fields, varchar, text, integer
* ORM, Object Relational Mapper such as Sequelize 
* Normalization
    * Eliminates redundancy 
    * Less space as possible, better performance
* Structured Query Language
* Data integrity rules using foreign constraint. 
* ACID Compliance: All or nothing transaction rule, all of the action or non of the action.
    * Atomicity 
    * Consistency 
    * Isolation
    * Durability 
