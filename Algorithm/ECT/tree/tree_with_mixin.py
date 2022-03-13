
class ToDictMixin(object):
    def to_dict(self):
        return self._traverse_dict(self.__dict__)
    
    def _traverse_dict(self, instance_dict):
        output = {}
        for key, value in instance_dict.items():
            output[key] = self._traverse(key, value)
        return output

    def _traverse(self, key, value):
        if isinstance(value, ToDictMixin):
            return value.to_dict()
        elif isinstance(value, dict):
            return self._traverse_dict(value)
        elif isinstance(value, list):
            return [self._traverse(key, i) for i in value]
        elif hasattr(value, '__dict__'):
            return self._traverse_dict(value.__dict__)
        else:
            return value

class AnyNode(ToDictMixin, object):

    def __init__(self, parent=None, children=None, **kwargs):
        self.__dict__.update(kwargs)
        self.parent = parent
        if children:
            self.children = children

root = AnyNode(id="root")
s0 = AnyNode(id="sub0", parent=root)
s0b = AnyNode(id="sub0B", parent=s0, foo=4, bar=109)
s0a = AnyNode(id="sub0A", parent=s0)
s1 = AnyNode(id="sub1", parent=root)
s1a = AnyNode(id="sub1A", parent=s1)
s1b = AnyNode(id="sub1B", parent=s1, bar=8)
s1c = AnyNode(id="sub1C", parent=s1)
s1ca = AnyNode(id="sub1Ca", parent=s1c)

print(root.to_dict())
print(s0.to_dict())
print(s0b.to_dict())
print(s1ca.to_dict())

root = AnyNode(id="root", children=[
        AnyNode(id="sub0", children=[
            AnyNode(id="sub0B", foo=4, bar=109),
            AnyNode(id="sub0A"),
        ]),
        AnyNode(id="sub1", children=[
            AnyNode(id="sub1A"),
            AnyNode(id="sub1B", bar=8),
            AnyNode(id="sub1C", children=[
                AnyNode(id="sub1Ca"),
        ]),
    ]),
])
print(root.to_dict())
