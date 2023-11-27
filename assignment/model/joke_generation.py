import tiktoken
import torch

from .gpt import Config, GPT, device
from assignment import ROOT_DIR

load_model_path = f'{ROOT_DIR}/model/model'  # here is the path to saved model

enc = tiktoken.get_encoding("gpt2")

max_seq_len = 100
tokens = 50257


def generate_joke(sentences):
    '''
    Something smart happens here.
    :param sentences:
    :return:
    '''
    config = Config(tokens, max_seq_len)
    model = GPT(config).to(device)
    model.load_state_dict(torch.load(load_model_path, map_location=torch.device('cpu')))
    model.eval()

    start = torch.tensor([enc.encode(sentences)], dtype=torch.long, device=device)
    return enc.decode(model.generate(xs=start, max_new_tokens=30, do_sample=True)[0].tolist())