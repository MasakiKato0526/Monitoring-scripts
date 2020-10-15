#
#  Monitor Azure Cache for Redis by 10 sec
#
import redis
import time
import datetime
from logging import basicConfig, getLogger, DEBUG, INFO
from logging.handlers import TimedRotatingFileHandler

# Define log format like "2020-10-15 00:01:30,839 INFO    : OK"
# Log is rotated at midnight
basicConfig(
    level = INFO,
    format = '%(asctime)s %(levelname)-8s: %(message)s',
    handlers = [TimedRotatingFileHandler('log/redisaccess.log', when = 'MIDNIGHT')]
)

logger = getLogger(__name__)

# Define Redis access setting
redis_host = '<Redis host name>'
redis_key = '<Redis key>'
redis_port = <Redis port>
db_number = <Redis db number>

# Define Redis client
client = redis.StrictRedis(host=redis_host, port=redis_port, db=db_number, password=redis_key, ssl=True)

# Start monitoring REdis
while True:
    logger.debug('Start monitoring')
    
    try:
        cache_result = client.get('test').decode('utf-8')
        logger.debug('cache: ' + cache_result)
    
        if cache_result != 'OK':
            client.set('test', 'OK')
            logger.warning('Reset cache') 

            time.sleep(10)
        else:
            logger.info(cache_result)
                
            time.sleep(10)
    except Exception as e:
        logger.error(e)
