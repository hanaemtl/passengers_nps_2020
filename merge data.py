def get_rs_data(query):
    import pandas as pd
    from super_mario.config import Databases
    print(Databases.REDSHIFT_DBNAME)
    print(Databases.REDSHIFT_USER)

    from super_mario.db_connection import DBConnection


    REDSHIFT = DBConnection(host=Databases.REDSHIFT_HOST,
                                port=Databases.REDSHIFT_PORT,
                                db_name=Databases.REDSHIFT_DBNAME,
                                user=Databases.REDSHIFT_USER,
                                password=Databases.REDSHIFT_PASSWORD,
                                timeout_sec=3600 )  # defaoult timeout is set to 5 minutes
    REDSHIFT.excluded_suffixes
    REDSHIFT.get_schemas()
    REDSHIFT.get_tables_list(schema="backend", exclude_not_relevant=True)
    REDSHIFT.get_views_list(schema="data")
    REDSHIFT.get_columns(schema="backend", table_name="rides", exclude_not_relevant=True)
    REDSHIFT.get_unique_values_of_column(schema="backend", table_name="rides", column_name="state")

    df = REDSHIFT.get_custom_query(query)
    return df
