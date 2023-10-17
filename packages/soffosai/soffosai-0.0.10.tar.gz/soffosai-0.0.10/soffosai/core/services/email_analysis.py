'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Created at: 2023-06-26
Purpose: Easily use Email Analysis Service
-----------------------------------------------------
'''
from .service import SoffosAIService, inspect_arguments
from soffosai.common.constants import ServiceString


class EmailAnalysisService(SoffosAIService):
    '''
    This module extracts key information from the body of an e-mail.
    '''

    def __init__(self,  **kwargs) -> None:
        service = ServiceString.EMAIL_ANALYSIS
        super().__init__(service, **kwargs)
    
    def __call__(self, user:str, text:str):
        payload = inspect_arguments(self.__call__, user, text)
        return super().__call__(payload)
