import time
import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

try:
    conn = psycopg2.connect(user="postgres",
                                  password="123456",
                                  host="localhost",
                                  port="5432")
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conn.cursor()

    # Creation
    sql_create_database = 'create database postgres_db'
    cursor.execute(sql_create_database)

    print('for tiny data')
    sum1, sum2, sum3, sum4 = 0, 0, 0, 0
    q1 = 'SELECT "VendorID", count(*) FROM public.trips group by 1;'
    q2 = 'SELECT "passenger_count", avg(total_amount) FROM public.trips GROUP BY 1;'
    q3 = 'SELECT "passenger_count", extract(year from "tpep_pickup_datetime"), count(*) FROM public.trips GROUP BY 1, 2;'
    q4 = 'SELECT "passenger_count", extract(year from "tpep_pickup_datetime"), round("trip_distance"), count(*) FROM public.trips GROUP BY 1, 2, 3 ORDER BY 2, 4 desc;'
    for i in range(10):
        # q1
        t0 = time.perf_counter()
        cursor.execute(q1)
        result1 = cursor.fetchall()
        t1 = time.perf_counter()
        sum1 += (t1 - t0)
        # q2
        t0 = time.perf_counter()
        cursor.execute(q2)
        result2 = cursor.fetchall()
        t1 = time.perf_counter()
        sum2 += (t1 - t0)
        # q3
        t0 = time.perf_counter()
        cursor.execute(q3)
        result3 = cursor.fetchall()
        t1 = time.perf_counter()
        sum3 += (t1 - t0)
        # q4
        t0 = time.perf_counter()
        cursor.execute(q4)
        result4 = cursor.fetchall()
        t1 = time.perf_counter()
        sum4 += (t1 - t0)
        if i == 9:
            print("First query")
            print("Result: ", result1)
            print("Average time: ", sum1 / 10)
            print()
            print("Second query")
            print("Result: ", result2)
            print("Average time: ", sum2 / 10)
            print()
            print("Third query")
            print("Result: ", result3)
            print("Average time: ", sum3 / 10)
            print()
            print("Fourth query")
            print("Result: ", result4)
            print("Average time: ", sum4 / 10)
            print()

    print('for big data')
    sum1, sum2, sum3, sum4 = 0, 0, 0, 0
    q1 = 'SELECT "VendorID", count(*) FROM public.taxi group by 1;'
    q2 = 'SELECT "passenger_count", avg(total_amount) FROM public.taxi GROUP BY 1;'
    q3 = 'SELECT "passenger_count", extract(year from "tpep_pickup_datetime"), count(*) FROM public.taxi GROUP BY 1, 2;'
    q4 = 'SELECT "passenger_count", extract(year from "tpep_pickup_datetime"), round("trip_distance"), count(*) FROM public.taxi GROUP BY 1, 2, 3 ORDER BY 2, 4 desc;'
    for i in range(10):
        # q1
        t0 = time.perf_counter()
        cursor.execute(q1)
        result1 = cursor.fetchall()
        t1 = time.perf_counter()
        sum1 += (t1 - t0)
        # q2
        t0 = time.perf_counter()
        cursor.execute(q2)
        result2 = cursor.fetchall()
        t1 = time.perf_counter()
        sum2 += (t1 - t0)
        # q3
        t0 = time.perf_counter()
        cursor.execute(q3)
        result3 = cursor.fetchall()
        t1 = time.perf_counter()
        sum3 += (t1 - t0)
        # q4
        t0 = time.perf_counter()
        cursor.execute(q4)
        result4 = cursor.fetchall()
        t1 = time.perf_counter()
        sum4 += (t1 - t0)
        if i == 9:
            print("First query")
            print("Result: ", result1)
            print("Average time: ", sum1 / 10)
            print()
            print("Second query")
            print("Result: ", result2)
            print("Average time: ", sum2 / 10)
            print()
            print("Third query")
            print("Result: ", result3)
            print("Average time: ", sum3 / 10)
            print()
            print("Fourth query")
            print("Result: ", result4)
            print("Average time: ", sum4 / 10)
            print()

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)
finally:
    if conn:
        cursor.close()
        conn.close()
