import time
import pandas as pd

tiny = pd.read_csv(r"D:\Study\бд\laba_3\nyc_yellow_tiny.csv")
big = pd.read_csv(r"D:\Study\бд\laba_3\nyc_yellow_big.csv")

print('for tiny data')
sum1, sum2, sum3, sum4 = 0, 0, 0, 0
for i in range(10):
    #q1
    t0 = time.perf_counter()
    result1 = tiny.groupby(["VendorID"]).size()
    t1 = time.perf_counter()
    sum1 += (t1 - t0)
    #q2
    t0 = time.perf_counter()
    result2 = tiny.groupby(["passenger_count"])["total_amount"].mean()
    t1 = time.perf_counter()
    sum2 += (t1 - t0)
    #q3
    t0 = time.perf_counter()
    tiny['Year'] = pd.to_datetime(tiny['tpep_pickup_datetime']).dt.year
    result3 = tiny.groupby(['passenger_count', 'Year']).size()
    t1 = time.perf_counter()
    sum3 += (t1 - t0)
    #q4
    t0 = time.perf_counter()
    tiny['Year'] = pd.to_datetime(tiny['tpep_pickup_datetime']).dt.year
    tiny['trip_distance'] = tiny['trip_distance'].round()
    result4 = tiny.groupby(['passenger_count', 'Year', 'trip_distance']).size().reset_index(name='count').sort_values(['Year', 'count'], ascending=[True, False])
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
for i in range(10):
    #q1
    t0 = time.perf_counter()
    result1 = big.groupby(["VendorID"]).size()
    t1 = time.perf_counter()
    sum1 += (t1 - t0)
    #q2
    t0 = time.perf_counter()
    result2 = big.groupby(["passenger_count"])["total_amount"].mean()
    t1 = time.perf_counter()
    sum2 += (t1 - t0)
    #q3
    t0 = time.perf_counter()
    big['Year'] = pd.to_datetime(big['tpep_pickup_datetime']).dt.year
    result3 = big.groupby(['passenger_count', 'Year']).size()
    t1 = time.perf_counter()
    sum3 += (t1 - t0)
    #q4
    t0 = time.perf_counter()
    big['Year'] = pd.to_datetime(big['tpep_pickup_datetime']).dt.year
    big['trip_distance'] = big['trip_distance'].round()
    result4 = big.groupby(['passenger_count', 'Year', 'trip_distance']).size().reset_index(name='count').sort_values(['Year', 'count'], ascending=[True, False])
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
