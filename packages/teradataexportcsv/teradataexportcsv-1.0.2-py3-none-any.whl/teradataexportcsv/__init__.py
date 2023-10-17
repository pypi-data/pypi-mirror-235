# Copyright 2023 by Teradata Corporation. All rights reserved.

import teradatasql

def export (sTableName, sFileName, **kwargs):
    with teradatasql.connect (**kwargs) as con:
        with con.cursor () as cur:
            cur.execute ("{fn teradata_try_fastexport}{fn teradata_write_csv(" + sFileName + ")}select * from " + sTableName)
