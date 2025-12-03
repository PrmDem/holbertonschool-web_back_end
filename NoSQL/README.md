# Python - NoSQL
Where SQL uses structured tables and relationships to organise data, NoSQL is the flexible alternative. It stores unstructured data, allows for greater scalability and an overall better performance for large amounts of data.<br/>
Through this project we'll learn how to use MongoDB, which stores data in JSON-like documents – eg key-value pairs in a dictionary.

## Requirements
### For Python files:
* Allowed editors: vi, vim, emacs
* All files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.9)
* All files should start with `#!/usr/bin/env python3` and end with a new line
* Code should use the pycodestyle style (version 2.5.)
* File length will be tested using wc
* All functions, modules, and classes should have a documentation
* Code should not be executed when imported (by using `if __name__ == "__main__":`)
### For MongoDB command files:
* All files will be interpreted/compiled on Ubuntu 20.04 LTS using MongoDB (version 4.4)
* All files should start with a comment and end with a new line
* The length of your files will be tested using wc

## Tasks overview
### General information
__Number of tasks:__ 13<br/>
__Completed:__ 11<br/>
__Passed:__ 10<br/>

### Details
#### 0. List all databases
Lists all databases in MongoDB.<br/>
See file [`0-list_databases`](./0-list_databases)
#### 1. Create a database
Creates or uses the database `my_db`.<br/>
See file [`1-use_or_create_database`](./1-use_or_create_database)
#### 2. Insert document
Inserts a document in the collection `school`. The document's sole attribute is `name`, with the value `Holberton school`.<br/>
The database name will be passed as an option in the mongo command.<br/>
See file [`2-insert`](./2-insert)
#### 3. All documents
Lists all the documents in the `school` collection.<br/>
See file [`3-all`](./3-all)
#### 4. All matches
Lists all documents with `name="Holberton school"` in the collection `school`.<br/>
See file [`4-match`](./4-match)
#### 5. Count
Displays the number of documents in the collection `school`.<br/>
See file [`5-count`](./5-count)
#### 6. Update
Adds attribute `address: "972 Mission street"` to all documents in the collection `school` where `name: "Holberton school"`.<br/>
See file [`6-update`](./6-update)
#### 7. Delete by match
Deletes all documents with `name="Holberton school"` in the collection `school`.<br/>
See file [`7-delete`](./7-delete)
#### 8. List all documents in Python
Write a Python function `list_all()` that lists all documents in a collection.<br/>
See file [`8-all.py`](./8-all.py)
#### 9. Insert a document in Python
Inserts a new document in a collection based on kwargs. Returns the new document's id.<br/>
See file [`9-insert_school.py`](./9-insert_school.py)
#### 10. Change school topics
Changes all topics of a school collection document according to its name.<br/>
See file [`10-update_topics.py`](./10-update_topics.py)
#### 11. Where can I learn Python?
<br/>
See file [``](./)
#### 12. Log stats
<br/>
See file [``](./)
