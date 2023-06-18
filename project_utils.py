import logging
import uuid
from models.utils import coll_generator
from bson.objectid import ObjectId


def setup_logging(log_file):
    """Configure logging settings"""
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(levelname)s] %(message)s', handlers=[
            logging.StreamHandler(), logging.FileHandler(log_file)])
    return logging.getLogger()  # Return the root logger


# Usage example:
log = setup_logging('current_log')
# log.debug('This is a debug message')
# log.info('This is an info message')
# log.warning('This is a warning message')
# log.error('This is an error message')
# log.critical('This is a critical message')


def get_uid():
    return str(uuid.uuid4()).replace('-', '')


def get_user_id():
    doc = coll_generator.find_one({"_id": ObjectId("648eaaa4c8b5ad3279ddaadb")})
    last_user_id = doc["user_id"] if doc else 0
    new_user_id = last_user_id + 1
    coll_generator.update_one(
        {"_id": ObjectId("648eaaa4c8b5ad3279ddaadb")},
        {"$set": {"user_id": new_user_id}},
        upsert=True)
    return new_user_id




