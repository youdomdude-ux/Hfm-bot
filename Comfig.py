# ELITE V2.0 - CONFIG - Priority 1: Account Protection
ACCOUNT_BALANCE = 5.0
LOT_SIZE_PREFERRED = 0.01
RISK_MAX = 0.10
PROFIT_TARGET = 0.20

# 3. SYMBOLS -> Broker mapping + verification
SYMBOLS = {
    "GER40": {"yahoo":"^GDAXI", "contract":1, "tick_size":0.1, "tick_value":1, "min_vol":0.01, "max_vol":10, "spread_max":5.0},
    "USA500": {"yahoo":"^GSPC", "contract":1, "tick_size":0.1, "tick_value":1, "min_vol":0.01, "max_vol":10, "spread_max":3.0},
    "USA30": {"yahoo":"^DJI", "contract":1, "tick_size":0.1, "tick_value":1, "min_vol":0.01, "max_vol":10, "spread_max":4.0},
    "AUDUSD": {"yahoo":"AUDUSD=X", "contract":100000, "tick_size":0.00001, "tick_value":1, "min_vol":0.01, "max_vol":10, "spread_max":0.0003},
    "EURGBP": {"yahoo":"EURGBP=X", "contract":100000, "tick_size":0.00001, "tick_value":1, "min_vol":0.01, "max_vol":10, "spread_max":0.0003},
    "EURUSD": {"yahoo":"EURUSD=X", "contract":100000, "tick_size":0.00001, "tick_value":1, "min_vol":0.01, "max_vol":10, "spread_max":0.0002},
    "GBPUSD": {"yahoo":"GBPUSD=X", "contract":100000, "tick_size":0.00001, "tick_value":1, "min_vol":0.01, "max_vol":10, "spread_max":0.0003},
    "USDJPY": {"yahoo":"USDJPY=X", "contract":100000, "tick_size":0.001, "tick_value":1, "min_vol":0.01, "max_vol":10, "spread_max":0.03},
}

# 4-5. RSI + SMA
RSI_PERIOD=14
RSI_OB=70
RSI_OS=30
RSI_WAIT_CANDLES=3
SMA_SHORT=20
SMA_MID=50
SMA_LONG=200

# 10-11. RISK
MAX_POSITIONS=2
MAX_AGG_RISK=0.20
MAX_DAILY_LOSS=0.30
MAX_CONSEC_LOSSES=3

# 9. NEWS
NEWS_BLOCK_HOURS=[(7,10),(13,15)] # UTC London + NY high impact
PRE_NEWS=30
POST_NEWS=30

# 13. TP TIME
TP_WINDOWS=[5,16,30]
MIN_CONF=75
