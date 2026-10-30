from datetime import datetime, timezone
import time
import hashlib
import random
import logging

class ISO8601Formatter(logging.Formatter):

  def formatTime(self, record, datefmt=None):
    dt = datetime.fromtimestamp(record.created, timezone.utc)
    return dt.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
formatter = ISO8601Formatter('%(asctime)s: %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


def main():
    x = random.randint(1, 1000)
    hash = hashlib.sha256(str(x).encode()).hexdigest()

    while True:
        now = datetime.now()
        timestamp = (
            datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + 'Z'
        )
        logger.info(hash)

        time.sleep(5)  

if __name__ == "__main__":
    main()