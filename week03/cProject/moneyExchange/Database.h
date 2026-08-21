
#ifndef DATABASE_H
#define DATABASE_H

#include <sqlite3.h>
#include <string>

class Database
{
private:
    sqlite3* db;

public:
    Database();
    ~Database();

    bool openDatabase(std::string dbName);
    void closeDatabase();
    void createTables();

    sqlite3* getDatabase();
};

#endif