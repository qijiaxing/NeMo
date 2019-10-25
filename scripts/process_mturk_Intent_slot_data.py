import argparse
import os

# Parsing arguments
parser = argparse.ArgumentParser(
    description='Joint intent slot filling system with pretrained BERT')
parser.add_argument("--data_dir", default='data/mturk', type=str)
parser.add_argument("--dataset_name", default='mturk', type=str)
parser.add_argument("--work_dir", default='outputs', type=str)
parser.add_argument("--do_lower_case", action='store_false')
parser.add_argument("--shuffle_data", action='store_false')

args = parser.parse_args()

if not os.path.exists(args.data_dir):
    raise ValueError(f'Data not found at {args.data_dir}')

work_dir = f'{args.work_dir}/{args.dataset_name.upper()}'

with open(args.data_dir, 'r') as f:
    utterances = f.readlines()

def analyze_inter_annotator_agreement(num_annotators, utterances):
	print("Agreement here")
	print(f'You had {num_annotators} annotators')
	print(utterances[1:10])


analyze_inter_annotator_agreement(3, utterances)