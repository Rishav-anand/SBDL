import pytest
from datetime import datetime, date
from pyspark.sql.types import StructType, StructField, StringType, NullType, TimestampType, ArrayType, DateType, Row

from lib import DataLoader
from lib.ConfigLoader import get_config
from lib.Utils import get_spark_session


@pytest.fixture(scope='session')
def spark():
    return get_spark_session("LOCAL")


def test_get_config():
    conf_local = get_config("LOCAL")
    conf_qa = get_config("QA")
    assert conf_local["kafka.topic"] == "sbdl_kafka_cloud"
    assert conf_qa["hive.database"] == "sbdl_db_qa"

def test_read_accounts(spark):
    accounts_df = DataLoader.read_accounts(spark, "LOCAL", False, None)
    assert accounts_df.count() == 8
