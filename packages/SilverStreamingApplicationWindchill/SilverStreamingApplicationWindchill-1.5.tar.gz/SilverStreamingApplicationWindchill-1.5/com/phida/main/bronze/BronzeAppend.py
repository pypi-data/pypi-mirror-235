

class BronzeAppend:
    """
    A streaming pipeline for cleansing incremental data from Raw file and append into Bronze

    args:
        srcFilePath: String - Source File (Raw Data File)
        tgtDatabaseName: String - Target Database Name (Will be created if not exists)
        tgtTableName: String - Target Table Name (Will be created if not exists)
        tgtTablePath: String - Target Table Path (so that the table is created as external)
        tgtTableKeyColumns: String - Column names separated by comma to help identify the primary key for the target table
        tgtPartitionColumns: String - Target partition columns (optional)
        triggerOnce: String - Whether continuous streaming or just once

    methods:
        bronzeCleansing
        prepareTarget

    example:
        from com.phida.main.bronze.BronzeAppend import BronzeAppend
        bronzeAppendObj = BronzeAppend(srcFilePath, tgtDatabaseName, tgtTableName,
                                        tgtTablePath, tgtTableKeyColumns, tgtPartitionColumns, triggerOnce)

    """