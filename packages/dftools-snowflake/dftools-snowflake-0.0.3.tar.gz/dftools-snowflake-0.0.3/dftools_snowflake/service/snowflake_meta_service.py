
from dftools.core.database import DatabaseMetadataService
from dftools_snowflake.util.snowflake_system_queries import (
    get_snow_structure_query_for_namespace
    , get_snow_structure_query_for_catalog_and_namespace
    , get_snow_structure_query_for_namespace_and_table
    , get_snow_structure_query_for_catalog_namespace_and_table
)
from dftools_snowflake.connection import SnowflakeConnectionWrapper
from dftools_snowflake.service.meta_decoder import SnowStructureDecoder

class SnowMetadataService(DatabaseMetadataService):

    def __init__(self, connection_wrapper: SnowflakeConnectionWrapper) -> None:
        super().__init__(connection_wrapper, SnowStructureDecoder())

    def get_structure_from_database(self, namespace : str, table_name : str, catalog : str = None) -> list:
        data_structure_extract_query = get_snow_structure_query_for_namespace_and_table(namespace=namespace, table_name=table_name) \
            if catalog is None else get_snow_structure_query_for_catalog_namespace_and_table(catalog=catalog, namespace=namespace, table_name=table_name)
        query_list = [("SHOW PRIMARY KEYS;", )
            , ("CREATE OR REPLACE TEMPORARY TABLE DATA_STRUCTURE_PRIMARY_KEYS_{session_id} AS SELECT * FROM TABLE(RESULT_SCAN('{last_query_exec_result.query_id}'));", )
            , (data_structure_extract_query.replace('DATA_STRUCTURE_PRIMARY_KEYS', 'DATA_STRUCTURE_PRIMARY_KEYS_{session_id}'), )
            ]
        query_exec_results = self.conn_wrap.execute_queries(query_list=query_list)
        if query_exec_results.has_failed():
            raise RuntimeError('Failure on structures metadata retrieval.')
        return query_exec_results[2].result_set

    def get_structures_from_database(self, namespace : str, catalog : str = None) -> list:
        structure_names_to_exclude = ['DATA_STRUCTURE_PRIMARY_KEYS']
        data_structure_extract_query = get_snow_structure_query_for_namespace(namespace=namespace, structure_names_to_exclude=structure_names_to_exclude) \
            if catalog is None \
            else get_snow_structure_query_for_catalog_and_namespace(catalog=catalog, namespace=namespace, structure_names_to_exclude=structure_names_to_exclude)
        query_list = [("SHOW PRIMARY KEYS;", )
            , ("CREATE OR REPLACE TEMPORARY TABLE DATA_STRUCTURE_PRIMARY_KEYS_{session_id} AS SELECT * FROM TABLE(RESULT_SCAN('{last_query_exec_result.query_id}'));", )
            , (data_structure_extract_query.replace('DATA_STRUCTURE_PRIMARY_KEYS', 'DATA_STRUCTURE_PRIMARY_KEYS_{session_id}'), )
            ]
        query_exec_results = self.conn_wrap.execute_queries(query_list=query_list)
        if query_exec_results.has_failed():
            raise RuntimeError('Failure on structures metadata retrieval.')
        return query_exec_results[2].result_set