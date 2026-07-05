from utils.schema_reader import SchemaReader

reader = SchemaReader()

schema = reader.read_schema()

print(schema)