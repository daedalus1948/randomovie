class Config():
    # shared configuration
    pass

class DevelopmentConfig(Config):
    # developoment configuration
    DEBUG = True

class ProductionConfig(Config):
    # production configuration
    DEBUG = False

app_config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
