# laba3

Лабораторная работа по базам данных №3

Описание проекта:

Проект реализован на двух типах данных: tiny и big - размером 115 МБ и 697 МБ соответвенно. В каждом из 5 py файлов реализованы 4 sql запроса на каждую базу данных (tiny и big) для конкретной библиотеки.

SQL запросы:

1. SELECT VendorID, count(*) FROM trips GROUP BY 1;
2. SELECT passenger_count, avg(total_amount) FROM trips GROUP BY 1;
3. SELECT passenger_count, extract(year from tpep_pickup_datetime), count(*) FROM trips GROUP BY 1, 2;
4. SELECT passenger_count, extract(year from tpep_pickup_datetime), round(trip_distance), count(*) FROM trips GROUP BY 1, 2, 3 ORDER BY 2, 4 desc;

Впечатления от библиотек:

Больше всего понравилась библиотека duckdb, так как она, с одной стороны, очень простая в плане синтаксиса, а с другой, самая быстрая из всех данных библиотек. Меньше всего понравилась библиотека pandas, так как у нее совершенно другой синтаксис по сравнению с другими библиотеками.

Графики:
