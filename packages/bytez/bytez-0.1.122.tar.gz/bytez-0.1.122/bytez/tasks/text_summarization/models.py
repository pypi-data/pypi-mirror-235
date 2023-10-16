from bytez.tasks.text_summarization._models.hhousen_docsum import HhousenDocsumModel
from bytez.tasks.text_summarization._models.dmmiller612_bert_extractive_summarizer import Dmmiller612BertExtractiveSummarizerModel
from dataclasses import dataclass
from bytez.tasks.text_summarization._models.chriskhanhtran_bert_extractive_summarization import ChriskhanhtranBertExtractiveSummarizationModel


@dataclass
class TextSummarizationModels:
    chriskhanhtran_bert_extractive_summarization = ChriskhanhtranBertExtractiveSummarizationModel().inference
    
    dmmiller612_bert_extractive_summarizer = Dmmiller612BertExtractiveSummarizerModel().inference
    hhousen_docsum = HhousenDocsumModel()