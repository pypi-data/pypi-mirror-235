from testcase.app.app_partial_rerun_merger import AppPartialRerunMerger
from worker.data.api import API
from worker.event.event_handler import EventHandler
from testcase.app.drilling_efficiency_app import DrillingEfficiency
from worker.mixins.logging import Logger
from worker.state import RedisHandler

redis_connection = None


def lambda_handler(event, context):
    """
    This function is the main entry point of the AWS Lambda function
    :param event: a scheduler or kafka event
    :param context: AWS Context
    :return:
    """
    global redis_connection
    redis_connection = RedisHandler.setup_existing_connection(redis_connection)

    app = DrillingEfficiency()

    merger = AppPartialRerunMerger(app, API(), context, Logger.get_logger())

    event_handler = EventHandler(app, merger)
    event_handler.process(event)
