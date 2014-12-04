import time
from datetime import datetime
import pytz

"""
    Convert unix timestamp (seconds since Jan 1, 1970, to ISO-8601 compatible
    UTC time string
"""    
def unixTimeToUTC(timestamp):
    utc = pytz.utc
    dtTime = datetime.fromtimestamp(timestamp, utc)
    iso_str = dtTime.isoformat()
    # isoformat returns a string like this:
    # '2014-10-30T04:25:21+00:00'
    # strip off the '+00:00' and replace
    # with 'Z' (both are ISO-8601 compatible)
    npos = iso_str.rfind('+')
    iso_z = iso_str[:npos] + 'Z'
    return iso_z