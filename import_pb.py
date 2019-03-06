'''
Import a protobuf graph (.pb) into Tensorboard

Example usage:
python import_pb.py --graph=./freeze/frozen_graph.pb  --log_dir=./tb_logs
'''

import argparse
from tensorflow.python.tools import import_pb_to_tensorboard


def run_main():
  parser = argparse.ArgumentParser(description='Script to import frozen graph into TensorBoard')
  parser.add_argument(
      '-g', '--graph',
      type=str,
      default='',
      help="Protobuf graph file (.pb) to import into TensorBoard.",
      required='True')
  parser.add_argument(
      '-l', '--log_dir',
      type=str,
      default='',
      help="TensorBoard log directory.",
      required='True')

  flags = parser.parse_args()

  import_pb_to_tensorboard.import_to_tensorboard(model_dir=flags.graph, log_dir=flags.log_dir)
  print('..or try `tensorboard --logdir=%s --port 6006 --host localhost`' % flags.log_dir)


if __name__ == '__main__':
    run_main()
