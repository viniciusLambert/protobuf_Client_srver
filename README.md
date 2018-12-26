# protobuf_Client_srver
A toy comunication program  using multiple lenguages

# Instalação PROTOBUF
    curl -OL https://github.com/google/protobuf/releases/download/v3.2.0/protoc-3.2.0-linux-x86_64.zip
    unzip protoc-3.2.0-linux-x86_64.zip -d protoc3
    sudo mv protoc3/bin/* /usr/local/bin/
    sudo mv protoc3/include/* /usr/local/include/




# PYTHON
##      Instalação
###          GRPC
    grcp - pip install grpcio-tools
    pip install googleapis-common-protos


##      Gerar protos.

(executar na pasta soma)--
    python -m grpc_tools.protoc -I../../protos --python_out=. --grpc_python_out=. ../../protos/soma.proto

Os protos estão na pasta proto

Executar codigo -
    python nome-codigo.py



##      LINK ÚTEIS:
        https://grpc.io/docs/tutorials/basic/python.html



# JAVA
##      Instalação.
    sudo apt-get install default-jdk
    git clone -b v1.14.0 https://github.com/grpc/grpc-java.git
    cd grpc-java/examples
    ./gradlew installDist



##      Gerar protos

Colocar os protos na pasta
    grcp-java/examples/src/main/proto
E os .java
    grpc-java/examples/src/main/java/io/grpc/examples/"nomeProjeto"

Na pasta examples
    ./gradlew installDist

Executar cliente
    ./build/install/examples/bin/nome-client
Executar Server
    ./build/install/examples/bin/nome-server



##      LINK ÚTEIS:
https://grpc.io/docs/tutorials/basic/java.html
https://developers.google.com/protocol-buffers/docs/reference/java-generated


### Os código Helloword foram tirados dos repositorios proprietarios do Grcp
