import time
import sqlite3
import pandas as pd

tiny = sqlite3.connect('nyc_yellow_tiny.db')
big = sqlite3.connect('nyc_yellow_big.db')

#Creation database
tdata = pd.read_csv(r"D:\Study\бд\laba_3\nyc_yellow_tiny.csv")
tdata.to_sql('trips', tiny, if_exists='replace', index=False)
bdata = pd.read_csv(r"D:\Study\бд\laba_3\nyc_yellow_big.csv")
bdata.to_sql('trips', big, if_exists='replace', index=False)

cursor = tiny.cursor()
q1 = 'SELECT VendorID, count(*) FROM trips GROUP BY 1;'
q2 = 'SELECT passenger_count, avg(total_amount) FROM trips GROUP BY 1;'
q3 = '''SELECT passenger_count, strftime('%Y', tpep_pickup_datetime), count(*) FROM trips GROUP BY 1, 2;'''
q4 = '''SELECT passenger_count, strftime('%Y', tpep_pickup_datetime), round(trip_distance), count(*) FROM trips GROUP BY 1, 2, 3 ORDER BY 2, 4 desc;'''

print('for tiny data')
cursor = tiny.cursor()
sum1, sum2, sum3, sum4 = 0, 0, 0, 0
for i in range(10):
    #q1
    t0 = time.perf_counter()
    cursor.execute(q1)
    result1 = cursor.fetchall()
    t1 = time.perf_counter()
    sum1 += (t1 - t0)
    #q2
    t0 = time.perf_counter()
    cursor.execute(q2)
    result2 = cursor.fetchall()
    t1 = time.perf_counter()
    sum2 += (t1 - t0)
    #q3
    t0 = time.perf_counter()
    cursor.execute(q3)
    result3 = cursor.fetchall()
    t1 = time.perf_counter()
    sum3 += (t1 - t0)
    #q4
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
cursor.close()
tiny.close()

print('for big data')
cursor = big.cursor()
sum1, sum2, sum3, sum4 = 0, 0, 0, 0
for i in range(10):
    #q1
    t0 = time.perf_counter()
    cursor.execute(q1)
    result1 = cursor.fetchall()
    t1 = time.perf_counter()
    sum1 += (t1 - t0)
    #q2
    t0 = time.perf_counter()
    cursor.execute(q2)
    result2 = cursor.fetchall()
    t1 = time.perf_counter()
    sum2 += (t1 - t0)
    #q3
    t0 = time.perf_counter()
    cursor.execute(q3)
    result3 = cursor.fetchall()
    t1 = time.perf_counter()
    sum3 += (t1 - t0)
    #q4
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
cursor.close()
big.close()
