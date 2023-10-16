import json
from typing import List, Tuple

from dftools.core.database.connection_wrapper import ConnectionWrapper
from dftools.core.structure import BaseStructureDecoder, Structure, StructureCatalog, StructureCatalogCsv

class DatabaseMetadataService():
    """
        Database Metadata Service interface
        
        All database implementation should implement this interface
    """

    def __init__(self, connection_wrapper : ConnectionWrapper, decoder : BaseStructureDecoder) -> None:
        self.conn_wrap = connection_wrapper
        self.decoder = decoder
    
    def decode_specific_structure_result_set(self, result_set : list) -> StructureCatalog:
        """
            Decode the specific structure result set to a structure catalog

            Parameters
            -----------
                result_set : list
                    The list of rows from a metadata result set

            Returns
            -----------
                structure_catalog : StructureCatalog
                    The structure catalog
            
        """
        structure_catalog = StructureCatalog()
        for row in result_set:
            cur_data = row[0]
            structure_meta = json.loads(cur_data)
            namespace, structure = self.decoder.decode_json(structure_meta)
            structure_catalog.add_structure(namespace=namespace, structure=structure)
        return structure_catalog
                
    def get_structure_from_database(self, namespace : str, table_name : str, catalog : str = None) -> list:
        """
            Get a structure from the database using the local connection wrapper

            Parameters
            -----------
                namespace : str
                    The namespace name (also named schema)
                table_name : str
                    The table name
                catalog : str, optional
                    The catalog name

            Returns
            -----------
                data_structure_result_set : a result set of the data structure dictionnary
            
        """
        return NotImplementedError('The get_structure_from_database method is not implemented')

    def get_standard_structure_from_database(self
            , namespace : str
            , table_name : str
            , catalog : str = None
            , output_file_path : str = None) -> StructureCatalog:
        """
            Get a standard structure from the database using the local connection wrapper

            Parameters
            -----------
                namespace : str
                    The namespace name (also named schema)
                table_name : str
                    The table name
                catalog : str, optional
                    The catalog name
                output_file_path : str, optional
                    The output file path, if a csv file to be generated

            Returns
            -----------
                structure_catalog : StructureCatalog
                    The structure catalog
        """
        current_namespace = namespace if namespace is not None else self.conn_wrap.get_current_namespace()
        structure_catalog = self.decode_specific_structure_result_set(self.get_structure_from_database(current_namespace, table_name))
        if output_file_path is not None:
            StructureCatalogCsv.to_csv(output_file_path, structure_catalog)
        return structure_catalog

    def get_structures_from_database(self, namespace : str, catalog : str = None) -> list:
        """
            Get a structure from the database using the local connection wrapper

            Parameters
            -----------
                namespace : str
                    The namespace name (also named schema)
                catalog : str
                    The catalog name

            Returns
            -----------
                data_structure_result_set : a result set of the data structure dictionnary
            
        """
        return NotImplementedError('The get_structures_from_database method is not implemented')

    def get_standard_structures_from_database(self
            , namespace : str
            , catalog : str = None
            , output_file_path : str = None) -> StructureCatalog:
        """
            Get a standard structure from the database using the local connection wrapper

            Parameters
            -----------
                namespace : str
                    The namespace name (also named schema)
                catalog : str, optional
                    The catalog name
                output_file_path : str, optional
                    The output file path, if a csv file to be generated

            Returns
            -----------
                structure_catalog : StructureCatalog
                    The structure catalog
        """
        current_namespace = namespace if namespace is not None else self.conn_wrap.get_current_namespace()
        structure_catalog = self.decode_specific_structure_result_set(self.get_structures_from_database(namespace=current_namespace, catalog=catalog))
        if output_file_path is not None:
            StructureCatalogCsv.to_csv(output_file_path, structure_catalog)
        return structure_catalog