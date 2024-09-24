class NodeBase:
    def __init__(self, editor, node):
        self.editor = editor
        self.node = node
        self._inputs = []
        self._outputs = []
        self._properties = []
        self._properties_dict = {}
        self._properties_order = []
        self._properties_order_dict