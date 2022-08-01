from tvm.driver import tvmc
import onnx

model = tvmc.load('resnet50-v2-7.onnx')
