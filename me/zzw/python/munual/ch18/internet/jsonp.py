import json

print json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])

print json.dumps("\"foo\bar")

print json.dumps(u'\u1234')

print json.dumps('\\')

print json.dumps({"c": 0, "b": 0, "a": 0}, sort_keys=True)

from StringIO import StringIO
io = StringIO()
json.dump(['streaming API'], io)
print io.getvalue()

print json.dumps([1,2,3,{'4': 5, '6': 7}], separators=(',',':'))

print json.dumps({'4': 5, '6': 7}, sort_keys=True,
                  indent=4, separators=(',', ': '))

# decoding JSON
json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')
[u'foo', {u'bar': [u'baz', None, 1.0, 2]}]
json.loads('"\\"foo\\bar"')
io = StringIO('["streaming API"]')
json.load(io)

# Specializing JSON object decoding:
def as_complex(dct):
     if '__complex__' in dct:
         return complex(dct['real'], dct['imag'])
     return dct

json.loads('{"__complex__": true, "real": 1, "imag": 2}',
     object_hook=as_complex)

import decimal
json.loads('1.1', parse_float=decimal.Decimal)

# Extending JSONEncoder:


class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, complex):
            return [obj.real, obj.imag]
        # Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)

json.dumps(2 + 1j, cls=ComplexEncoder)
ComplexEncoder().encode(2 + 1j)
list(ComplexEncoder().iterencode(2 + 1j))
['[', '2.0', ', ', '1.0', ']']


obj = [[1,2,3],123,123.123,'abc',{'key1':(1,2,3),'key2':(4,5,6)}]
encodedjson = json.dumps(obj)
print repr(obj)
print encodedjson