import psycopg2


conn = psycopg2.connect\
("host=localhost dbname=tweet_text user=postgres password=tmobile91")

cur=conn.cursor()
conn.autocommit=True

create_table_cluster="create table bot_cluster (date TIMESTAMP,\
                                        clstr_ind INT,\
                                        screen_name TEXT,\
                                        clstr_len INT,\
                                        user_id BIGINT,\
                                        PRIMARY KEY (date, clstr_ind,screen_name));"

cur.execute(create_table_cluster)

#cur.execute(create_table3)

conn.autocommit=False
conn.close()

count=0
for row in data:
    cur.execute("INSERT INTO bot_cluster(date,clstr_ind,screen_name,clstr_len,user_id\)\
                               values (%s,%s,%s,%s,%s)"\
                               ,(str(row[0]),row[1],row[2],row[3],row[4]))
    
    if (count==10000):
        conn.commit()
        count=0
        print('\n commit \n')
    else:
        count=count+1

        
conn.close()    