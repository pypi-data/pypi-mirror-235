import math
import numpy as np
from sentence_transformers import SentenceTransformer
from typing import List, Union
from tqdm import tqdm

from torchness.base_elements import TorchnessException
from torchness.motorch import MOTorch, Module


# Text Embedding Module, based on Sentence-Transformer, prepares embedding for given text (str)
class TextEMB(Module):

    def __init__(
            self,
            st_name: str=   'all-MiniLM-L6-v2',
            enc_batch_size= 256,
            **kwargs):
        Module.__init__(self, **kwargs)
        self.st_name = st_name
        self.st_model = SentenceTransformer(model_name_or_path=st_name)
        self.enc_batch_size = enc_batch_size
        self.logger.info(f'*** TextEMB : {self.st_name} *** initialized, feats width:{self.width} seq length:{self.length}')

    def tokenize(self, texts:List[str]) -> List[List[str]]:
        tokenizer = self.st_model.tokenizer
        return [tokenizer.tokenize(t) for t in texts]

    # original, wrapped version
    def encode(
            self,
            texts: List[str],
            show_progress_bar=  True,
            device=             None,
    ) -> np.ndarray:
        return self.st_model.encode(
            sentences=          texts,
            batch_size=         self.enc_batch_size,
            show_progress_bar=  show_progress_bar,
            device=             device)
    """
    # extracted essence, not working for cuda
    def encode(
            self,
            texts: List[str],
            device=             None,
            show_progress_bar=  True,
    ) -> torch.Tensor:

        # texts should be split in batches
        features = self.st_model.tokenize(texts)
        with torch.no_grad():
            out_features = self.st_model.forward(features)
        #embeddings = out_features['sentence_embedding']
        #embeddings = embeddings.detach().cpu().numpy()

        return out_features['sentence_embedding']
    #"""

    @property
    def width(self) -> int:
        return self.st_model.get_sentence_embedding_dimension()

    @property
    def length(self) -> int:
        return self.st_model.get_max_seq_length()


# is MOTorch for given st_name (SentenceTransformer) based on TextEMB module
class TextEMB_MOTorch(MOTorch):

    def __init__(self, module_type:type(TextEMB)=TextEMB, **kwargs):

        if 'name' not in kwargs:
            if 'st_name' not in kwargs:
                raise TorchnessException('\'st_name\' must be given when MOTorch \'name\' is not given')
            st_name = kwargs['st_name']
            st_name_replaced = st_name.replace('/','__') # replace possible / in st_name since it conflicts with model folder name
            kwargs['name'] = f'TextEMB_MOTorch_{st_name_replaced}'

        MOTorch.__init__(self, module_type=module_type, **kwargs)

    def get_tokens(self, lines: List[str]):
        self.logger.info(f'{self.name} prepares tokens for {len(lines)} lines..')
        return self.module.tokenize(lines)

    def get_embeddings(
            self,
            lines: Union[List[str],str],
            show_progress_bar=  'auto') -> np.ndarray:

        if show_progress_bar == 'auto':
            show_progress_bar = False
            if self.logger.level < 21 and type(lines) is list and len(lines) > 1000:
                show_progress_bar = True

        self.logger.info(f'{self.name} prepares embeddings for {len(lines)} lines..')
        return self.module.encode(
            texts=              lines,
            device=             self.device, # fixes bug of SentenceTransformers.encode() device placement
            show_progress_bar=  show_progress_bar)

    def get_probs(self, lines:List[str]) -> np.ndarray:

        embs = self.get_embeddings(lines)

        num_splits = math.ceil(embs.shape[0] / self['fwd_batch_size']) # INFO: gives +- batch_size
        featsL = np.array_split(embs,num_splits)

        self.logger.info(f'TeXClas_MOTorch computes probs for {len(featsL)} batches of embeddings')
        iter = tqdm(featsL) if self.logger.level < 21 else featsL
        probsL = [self(feats)['probs'].cpu().detach().numpy() for feats in iter]
        probs = np.concatenate(probsL)
        self.logger.info(f'> got probs {probs.shape}')

        return probs

    def get_probsL(self, linesL:List[List[str]]) -> List[np.ndarray]:

        lines = []
        for l in linesL:
            lines += l

        probs = self.get_probs(lines)

        acc_lengths = []
        acc = 0
        for l in [len(ls) for ls in linesL]:
            acc_lengths.append(l+acc)
            acc += l
        acc_lengths.pop(-1)

        if acc_lengths: return np.split(probs,acc_lengths)
        else:           return [probs]

    @property
    def width(self) -> int:
        return self.module.width