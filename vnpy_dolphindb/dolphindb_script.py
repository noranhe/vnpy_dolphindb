
# dolphindb脚本，用于在dolphindb创建数据库和表
# 创建数据库
create_database = """
dataPath = "dfs://vnpy"
db = database(dataPath, VALUE, 2000.01M..2030.12M, engine=`TSDB)
"""

# 创建bar表
create_bar_table = """
db = database(dataPath)

bar_columns = ["symbol", "exchange", "datetime", "interval", "volume", "turnover", "open_interest", "open_price", "high_price", "low_price", "close_price"]
bar_type = [SYMBOL, SYMBOL, NANOTIMESTAMP, SYMBOL, DOUBLE, DOUBLE, DOUBLE, DOUBLE, DOUBLE, DOUBLE, DOUBLE]
bar = table(1:0, bar_columns, bar_type)

db.createPartitionedTable(
    bar,
    "bar",
    partitionColumns=["datetime"],
    sortColumns=["symbol", "exchange", "interval", "datetime"],
    keepDuplicates=LAST)
"""

# 创建tick表
create_tick_table = """
db = database(dataPath)

tick_columns = ["symbol", "exchange", "datetime", "name", "volume", "turnover", "open_interest", "last_price", "last_volume", "limit_up", "limit_down",
                "open_price", "high_price", "low_price", "pre_close", "interval",
                "bid_price_1", "bid_price_2", "bid_price_3", "bid_price_4", "bid_price_5",
                "ask_price_1", "ask_price_2", "ask_price_3", "ask_price_4", "ask_price_5",
                "bid_volume_1", "bid_volume_2", "bid_volume_3", "bid_volume_4", "bid_volume_5",
                "ask_volume_1", "ask_volume_2", "ask_volume_3", "ask_volume_4", "ask_volume_5", "localtime"]
tick_type = [SYMBOL, SYMBOL, NANOTIMESTAMP, SYMBOL, DOUBLE, DOUBLE, DOUBLE, DOUBLE, DOUBLE, DOUBLE, DOUBLE,
             DOUBLE, DOUBLE, DOUBLE, DOUBLE, SYMBOL,
             DOUBLE, DOUBLE, DOUBLE, DOUBLE, DOUBLE,
             DOUBLE, DOUBLE, DOUBLE, DOUBLE, DOUBLE,
             DOUBLE, DOUBLE, DOUBLE, DOUBLE, DOUBLE,
             DOUBLE, DOUBLE, DOUBLE, DOUBLE, DOUBLE, NANOTIMESTAMP]
tick = table(1:0, tick_columns, tick_type)

db.createPartitionedTable(
    tick,
    "tick",
    partitionColumns=["datetime"],
    sortColumns=["symbol", "exchange", "datetime"],
    keepDuplicates=LAST)
"""

# 创建overview表
create_overview_table = """
db = database(dataPath)

overview_columns = ["symbol", "exchange", "interval", "count", "start", "end", "datetime"]
overview_type = [SYMBOL, SYMBOL, SYMBOL, INT, NANOTIMESTAMP, NANOTIMESTAMP, NANOTIMESTAMP]
overview = table(1:0, overview_columns, overview_type)

db.createPartitionedTable(
    overview,
    "overview",
    partitionColumns=["datetime"],
    sortColumns=["symbol", "exchange", "interval", "datetime"],
    keepDuplicates=LAST)
"""
