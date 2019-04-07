from grpc_tools import protoc
import subprocess
import os

proto_files = []
rootDir = '../instrosetta-proto'
for dirName, subdirList, fileList in os.walk(rootDir):
    for fname in fileList:
        if fname.endswith('.proto'):
            path = os.path.join(dirName, fname)
            proto_files.append(path)

for path in proto_files:
    print(path)

    subprocess.run((
        'protoc',
        f'-I{rootDir}',
        '--python_out=./',
        # '--grpc_python_out=./',
        f'--csharp_out=../Instrosetta-csharp/instrosetta/src/',
        # '--csharp_opt=base_namespace=',
        path,
    ))

