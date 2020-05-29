import Adafruit_DHT
import time
import datetime
import urllib.request
import pymysql

sensor=Adafruit_DHT.DHT11
pin=21
conn=pymysql.connect('210.119.12.52','test_usr','mysql_p@ssw0rd','shopdb',charset='utf8')

try:
    while True:
        wtime=datetime.datetime.now()
        humid,temp=Adafruit_DHT.read_retry(sensor,pin)
        if humid is not None and temp is not None:
            print(wtime,'Temp={0:0.1f}*C humid={1:0.1f}%'.format(temp,humid))
            curs=conn.cursor()
            query="""INSERT INTO shopdb.iotmachine(currents_time,machine_id,temperature,humidity)
                   VALUES(%s,%s,%s,%s)"""
            data=(wtime.strftime("%Y-%m-%d %H:%M:%S"),'Moon',temp,humid)
            curs.execute(query,data)
            conn.commit()
            time.sleep(10)
        else:
            print("fail")
        time.sleep(1)
finally:
    curs.close()
    conn.close()