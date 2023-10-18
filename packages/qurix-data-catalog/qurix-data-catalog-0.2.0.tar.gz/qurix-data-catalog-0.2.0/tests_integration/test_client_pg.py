from qurix.data.catalog.client import DataCatalogClient
from qurix.data.catalog.entities import CatalogDataSource
import pytest
# import subprocess


PG_PASS = "Welcome4$"
PG_USER = "pgsqldev"
PG_IMAGE = "postgres:latest"
PG_DB = "postgres"
CONTAINER_NAME = "postgressql"

# @pytest.fixture(autouse=True)
# def run_before_and_after_tests(tmpdir):
#     """Fixture to execute asserts before and after a test is run"""
#     # Setup: fill with any logic you want
#     subprocess.call("tests_integration/scripts/tearup_db.sh")
#     subprocess.call("tests_integration/scripts/prepare_sql.py")
#     # subprocess.run("tests_integration/scripts/tearup_db.sh")
#     # yield  # this is where the testing happens

#     # # Teardown : fill with any logic you want
#     # subprocess.run("tests_integration/scripts/teardown.sh")


@pytest.fixture
def empty_catalog_client() -> DataCatalogClient:
    return DataCatalogClient()


@pytest.fixture
def data_catalog_entry_postgres() -> CatalogDataSource:
    return CatalogDataSource(name="source f",
                             location="postgresql://pgsqldev:Welcome4$@localhost:5432/testdb",
                             business_partner="some partner",
                             table_schema="public",
                             table="dummy_data")


def test_1_1():
    assert 1 == 1


# def test_load_postgres(empty_catalog_client: DataCatalogClient, data_catalog_entry_postgres: CatalogDataSource):
#     subprocess.call("tests_integration/scripts/tearup_db.sh")
#     # subprocess.call("tests_integration/scripts/prepare_sql.py")
#     empty_catalog_client.add(dc_entry=data_catalog_entry_postgres,
#                              persist_data=True)
#     new_data_catalog = DataCatalogClient()
#     new_data_catalog.load_data()
#     result = new_data_catalog.describe_obj("source_f")
#     # print(result)
#     count_list = ([item for item in result["count"].to_list()])
#     expected_list = [10, 10, 10]
#     assert count_list == expected_list
#     subprocess.call("tests_integration/scripts/teardown_db.sh")
