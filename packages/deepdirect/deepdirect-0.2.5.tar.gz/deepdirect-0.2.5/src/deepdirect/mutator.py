import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from deepdirect.model import build_aa_mutator
import pkg_resources

def predict(input_lst):
    relative_path_to_weight = '/weights/model_i_weights.h5'
    weight_file_path = pkg_resources.resource_filename('deepdirect', relative_path_to_weight)
    aa_mutator = build_aa_mutator()
    aa_mutator.load_weights(weight_file_path)
    return aa_mutator.predict(input_lst)
    