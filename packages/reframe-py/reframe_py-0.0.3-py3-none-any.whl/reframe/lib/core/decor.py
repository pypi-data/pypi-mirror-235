#!/usr/bin/env python

__authors__ = ["Peter W. Njenga"]
__copyright__ = "Copyright © 2023 ReframeAI, Inc."

# Standard Libraries
import json
import hashlib
from pprint import pformat
from os import environ as os_env
from datetime import datetime, timezone

# External Libraries
import openai
from loguru import logger

# Internal Libraries
from reframe.server.lib.db_session import meta_db, red_stream, red_cache

# Global Variables
openai.api_key = os_env.get('OPENAI_API_KEY')
CACHE_EXPIRATION_DURATION = 60 * 60 * 24 * 90 # 90 days

# ------------------------------

def with_cache(prefix, *args, **kwargs):

    def wrapper(func):

        async def wrapped(*args, **kwargs):
            arg_str = f"{args, kwargs}"

            cache_key = hashlib.sha256(str(arg_str).encode('utf-8')).hexdigest()

            cache_key = f"{prefix}::elem->{cache_key}"
            read_cache = kwargs.pop('read_cache', True)
            write_cache = kwargs.pop('write_cache', True)

            found_in_cache = False
            if read_cache:
                cache_val = red_cache.get(cache_key)

                if cache_val:
                    logger.opt(ansi=True).debug(f'Found element in cache - returning cached results. <green>{cache_val[:250]}...</green>')
                    try:
                        # Attempt to load the cache value as a json.
                        result_dict = json.loads(cache_val)
                        if 'result' not in result_dict:
                            raise Exception('Cache value is not a result dict')
                        found_in_cache = True
                        return result_dict['result']
                    except Exception as e:
                        logger.exception(e)
                else:
                    logger.debug(f'No cache found for key {cache_key}')

            if not found_in_cache:
                logger.debug('No cache found or skipping cache - running function')
                try:
                    start_time = datetime.now(timezone.utc)
                    _result = await func(*args, **kwargs)
                    end_time = datetime.now(timezone.utc)

                    # If success. The result is a dict with the result and status
                    result_dict = {
                        "result": _result,
                        "status": "SUCCESS",
                        "start_time": start_time,
                        "end_time": end_time,
                    }
                except Exception as e:
                    logger.exception(e)
                    # If error. The result is a dict with the error and status
                    result_dict = {
                        "payload": str(e),
                        "status": "ERROR",
                    }
                finally:
                    if write_cache:
                        red_cache.set(
                            cache_key,
                            json.dumps(result_dict, default=str),
                            ex=CACHE_EXPIRATION_DURATION
                        )

            return _result

        return wrapped

    return wrapper

