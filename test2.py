import torch
from pytorch_pretrained_bert import BertTokenizer, BertModel, BertForMaskedLM
model = BertModel.from_pretrained('bert-base-uncased')
model.eval()