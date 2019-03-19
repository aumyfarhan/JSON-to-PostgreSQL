import json
import psycopg2
import pandas as pd
import os
import fnmatch

conn = psycopg2.connect\
("host=localhost dbname=tweet_text user=postgres password=tmobile91")

cur=conn.cursor()

print ('start')

count=0

conn.autocommit=False

def find_files(directory, pattern):
    for root, dirs, files in os.walk(directory):	
        for basename in files:
            if fnmatch.fnmatch(basename, pattern):
                filename = os.path.join(root, basename)
                yield filename


pattern = "[0-9]*.txt"            
tweet_file_path=r'''G:\election_data'''
cc=0
for filename in find_files(tweet_file_path,pattern):
    print(filename)
    cur_file = open(filename,'r')
    try:    
       for line in cur_file:
           cc=cc+1
           if (len(line)>1000):
               try:
                   cur_object=json.loads(line)
                   if 'id' in cur_object.keys():
                       uuid=cur_object['user']['id']
                       if uuid in all_cm_user:
                           
                           tweet_id=cur_object['id']
                           tweet_text=cur_object['text']
                           user_id=cur_object['user']['id']
                           tweet_lang=cur_object['lang']
                           tweet_time=str(pd.to_datetime(cur_object['created_at']))
                           

                           tweet_client_name=cur_object['source']
                           is_retweet=cur_object['retweeted']
                           hashtags=[hashtag['text'] for hashtag in cur_object['entities']['hashtags']]
                           urls=[url['url'] for url in cur_object['entities']['urls']]
                           user_mentions=[user_mentions['id'] for user_mentions in cur_object['entities']['user_mentions']]

                          
                           user_display_name=cur_object['user']['name']
                           user_screen_name=cur_object['user']['screen_name']
                           user_reported_location=cur_object['user']['location']
                           user_pro_des=cur_object['user']['description']
                           user_pro_url=cur_object['user']['url']
                           follower_count=cur_object['user']['followers_count']
                           following_count=cur_object['user']['friends_count']
                           statuses_count=cur_object['user']['statuses_count']
                           favorited_count=cur_object['user']['favourites_count']
                           account_creation_date=str(pd.to_datetime(cur_object['user']['created_at']))
                           account_lang=cur_object['user']['lang']
                           
                           cur.execute("INSERT INTO prgd_elec_tweet_text(tweet_id,user_id,tweet_lang,tweet_text,tweet_time,\
                                                                        tweet_client_name,is_retweet,hashtags,urls, user_mentions)\
                                                                       values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT(tweet_id) DO NOTHING"\
                                                                       ,(tweet_id,user_id,tweet_lang,tweet_text,tweet_time,\
                                                                        tweet_client_name,is_retweet,hashtags,urls, user_mentions))
                           
                           
                           
                           
                           
                           cur.execute("INSERT INTO prgd_elec_user(user_id,user_display_name, user_screen_name,\
                                                                  user_reported_location,user_pro_des,user_pro_url,\
                                                                  follower_count,following_count,statuses_count,\
                                                                  favorited_count,account_creation_date,account_lang)\
                                                                  values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON CONFLICT(user_id) DO NOTHING"\
                                                                  ,(user_id,user_display_name, user_screen_name,\
                                                                    user_reported_location,user_pro_des,user_pro_url,\
                                                                    follower_count,following_count,statuses_count,\
                                                                    favorited_count,account_creation_date,account_lang))
                           
                           
                           conn.commit()
                           
                           print('\n commit \n')
                       
                   else:
                       print('error id')
                           
               except Exception as b: print(b)
       
    except Exception as e: print(e)
        
                      
conn.close()


                                        