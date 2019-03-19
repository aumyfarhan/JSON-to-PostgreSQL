import psycopg2


conn = psycopg2.connect\
("host=localhost dbname=tweet_text user=postgres password=tmobile91")

cur=conn.cursor()
conn.autocommit=True
#cur.execute("set autocommit on;")

#cur.execute("set transaction read write")
#create_table_space="CREATE TABLESPACE tweet_text LOCATION 'G:/tweet_data_collection';"
#create_database="CREATE DATABASE tweet_text TABLESPACE tweet_text"
#cur.execute(create_table_space)

create_table1="create table tweet_text(tweet_id BIGINT PRIMARY KEY,\
                                        tweet_text TEXT,\
                                        user_id BIGINT NOT NULL,\
                                        lang TEXT,\
                                        post_time TIMESTAMP NOT NULL)"



create_table2="create table user_created_at(user_id BIGINT PRIMARY KEY,\
                                    created_at TIMESTAMP NOT NULL)"


create_table3="create table user_dynamic (user_id BIGINT,\
                                        cur_time TIMESTAMP,\
                                        status INT,\
                                        favorite INT,\
                                        friends INT,\
                                        followers INT,\
                                        name TEXT,\
                                        scr_name TEXT,\
                                        bio TEXT,\
                                        lang TEXT,\
                                        location TEXT,\
                                        PRIMARY KEY (user_id, cur_time))"
#cur.execute(create_database)

cur.execute(create_table1)

cur.execute(create_table2)

cur.execute(create_table3)

conn.autocommit=False
conn.close()