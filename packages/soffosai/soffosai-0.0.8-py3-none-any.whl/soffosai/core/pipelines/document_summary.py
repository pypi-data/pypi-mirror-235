'''
Copyright (c)2022 - Soffos.ai - All rights reserved
Created at: 2023-06-30
Purpose: Define the standard Pipeline for converting, summarizing an ingested document
-----------------------------------------------------
'''
from soffosai.core import inspect_arguments
from soffosai.core.nodes import DocumentsSearchNode, SummarizationNode
from soffosai.core.pipelines import Pipeline


def get_text_from_passages(passages):
    text = ""
    for passage in passages:
        text = text + passage['content']
    return text


class DocumentSummaryPipeline(Pipeline):
    '''
    A Soffos Pipeline that takes document_ids, then summarizes the content.
    The output is a list containing the output object of file converter and summarization.
    '''
    def __init__(self, **kwargs) -> None:
        document_search_node = DocumentsSearchNode(
            name = "doc_search",
            document_ids= {"source": "user_input", "field": "document_ids"}
        )
        
        summarization_node = SummarizationNode(
            name = "summarization",
            text = {"source": "doc_search", "field": "passages", "pre_process": get_text_from_passages},
            sent_length = {"source": "user_input", "field": "sent_length"}
        )

        nodes = [document_search_node, summarization_node]
        use_defaults = False
        super().__init__(nodes=nodes, use_defaults=use_defaults, **kwargs)


    def __call__(self, user, document_ids, sent_length):
        user_input = inspect_arguments(self.__call__, user, document_ids, sent_length)
        return super().__call__(user_input)
