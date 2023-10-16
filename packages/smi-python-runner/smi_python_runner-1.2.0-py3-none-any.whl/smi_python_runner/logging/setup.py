import logging


def logging_setup(application):
    # module_name = kwargs.get('module_name')
    # In Java : %d{yyyy-MM-dd HH:mm:ss.SSS} [${spring.flask-application.name}] [%thread] %-5level %logger{36} - %msg%n
    # logging_format = "%(asctime)s %(name)s %(levelname)s - %(message)s"
    logging_format = "%(asctime)s.%(msecs)03d [" \
                     + application.name \
                     + "] [%(threadName)s] %(levelname)s %(name)s - %(message)s"
    logging.basicConfig(
        # filename='example.log',
        # level=
        encoding='utf-8',
        level=logging.DEBUG,
        format=logging_format,
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    # logging.config.fileConfig('logging.conf')
    ''' From old Flask python-start-prohect
    logging.basicConfig(filename=application_properties.log.directory + application_properties.log.fileName, format=application_properties.log.format, level=application_properties.log.level)
    handler = RotatingFileHandler(filename=application_properties.log.directory + application_properties.log.fileName, maxBytes=application_properties.log.size, backupCount=1)
    log = logging.getLogger()
    log.addHandler(handler)
    '''
    return application
