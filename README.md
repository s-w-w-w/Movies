# Movies
SQLite 3 database and CLI interface written in Python for collection of Movies

## Database
Database:

### Table Blockbusters
All tables (1 for now) should be stored in **data/data.db** Blockbusters table create statement

```
CREATE TABLE "Blockbusters" (
	"id"	INTEGER NOT NULL UNIQUE,
	"title"	TEXT NOT NULL,
	"year"	TEXT NOT NULL,
	"score"	NUMERIC NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
)
```
## Interface
Run **./client.py** help on the command line for available options. 