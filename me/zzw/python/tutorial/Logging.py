import logging
logging.warning('Something went wrong.')

logging.basicConfig(level=logging.WARNING)
logging.debug('Debug message')
logging.error('This is an error')

logging.basicConfig(level=logging.ERROR)
logging.debug('Debug message')
logging.info('Program started..')
logging.info('Loading files')
logging.error('This is an error')

logging.basicConfig(level=logging.WARNING)