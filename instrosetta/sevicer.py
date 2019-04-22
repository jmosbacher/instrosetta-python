import grpc
from functools import wraps

class RPCServicer:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.device = None

    def bind(self, server):
        raise NotImplementedError

def simple_get(response_class, attr, alias='value'):
    def handler(self, request, context):
        resp = response_class()
        try:
            value = getattr(self.device, attr)
            setattr(resp, alias, value)
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f'Failed to get {attr} from device. Details: {e}') 
        return resp
    return handler

def simple_set(response_class, attr, alias='value'):
    def handler(self, request, context):
        resp = response_class()
        try:
            value = getattr(request, alias)
            setattr(self.device, attr, value)
            resp.success = True
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f'Failed to set {attr} on device to {value}. Details: {e}') 
            resp.success = False
        return resp
    return handler

def simple_call(response_class, name, **aliases):
    def handler(self, request, context):
        resp = response_class()
        try:
            kwargs = {k: getattr(request, v) for k,v in aliases.items()}
            getattr(self.device, name)(**kwargs)
            resp.success = True
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f'Failed to call {name} on device. Details: {e}') 
            resp.success = False
        return resp
    return handler

def simple_rpc(func, response_class, description='RPC'):
    @wraps(func)
    def handler(self, request, context):
        response = response_class()
        try:
            func(self, request, response)
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f'{description} failed. Details: {e}')
        return response
    return handler