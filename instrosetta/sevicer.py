import grpc


class RPCServicer:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.device = None

    def bind(self, server):
        raise NotImplementedError

def simple_get(resp, attr, alias='value'):
    def handler(self, request, context):
        try:
            value = getattr(self.device, attr)
            setattr(resp, alias, value)
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f'Failed to get {attr} from device. Details: {e}') 
        return resp
    return handler

def simple_set(resp, attr, value):
    def handler(self, request, context):
        try:
            setattr(self.device, attr, value)
            resp.success = True
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f'Failed to set {attr} on device to {value}. Details: {e}') 
            resp.success = False
        return resp
    return handler

def simple_call(resp, name, *args, **kwargs):
    def handler(self, request, context):
        try:
            getattr(self.device, name)(*args, **kwargs)
            resp.success = True
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f'Failed to call {name} on device. Details: {e}') 
            resp.success = False
        return resp
    return handler