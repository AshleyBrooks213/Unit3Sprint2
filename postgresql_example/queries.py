"""Holds my PosGreSQL example queries"""

# SQL Create Table Query
CREATE_TABLE_STATEMENT = """
CREATE TABLE test_table (
    id SERIAL PRIMARY KEY,
    name VARCHAR(40) NOT NULL,
    data JSONB
);
"""


#SQL Insert Values Query
INSERT_STATEMENT = """
    INSERT INTO test_table(name, data) VALUES
    (
        'A Row', 
        null
    ),
    (
        'Another Row, with Json',
        '{"a": 1, "b": ["leanves, "more leaves", "even more leaves"]}'::JSONB
    );
    """