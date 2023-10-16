from utils.config.addr_config import mysql_config, redis_config, hbase_config, kafka_config

mysql = Mysql = MysqlConfig = mysql_config = mysql_config.MysqlConfig
redis = Redis = RedisConfig = redis_config = redis_config.RedisConfig
kafka = Kafka = KafkaConfig = kafka_config = kafka_config.KafkaConfig
hbase = Hbase = HbaseConfig = hbase_config = hbase_config.HbaseConfig

__all__ = [
    "mysql",
    "Mysql",
    "MysqlConfig",
    "mysql_config",
    "redis",
    "Redis",
    "RedisConfig",
    "redis_config",
    "kafka",
    "Kafka",
    "KafkaConfig",
    "kafka_config",
    "hbase",
    "Hbase",
    "HbaseConfig",
    "hbase_config"
]
