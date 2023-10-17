from .node import Node
from soffosai.core.services import LanguageDetectionService, inspect_arguments


class LanguageDetectionNode(Node):
    '''
    Language Detection configuration for Pipeline Use
    '''
    def __init__(self, name:str, text:str):
        source = inspect_arguments(self.__init__, name, text)
        service = LanguageDetectionService
        super().__init__(name, service, source)
