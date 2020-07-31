import sys
import os


import graphsurgeon as gs
import uff


def prepare_namespace_plugin_map():
    trt_relu6 = gs.create_plugin_node(name="trt_relu6", op="Clip_TRT")
    namespace_plugin_map = {
        "Relu6": trt_relu6
    }
    return namespace_plugin_map

def model_path_to_uff_path(model_path):
    uff_path = os.path.splitext(model_path)[0] + ".uff"
    return uff_path

def model_to_uff(model_path,outputName = "score"):
    dynamic_graph = gs.DynamicGraph(model_path)
    dynamic_graph.collapse_namespaces(prepare_namespace_plugin_map())
    output_uff_path = model_path_to_uff_path(model_path)
    uff.from_tensorflow(
        dynamic_graph.as_graph_def(),
        [outputName],
        output_filename=output_uff_path,
        text=False
    )
    return output_uff_path



if __name__ == "__main__":
    MODEL_PATH = "D:/bxh/transferlearning_lite_2\Checkpoints\MaoLi_mobileNet_0710122934.pb"
    model_to_uff(MODEL_PATH)
