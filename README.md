# laba3

Лабораторная работа по базам данных №3

Описание проекта:

Проект реализован на двух типах данных: tiny и big - размером 115 МБ и 697 МБ соответвенно. В каждом из 5 py файлов реализованы 4 sql запроса на каждую базу данных (tiny и big) для конкретной библиотеки.

SQL запросы:

1. SELECT VendorID, count(*) FROM trips GROUP BY 1;
2. SELECT passenger_count, avg(total_amount) FROM trips GROUP BY 1;
3. SELECT passenger_count, extract(year from tpep_pickup_datetime), count(*) FROM trips GROUP BY 1, 2;
4. SELECT passenger_count, extract(year from tpep_pickup_datetime), round(trip_distance), count(*)
     FROM trips GROUP BY 1, 2, 3 ORDER BY 2, 4 desc;

Впечатления от библиотек:

Больше всего понравилась библиотека duckdb, так как она, с одной стороны, очень простая в плане синтаксиса, а с другой, самая быстрая из всех данных библиотек. Меньше всего понравилась библиотека pandas, так как у нее совершенно другой синтаксис, на мой взгляд, он сложнее, по сравнению с другими библиотеками.

Графики:

1) на маленьких данных

![image](https://github.com/SkyPlusik/laba3/assets/150513344/5d5e4b2e-53f5-4964-bf71-e88a088f8bd7)
![image](https://github.com/SkyPlusik/laba3/assets/150513344/02ac7e0e-cb26-4e00-874c-8b5bbcc10b96)

2) на больших данных

![image](https://github.com/SkyPlusik/laba3/assets/150513344/b423415d-7ac4-4117-9b0b-65f4f4e905f7)
![image](https://github.com/SkyPlusik/laba3/assets/150513344/cce091fb-4fb0-445b-b205-581dfa71f2d4)


Анализ графиков:

Самой быстрой библиотекой на всех запросах и данных любого размера оказалась duckdb. Это происходит потому, что она выполняет запросы путём векторизации (ориентированной на столбцы), в то время как другие СУБД (SQLite, PostgreSQL и другие) обрабатывают каждую строку последовательно. Самые медленные библиотеки - SQLite и SQLAlchemy, причем их время работы примерно одинаковое, так как в этом случае SQLAlchemy реализована на базе SQLite. 
