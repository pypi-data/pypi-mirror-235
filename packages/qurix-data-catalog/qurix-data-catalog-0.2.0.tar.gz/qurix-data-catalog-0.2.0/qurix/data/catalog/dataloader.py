import os
import re
import sqlite3
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any
from urllib.parse import quote, urlparse

import connectorx as cx  # type: ignore
import pandas as pd
from sqlalchemy import create_engine


class DataLoader(ABC):
    def __init__(self, catalog_source_location: str | Path):
        self._catalog_source_location = catalog_source_location
        self._unmasked_catalog_source_location = self.unmask_credentials(
            self._catalog_source_location)

    def unmask_credentials(self, connection_string: str) -> str:
        placeholders = re.findall(r'{(.*?)}', connection_string)
        connection_string_unmasked = connection_string
        for placeholder in placeholders:
            env_value = os.getenv(placeholder)
            if env_value:
                connection_string_unmasked = connection_string_unmasked.replace(
                    '{' + placeholder + '}', env_value)
        return connection_string_unmasked

    @abstractmethod
    def load(self, **kwargs: Any) -> pd.DataFrame:
        """Loads data from data source"""
        raise NotImplementedError


class PostgresDataLoader(DataLoader):
    def __init__(self, catalog_source_location: str | Path,
                 source_table: str,
                 source_schema: str):
        super().__init__(catalog_source_location=catalog_source_location)
        self._source_schema = source_schema
        self._source_table = source_table

    def load(self, **kwargs: Any) -> pd.DataFrame:
        # try:
        df = self._load(url=self._unmasked_catalog_source_location,
                        schema=self._source_schema,
                        table=self._source_table,
                        **kwargs)
        # except:
        #     df = self._load_sql_alchemy(url=self._catalog_source_location,
        #                                 schema=self._source_schema,
        #                                 table=self._source_table,
        #                                 **kwargs)
        return df

    def get_row_count(self, **kwargs: Any) -> int:
        # try:
        row_count = self._get_row_count(url=self._unmasked_catalog_source_location,
                                        schema=self._source_schema,
                                        table=self._source_table,
                                        **kwargs)

        # except Exception:
        # row_count = self._get_row_count_sql_alchemy(url=self._catalog_source_location,
        #                     schema=self._source_schema,
        #                     table=self._source_table,
        #                     **kwargs)
        return row_count

    # def load(self, **kwargs: Any) -> pd.DataFrame:
    #     df = self._load_sql_alchemy(url=self._catalog_source_location,
    #                                 schema=self._source_schema,
    #                                 table=self._source_table,
    #                                 **kwargs)
    #     return df

    @staticmethod
    def _load(url: str, schema: str, table: str, **kwargs) -> pd.DataFrame:
        """loads a dataframe from a SQL table into memory

        Args:
            url (str): In the form:
                "postgresql://{user}:{password}@{server}/{database}",
            schema (str): table schema
            table (str): table name

        Returns:
            pd.DataFrame: result of the SQL query
        """
        query = f"SELECT * FROM {schema}.{table} LIMIT 10"
        return cx.read_sql(url, query, **kwargs)

    @staticmethod
    def _load_sql_alchemy(url: str, schema: str, table: str, **kwargs) -> pd.DataFrame:
        """loads a dataframe from a SQL table into memory

        Args:
            url (str): In the form:
                "postgresql://{user}:{password}@{server}/{database}",
            schema (str): table schema
            table (str): table name

        Returns:
            pd.DataFrame: result of the SQL query
        """
        r = urlparse(url)
        # Define PostgreSQL database connection parameters
        db_params = {
            "dbname": r.path.replace("/", ""),
            "user": r.username,
            "password": r.password,
            "host": r.hostname,
            "port": r.port
        }
        # Encode the password to handle special characters
        encoded_password = quote(db_params["password"], safe="")

        # Create a SQLAlchemy engine
        engine = create_engine(
            f'postgresql+psycopg2://{db_params["user"]}:{encoded_password}@{db_params["host"]}:{db_params["port"]}/{db_params["dbname"]}')

        # Specify the SQL query to select data from the PostgreSQL table

        query = f"SELECT * FROM {schema}.{table} LIMIT 10"

        # Execute the SQL query and load data into a Pandas DataFrame
        try:
            df = pd.read_sql_query(query, engine)
        except Exception as e:
            print(f"Error executing SQL query: {e}")
            engine.dispose()
            exit(1)

        # Dispose of the SQLAlchemy engine
        engine.dispose()
        return df

    @staticmethod
    def _get_row_count(url: str, schema: str, table: str, **kwargs) -> int:
        """gets row count of a dataframe read as from a SQL table

        Args:
            url (str): In the form:
                "postgresql://{user}:{password}@{server}/{database}",
            schema (str): table schema
            table (str): table name

        Returns:
            pd.DataFrame: result of the SQL query
        """
        query = f"SELECT COUNT(*) FROM {schema}.{table}"
        result_df = cx.read_sql(url, query, **kwargs)
        return result_df.values[0][0]

    @staticmethod
    def _get_row_count_sql_alchemy(url: str, schema: str, table: str, **kwargs) -> int:
        """gets row count of a dataframe read as from a SQL table using sql alchemy

        Args:
            url (str): In the form:
                "postgresql://{user}:{password}@{server}/{database}",
            schema (str): table schema
            table (str): table name

        Returns:
            pd.DataFrame: result of the SQL query
        """
        r = urlparse(url)
        # Define PostgreSQL database connection parameters
        db_params = {
            "dbname": r.path.replace("/", ""),
            "user": r.username,
            "password": r.password,
            "host": r.hostname,
            "port": r.port
        }
        # Encode the password to handle special characters
        encoded_password = quote(db_params["password"], safe="")

        # Create a SQLAlchemy engine
        engine = create_engine(
            f'postgresql+psycopg2://{db_params["user"]}:{encoded_password}@{db_params["host"]}:{db_params["port"]}/{db_params["dbname"]}')

        # Specify the SQL query to select data from the PostgreSQL table

        query = f"SELECT COUNT(*) FROM {schema}.{table}"

        # Execute the SQL query and load data into a Pandas DataFrame
        try:
            df = pd.read_sql_query(query, engine)
        except Exception as e:
            print(f"Error executing SQL query: {e}")
            engine.dispose()
            exit(1)

        # Dispose of the SQLAlchemy engine
        engine.dispose()
        return df.values[0][0]

    def __str__(self):
        return "<PostgresDataLoader>"


class DB2DataLoader(DataLoader):
    def __init__(self, catalog_source_location: str | Path,
                 source_table: str,
                 source_schema: str):
        super().__init__(catalog_source_location=catalog_source_location)
        self._source_schema = source_schema
        self._source_table = source_table

    def load(self, **kwargs: Any) -> pd.DataFrame:
        df = self._load(url=self._catalog_source_location,
                        schema=self._source_schema,
                        table=self._source_table,
                        **kwargs)
        return df

    def get_row_count(self, **kwargs: Any) -> int:
        row_count = self._get_row_count(url=self._catalog_source_location,
                                        schema=self._source_schema,
                                        table=self._source_table,
                                        **kwargs)
        return row_count

    @staticmethod
    def _load(url: str, schema: str, table: str, **kwargs) -> pd.DataFrame:
        """loads a dataframe from a DB2 table into memory

        Args:
            url (str): In the form:
                "ibm_db_sa://user:password@host:port/database",
            schema(str): table schema
            table (str): table name

        Returns:
            pd.DataFrame: result of the SQL query
        """
        engine = create_engine(str(url))
        query = f"SELECT * FROM {schema}.{table} LIMIT 10"
        df = pd.read_sql(query, engine)
        engine.dispose()
        return df

    @staticmethod
    def _get_row_count(url: str, schema: str, table: str, **kwargs) -> int:
        """gets row count of a dataframe read as from a SQL table

        Args:
            url (str): In the form:
                "ibm_db_sa://user:password@host:port/database",
            schema(str): table schema
            table (str): table name

        Returns:
            int: row count of the dataframe read from the DB2 table
        """
        engine = create_engine(str(url))
        query = f"SELECT COUNT(*) FROM {schema}.{table}"
        df = pd.read_sql(query, engine)
        engine.dispose()
        return df.values[0][0]

    def __str__(self):
        return "<DB2DataLoader>"


class SQLiteDataLoader(DataLoader):
    def __init__(self, catalog_source_location: str | Path,
                 source_table: str):
        super().__init__(catalog_source_location=catalog_source_location)
        self._source_table = source_table

    def load(self, **kwargs: Any) -> pd.DataFrame:
        df = self._load(url=self._catalog_source_location,
                        table=self._source_table,
                        **kwargs)
        return df

    def get_row_count(self, **kwargs: Any) -> int:
        row_count = self._get_row_count(url=self._catalog_source_location,
                                        table=self._source_table,
                                        **kwargs)
        return row_count

    @staticmethod
    def _load(url: str, table: str, **kwargs) -> pd.DataFrame:
        """loads a dataframe from a SQL table into memory

        Args:
            url (str): In the form:
                "tests/resources/source_g.db",
            table (str): table name

        Returns:
            pd.DataFrame: result of the SQL query
        """
        conn = sqlite3.connect(url)
        query = f"SELECT * FROM {table}"
        df = pd.read_sql_query(query, conn)
        conn.close()
        return df

    @staticmethod
    def _get_row_count(url: str, table: str, **kwargs) -> int:
        """gets row count of a dataframe read as from a SQL table

        Args:
            url (str): In the form:
                "tests/resources/source_g.db",
            table (str): table name

        Returns:
            int: row count of the dataframe read from the SQLite table
        """
        conn = sqlite3.connect(url)
        query = f"SELECT COUNT(*) FROM {table}"
        df = pd.read_sql(query, conn)
        conn.close()
        return df.values[0][0]

    def __str__(self):
        return "<SQLiteDataLoader>"


class CsvDataLoader(DataLoader):
    def load(self, **kwargs: Any) -> pd.DataFrame:
        df = self._load(url=self._catalog_source_location,
                        **kwargs)
        return df

    def get_row_count(self, **kwargs: Any) -> int:
        row_count = self._get_row_count(url=self._catalog_source_location,
                                        **kwargs)
        return row_count

    @staticmethod
    def _load(url: str, **kwargs) -> pd.DataFrame:
        """loads a dataframe from a csv file into memory

        Args:
            url (str): In the form:
                "Folger/Subfolder/filename.csv"

        Returns:
            pd.DataFrame
        """
        return pd.read_csv(url, **kwargs)

    @staticmethod
    def _get_row_count(url: str, **kwargs) -> pd.DataFrame:
        """loads a dataframe from a csv file into memory

        Args:
            url (str): In the form:
                "Folger/Subfolder/filename.csv"

        Returns:
            pd.DataFrame
        """
        df = pd.read_csv(url, **kwargs)
        return df.shape[0]

    def __str__(self):
        return "<CsvDataLoader>"


class XlsxDataLoader(DataLoader):
    def load(self, **kwargs: Any) -> pd.DataFrame:
        return self._load(self._catalog_source_location, **kwargs)

    def get_row_count(self, **kwargs: Any) -> int:
        row_count = self._get_row_count(url=self._catalog_source_location,
                                        **kwargs)
        return row_count

    @staticmethod
    def _load(url: str, **kwargs) -> pd.DataFrame:
        """loads a dataframe from an xlsx file into memory

        Args:
            url (str): In the form:
                "Folger/Subfolder/filename.xlsx"

        Returns:
            pd.DataFrame
        """
        return pd.read_excel(url, **kwargs)

    @staticmethod
    def _get_row_count(url: str, **kwargs) -> pd.DataFrame:
        """loads a dataframe from a csv file into memory

        Args:
            url (str): In the form:
                "Folger/Subfolder/filename.xlsx"

        Returns:
            pd.DataFrame
        """
        df = pd.read_excel(url, **kwargs)
        return df.shape[0]

    def __str__(self):
        return "<XlsxDataLoader>"


class ParquetDataLoader(DataLoader):
    def load(self, **kwargs: Any) -> pd.DataFrame:
        return self._load(self._catalog_source_location, **kwargs)

    def get_row_count(self, **kwargs: Any) -> int:
        row_count = self._get_row_count(url=self._catalog_source_location,
                                        **kwargs)
        return row_count

    @staticmethod
    def _load(url: str, **kwargs) -> pd.DataFrame:
        """loads a dataframe from an xlsx file into memory

        Args:
            url (str): In the form:
                "Folger/Subfolder/filename.parquet"

        Returns:
            pd.DataFrame
        """
        return pd.read_parquet(url, **kwargs)

    @staticmethod
    def _get_row_count(url: str, **kwargs) -> pd.DataFrame:
        """loads a dataframe from a parquet file into memory

        Args:
            url (str): In the form:
                "Folger/Subfolder/filename.parquet"

        Returns:
            pd.DataFrame
        """
        df = pd.read_parquet(url, **kwargs)
        return df.shape[0]

    def __str__(self):
        return "<ParquetDataLoader>"
        return "<ParquetDataLoader>"
