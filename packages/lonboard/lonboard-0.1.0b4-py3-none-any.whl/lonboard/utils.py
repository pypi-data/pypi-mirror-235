import pyarrow as pa

from lonboard.constants import EXTENSION_NAME

GEOARROW_EXTENSION_TYPE_NAMES = {e.value for e in EXTENSION_NAME}


def get_geometry_column_index(schema: pa.Schema) -> int:
    """Get the positional index of the geometry column in a pyarrow Schema"""
    for field_idx in range(len(schema)):
        field_metadata = schema.field(field_idx).metadata
        if (
            field_metadata
            and field_metadata.get(b"ARROW:extension:name")
            in GEOARROW_EXTENSION_TYPE_NAMES
        ):
            return field_idx

    raise ValueError("No geometry column in table schema.")


def get_num_coordinates(table: pa.Table) -> int:
    """Get the total number of coordinates in a table"""
    geom_col_idx = get_geometry_column_index(table.schema)
    geom_col = table.column(geom_col_idx)
    extension_type_name = table.schema.field(geom_col_idx).metadata[
        b"ARROW:extension:name"
    ]

    if extension_type_name == EXTENSION_NAME.POINT:
        return len(geom_col)

    if extension_type_name in [EXTENSION_NAME.LINESTRING, EXTENSION_NAME.MULTIPOINT]:
        return sum([len(chunk.flatten()) for chunk in geom_col.chunks])

    if extension_type_name in [EXTENSION_NAME.POLYGON, EXTENSION_NAME.MULTILINESTRING]:
        return sum([len(chunk.flatten().flatten()) for chunk in geom_col.chunks])

    if extension_type_name == EXTENSION_NAME.MULTIPOLYGON:
        return sum(
            [len(chunk.flatten().flatten().flatten()) for chunk in geom_col.chunks]
        )

    assert False
