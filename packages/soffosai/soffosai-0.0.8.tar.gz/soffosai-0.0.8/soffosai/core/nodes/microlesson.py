from .node import Node
from soffosai.core.services import MicrolessonService, inspect_arguments


class MicrolessonNode(Node):
    '''
    Microlesson Service configuration for Pipeline Use
    '''
    def __init__(self, name:str, content:list):
        source = inspect_arguments(self.__init__, name, content)
        service = MicrolessonService
        super().__init__(name, service, source)
