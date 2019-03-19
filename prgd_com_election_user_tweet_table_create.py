import psycopg2


conn = psycopg2.connect\
("host=localhost dbname=tweet_text user=postgres password=tmobile91")

cur=conn.cursor()
conn.autocommit=True

ct_st1='''CREATE TABLE  prgd_elec_tweet_text (tweet_id BIGINT PRIMARY KEY,\
                                            user_id BIGINT,\
                                            tweet_lang TEXT,\
                                            tweet_text TEXT,\
                                            tweet_time TIMESTAMP,\
                                            tweet_client_name TEXT,\
                                            is_retweet BOOLEAN,\
                                            hashtags TEXT,\
                                            urls TEXT,\
                                            user_mentions TEXT)'''



ct_st2='''CREATE TABLE prgd_elec_user (user_id BIGINT PRIMARY KEY,\
                                      user_display_name TEXT,\
                                      user_screen_name text,\
                                      user_reported_location TEXT,\
                                      user_pro_des TEXT,\
                                      user_pro_url TEXT,\
                                      follower_count INT,\
                                      following_count INT,\
                                      statuses_count INT,\
                                      favorited_count INT,\
                                      account_creation_date TIMESTAMP,\
                                      account_lang TEXT)'''


cur.execute(ct_st1)

cur.execute(ct_st2)

conn.autocommit=False
conn.close()

