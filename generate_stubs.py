from grpc_tools import protoc
import subprocess
import os
if __name__ == '__main__':
    import argparse
    dir_path = os.path.dirname(os.path.realpath(__file__))
    parent_path = os.path.join(*os.path.split(dir_path)[:-1])
    default_root = os.path.join(parent_path,'instrosetta-proto')
    parser = argparse.ArgumentParser(description='Root proto path.')
    parser.add_argument('-PR', '--PROTOROOT', dest='rootDir', default=default_root,
                         help=f'Path to a valid config file.')
    cmd_args = parser.parse_args()
    rootDir = cmd_args.rootDir
    print(rootDir)
    proto_files = []
    for dirName, subdirList, fileList in os.walk(rootDir):
        print(dirName)
        for fname in fileList:
            if fname.endswith('.proto'):
                path = os.path.join(dirName, fname)
                proto_files.append(path)

    for path in proto_files:
        print(path)

        protoc.main((
            '',
            f'-I{rootDir}',
            '--python_out=./',
            '--grpc_python_out=./',
            # f'--csharp_out=../Instrosetta-csharp/Instrosetta/src/',
            # '--csharp_opt=base_namespace=',
            path,
        ))

