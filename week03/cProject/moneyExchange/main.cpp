#include "Database.h"

// setp 1, test database: clang++ main.cpp Database.cpp -lsqlite3 -o app
// clang++ main.cpp 主程序  Database.cpp 数据库实现  -lsqlite3 链接sql lite3库 -o app 输出可执行文件app
// 以后可以一直使用 clang++ *.cpp -lsqlite3 -o app
int main()
{
    Database database;
    database.openDatabase("moneyExchange.db");
    database.createTables();
    database.closeDatabase();

    return 0;
}