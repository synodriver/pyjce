from pyjce import JceReader, JceStruct

# type tag length value


f = open('tests/datas', 'rb')
stream = JceReader(f.read())
s = JceStruct()
s.read_from(stream)
ff = open('datas.json', 'w', encoding="utf-8")
print(s.as_dict())
ff.write(s.as_json())
f.close()
ff.close()
