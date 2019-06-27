# import_pb
How to import graphDefs in .pb or .pbtxt file format to TensorBoard 

To view the example graph file provided in this repository:

1. At the command prompt:  python import_pb.py --graph ./frozen_graph.pb --log_dir=./tb_logs
2. At the command prompt:  tensorboard --logdir=./tb_logs --port 6006 --host localhost
3. Open a web browser then paste the following into the URL bar: http://localhost:6006/

TensorBoard should open and display the graph.
