from worker.partial_rerun_merge.merge import PartialRerunMerge
from worker.partial_rerun_merge.models import CollectionMergingModel, MergingSchemaModel


collections = [
    {
        "collection_name": "drilling-efficiency.mse"
    }
]

collections = [
    CollectionMergingModel(**collection)
    for collection in collections
]


SCHEMA = MergingSchemaModel(
    collections=collections,
    modules=None
)


class AppPartialRerunMerger(PartialRerunMerge):
    def __init__(self, app, api, context, logger):
        schema = SCHEMA
        schema.modules = app.get_active_modules()
        super().__init__(schema, api, context, logger)
