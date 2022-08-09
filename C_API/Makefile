CXX = clang++
CXXFLAGS = -O3 -I$${TVM_HOME}/include/ -I$${TVM_HOME}/3rdparty/dmlc-core/include/ -I$${TVM_HOME}/3rdparty/dlpack/include/ -L$${TVM_HOME}/build -ldl -pthread -llibtvm_runtime

main: main.o
	${CXX} -o ${@} ${CXXFLAGS} ${^}
