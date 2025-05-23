# PyRDB

A toy relational-database engine in Python, built to learn how RDBMS internals work.

**Status:** Schema-driven file storage is implemented; basic inserts and selects succeed.

## Features

- **Schema-driven**: define tables and columns in a JSON file.
- **Binary storage**: data is written to and read from binary files.
- **Simple API**: supports `INSERT` and full-table `SELECT`.
  - Foreign-key enforcement: _not yet supported_.
  - Row filtering: _not yet supported_.

## Roadmap

### Next steps

#### DB internals
- Set up primary keys - one b-tree index file per table
  - addition of an index to the binary tree
  - deletion of an index and taking care how to either mantain or update the memory offsets correspomnding to the oter indexes.
- Enforce foreign-key constraints  
- Implement `WHERE`-clause filtering
- Support join operations

#### SQL parser
Parse SQL commands into functions

#### DB server
Build a TCP-socket server with:
- Event listener  
- SQL-text parser
- Client authentication

#### Front end
- Develop a minimal web client interface
- Require authentication before quering
