'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Created at: 2023-06-26
Purpose: Easily use Simplify Service
-----------------------------------------------------
'''
from .service import SoffosAIService, inspect_arguments
from soffosai.common.constants import ServiceString


class SimplifyService(SoffosAIService):
    '''
    Paraphrase and Simplify are available as two different flavors of the same module. 
    While the Paraphrase module attempts to change the wording while keeping the same level of complexity, 
    the Simplify module outputs more commonly used words without altering the meaning of the original text. 
    '''

    def __init__(self,  **kwargs) -> None:
        service = ServiceString.SIMPLIFY
        super().__init__(service, **kwargs)
    

    def __call__(self, user:str, text:str):
        payload = inspect_arguments(self.__call__, user, text)
        return super().__call__(payload)
