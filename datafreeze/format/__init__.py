from datafreeze.format.fjson import JSONSerializer
from datafreeze.format.fcsv import CSVSerializer
from datafreeze.format.ftabson import TabsonSerializer

SERIALIZERS = {
    'json': JSONSerializer,
    'csv': CSVSerializer,
    'tabson': TabsonSerializer
    }


def get_serializer(config):
    serializer = config.get_normalized('format', 'json')
    return SERIALIZERS.get(serializer)
