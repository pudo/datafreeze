import json
from datetime import datetime, date
from collections import defaultdict, OrderedDict
from decimal import Decimal

from six import PY3

from datafreeze.format.common import Serializer


class JSONEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj, (datetime, date)):
            return obj.isoformat()
        if isinstance(obj, Decimal):
            return str(obj)


class JSONSerializer(Serializer):

    def init(self):
        self.buckets = defaultdict(list)

    def write(self, path, result):
        self.buckets[path].append(result)

    def wrap(self, result):
        if self.mode == 'item':
            result = result[0]
        if self.export.get_bool('wrap', True):
            result = OrderedDict([
                ('count', len(result)),
                ('results', result),
            ])
            meta = self.export.get('meta', {})
            if meta is not None:
                result['meta'] = meta
        return result

    def close(self):
        for path, result in self.buckets.items():
            result = self.wrap(result)

            if self.fileobj is None:
                if PY3:  # pragma: no cover
                    fh = open(path, 'w', encoding='utf8')
                else:
                    fh = open(path, 'wb')
            else:
                fh = self.fileobj

            data = json.dumps(result,
                              cls=JSONEncoder,
                              indent=self.export.get_int('indent'))

            callback = self.export.get('callback')
            if callback:
                data = "%s && %s(%s);" % (callback, callback, data)

            if PY3:
                fh.write(bytes(data, encoding='utf8'))
            else:
                fh.write(data)
            if self.fileobj is None:
                fh.close()
