import grpc
from functools import wraps
import types
from instrosetta.utils.cases import snake_case, pascal_case

class RPCServicer:

    def __init__(self, *args, **kwargs):
        self.device = None

    def bind(self, server):
        raise NotImplementedError

class Property:
    def __init__(self, name, stubs, delegate_to=None, alias=None):
        self.name = pascal_case(name)
        if delegate_to is None:
            self.delegate = self
        else:
            self.delegate = getattr(self, delegate_to)
        if alias is None:
            self.alias = name
        else:
            self.alias = alias
        
class SimpleRPC:
    def __init__(self, response_class, *args, **kwargs):
        self.response_class = response_class

    def __call__(self, servicer, request, context):
        response = self.response_class()
        try:
            self.logic(servicer, request, response)
        except Exception as e:
            context.set_code(grpc.StatusCode.INTERNAL)
            context.set_details(f'Failed to perform rpc {self.__class__.__name__} for device. Details: {e}') 
        return response

    def __get__(self, servicer, servicertype=None):
        if servicer is None:
            return self
        return types.MethodType(self, servicer)

    def logic(self, servicer, request, response):
        raise NotImplementedError('No logic implemented.')

class PropertyRPC(SimpleRPC):
    def __init__(self, response_class, attr, alias=None, value_name='value'):
        super().__init__(response_class)
        self.attr = attr
        if alias is None:
            self.alias = pascal_case(attr)
        else:
            self.alias = alias
        self.value_name = value_name

class GetterRPC(PropertyRPC):
    def logic(self, servicer, request, response):
        value = getattr(servicer.device, self.attr)
        setattr(response, self.value_name, value)

class SetterRPC(PropertyRPC):
    def logic(self, servicer, request, response):
        value = getattr(request, self.value_name)
        setattr(servicer.device, self.attr, value)
        response.success = True

class MethodCallRPC(SimpleRPC):
    def __init__(self, response_class, method_name, args=(), request_args=(), return_name=None):
        super().__init__(response_class)
        self.method_name = method_name
        self.args = args
        self.kwargs = request_args
        self.return_name = return_name

    def logic(self, servicer, request, response):
        kwargs = {k: getattr(request, k) for k in self.kwargs}
        ret = getattr(servicer.device, self.method_name)(*self.args, **kwargs)
        if self.return_name is not None:
            setattr(response, self.return_name, ret)

def simple_rpc(response_class, description='RPC'):
    def decorator(func):
        def handler(self, request, context):
            response = response_class()
            try:
                func(self, request, response)
            except Exception as e:
                context.set_code(grpc.StatusCode.INTERNAL)
                context.set_details(f'{description} failed. Details: {e}')
            return response
        return handler
    return decorator

