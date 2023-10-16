
from dftools.core.structure.core import StructureCatalog, FieldCatalog, Field

class StructureCatalogApi :

    def __init__(self) -> None:
        pass

    def update_structure_catalog_with_known_field_standard_definitions(
        str_catalog : StructureCatalog
        , field_standard_def_catalog : FieldCatalog
        , desc_override : bool = False
        , characterisation_append : bool = True
        , data_format_override : bool = True
        , default_value_override : bool = True
        ) -> StructureCatalog:
        for namespace in str_catalog.get_namespaces():
            if field_standard_def_catalog.has_namespace(namespace):
                structure_dict = str_catalog.get_structures(namespace)
                for structure in structure_dict.values():
                    for field in structure.fields:
                        if field_standard_def_catalog.has_field(namespace, field.name):
                            StructureCatalogApi.update_field_from_ref_field(field = field
                                , field_ref = field_standard_def_catalog.get_field(namespace, field.name)
                                , desc_override=desc_override, characterisation_append=characterisation_append
                                , data_format_override=data_format_override, default_value_override=default_value_override
                            )
        return str_catalog

    def update_field_from_ref_field(
        field : Field
        , field_ref : Field
        , desc_override : bool = False
        , characterisation_append : bool = True
        , data_format_override : bool = True
        , default_value_override : bool = True
        ) -> Field:
        
        # Description override
        if desc_override :
            if field_ref.desc != field.desc:
                field.desc = field_ref.desc
        # Characterisation appending
        if characterisation_append : 
            for char_name in field_ref.get_characterisation_names():
                if not field.has_characterisation(char_name):
                    field.add_characterisation(field_ref.get_characterisation(char_name))
        # Data Format override
        if data_format_override :
            if field_ref.data_type != field.data_type :
                field.data_type = field_ref.data_type
            if field_ref.length != field.length :
                field.length = field_ref.length
            if field_ref.precision != field.precision :
                field.precision = field_ref.precision
        # Default Value override
        if default_value_override :
            if field_ref.default_value != field.default_value :
                field.default_value = field_ref.default_value

        return field