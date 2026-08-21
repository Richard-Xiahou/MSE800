#include "Database.h"

#include <iostream>

Database::Database()
{
    db = nullptr;
}

Database::~Database()
{
    closeDatabase();
}

bool Database::openDatabase(std::string dbName)
{
    int result;
    result = sqlite3_open(dbName.c_str(), &db);

    if(result != SQLITE_OK)
    {
        std::cout << "Open database failed." << std::endl;
        return false;
    }
    std::cout << "Database opened successfully." << std::endl;

    return true;
}

void Database::closeDatabase()
{
    if(db != nullptr)
    {
        sqlite3_close(db);
        db = nullptr;
        std::cout << "Database closed." << std::endl;
    }
}

sqlite3* Database::getDatabase()
{
    return db;
}

void Database::createTables()
{
    char* errorMessage = nullptr;

    std::string sql =
    "CREATE TABLE IF NOT EXISTS Customer("
    "customer_id INTEGER PRIMARY KEY,"
    "first_name TEXT,"
    "last_name TEXT,"
    "phone TEXT);"

    "CREATE TABLE IF NOT EXISTS Currency("
    "currency_id INTEGER PRIMARY KEY,"
    "currency_code TEXT,"
    "currency_name TEXT);"

    "CREATE TABLE IF NOT EXISTS ExchangeRate("
    "rate_id INTEGER PRIMARY KEY,"
    "from_currency INTEGER,"
    "to_currency INTEGER,"
    "rate REAL);"

    "CREATE TABLE IF NOT EXISTS Transaction("
    "transaction_id INTEGER PRIMARY KEY,"
    "customer_id INTEGER,"
    "from_currency INTEGER,"
    "to_currency INTEGER,"
    "amount REAL,"
    "rate_used REAL,"
    "amount_received REAL);";

    int result;

    result = sqlite3_exec(
        db,
        sql.c_str(),
        nullptr,
        nullptr,
        &errorMessage
    );

    if(result != SQLITE_OK)
    {
        std::cout << errorMessage << std::endl;
        sqlite3_free(errorMessage);
    }
    else
    {
        std::cout << "Tables created successfully." << std::endl;
    }
}