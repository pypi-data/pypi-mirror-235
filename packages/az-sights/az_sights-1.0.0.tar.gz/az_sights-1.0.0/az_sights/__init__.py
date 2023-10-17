"""
This module handles app insight queries
copyright: (c) 2023 by Kourosh Parsa.
"""
import os
import subprocess
from datetime import datetime
import calendar
import json
import logging

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


def execute(cmd):
    """
    returns output, err, returncode
    """
    ps = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                          stderr=subprocess.PIPE, universal_newlines=True)
    output, err = ps.communicate()
    return output, err, ps.returncode


def get_extensions():
    """
    returns a list of installed Azure extentions
    """
    cmd = 'az extension list'
    output, err, returncode = execute(cmd)
    if returncode != 0:
        raise Exception(err)

    res = json.loads(output)
    return [os.path.basename(data['path']) for data in res]


def install_extension(extension):
    """
    param extension: string, the name of the Azure extension
    It installs the given Azure extension
    """
    logger.info(f'Installing {extension}')
    cmd = f'az extension add --name {extension}'
    _, err, returncode = execute(cmd)
    if returncode != 0:
        raise Exception(err)


def check_extensions():
    extensions = get_extensions()
    for extension in ['application-insights']:
        if extension not in extensions:
            install_extension(extension)


def query_today(app_id, query):
    """
    :param app_id:
    :param query:
    :return: a dictionary
    """
    t = datetime.now()
    t = t.strftime("%Y-%M-%d")
    return query_app_insights(app_id, query, t, t)


def query_this_month(app_id, query):
    """
    :param app_id:
    :param query:
    :return: a dictionary
    """
    t1 = first_day_of_month()
    t2 = last_day_of_month()
    start_time = t1.strftime("%Y-%M-%d")
    end_time = t2.strftime("%Y-%M-%d")
    return query_app_insights(app_id, query, start_time, end_time)


def query_app_insights(app_id, query, start_time, end_time):
    """
    :param app_id:
    :param query:
    :param start_time: date or datetime,
    Format: date (yyyy-mm-dd) time (hh:mm:ss.xxxxx) timezone (+/-hh:mm).
    :param end_time:  date or datetime,
    Format: date (yyyy-mm-dd) time (hh:mm:ss.xxxxx) timezone (+/-hh:mm).
    :return: a dictionary
    """
    check_extensions()
    query = query.replace('"', '\'').strip()
    time_range = f'--start-time {start_time} --end-time {end_time}'
    cmd = f'az monitor app-insights query --app {app_id} {time_range} --analytics-query "{query}"'
    output, err, returncode = execute(cmd)
    if returncode != 0:
        raise Exception(err)

    try:
        res = json.loads(output)
    except Exception:
        raise Exception("Output is not in json format:\n" + output)
    
    try:
        res = convert_azure_table_to_dict(res)
    except Exception:
        pass
    return res


def convert_azure_table_to_dict(data):
    if isinstance(data, list):
        return data

    res = []
    try:
        for table in data['tables']:
            table_data = []
            columns = [col['name'] for col in table['columns']]
            for row in table['rows']:
                table_data.append(dict(zip(columns, row)))
            res.append(table_data)
        if len(res) == 1:
            return res[0]
    except Exception as ex:
        logger.warning('Failed to convert some azure result: %s', ex)
        return data
    return res


def first_day_of_month():
    return datetime.now().replace(day=1)


def last_day_of_month():
    today = datetime.now()
    last_day = calendar.monthrange(today.year, today.month)[1]
    return today.replace(day=last_day)
