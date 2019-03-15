import grpc
from enum import Enum
import pint
from instrosetta.utils.units import accept_text
from instrosetta.interfaces.optomechanics import monochromator_pb2
from instrosetta.interfaces.optomechanics import monochromator_pb2_grpc

ureg = pint.UnitRegistry()
Q_ = ureg.Quantity


