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
- Enforce foreign-key constraints  
- Implement `WHERE`-clause filtering
- Support join operations  
- Build a TCP-socket server with:
  - Event listener  
  - SQL-text parser  
- Develop a minimal web client interface
