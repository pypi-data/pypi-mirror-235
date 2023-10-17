from logclshelper import LogClsHelper
from pyspark.sql import SparkSession

class PySparkHelper(LogClsHelper):
    _spark = None
    
    @classmethod
    def get_or_create_spark(cls):
        cls.logger().debug(f'#beg# get_or_create_spark')
        
        if(cls._spark is None):
            cls._spark = SparkSession.builder.enableHiveSupport().getOrCreate()
            
        cls.logger().debug(f'#end# get_or_create_spark {cls._spark}')
        
        return cls._spark
    
    @classmethod
    def stop_spark(cls):
        cls.logger().debug(f'#beg# stop_spark {cls._spark}')
        
        if(cls._spark is not None):
            cls._spark.stop()
            cls._spark = None
            
        cls.logger().debug(f'#end# stop_spark {cls._spark}')
            
    @classmethod
    def clear_spark_cache(cls):
        cls.logger().debug(f'#beg# clear_spark_cache')
        
        cls.get_or_create_spark().catalog.clearCache()
        
        cls.logger().debug(f'#end# clear_spark_cache')



