"""
ltcodecs.nullable_codec
------------------------------

This module contains the NullableCodec class, which uses a boolean field to control whether a target field is optionally
encoded.
"""

from __future__ import annotations
from bitstring import BitArray, ConstBitStream, Bits
from .multiple_field_codec import MultipleFieldCodec
import ltcodecs as ltcodecs
from typing import Any
from .exceptions import EncodingFailed


class OptionalFieldCodec(MultipleFieldCodec):
    """
    codec for optional fields, where a boolean field controls whether a "target" field should be encoded.

    If the controlling field is true, the target field will be encoded using target_params.  If false, the
    target_field won't be encoded.

    :param target_field: Target field name
    :param target_type: ROS type of the target field (as a string)
    :param target_params: dictionary with target field codec parameters
    """

    def __init__(
        self, target_field: str, target_type: str, target_params=None, **kwargs
    ) -> None:
        self.target_field = target_field
        if target_params:
            self.target_field_codec = ltcodecs.field_codec_classes[target_type](
                **target_params
            )
        else:
            self.target_field_codec = ltcodecs.field_codec_classes[target_type]()

    def encode_multiple(self, value: bool, message_dict: dict) -> tuple[Bits, bool, dict]:
        """
        encode a pair of fields: the boolean used to control the "nullable" target, and the target if requested

        :param value: the boolean field value that indicates whether the target should be encoded
        :param message_dict: the full message from which the target field is read
        """
        value = bool(value)
        value_bits = BitArray(bool=value)

        # If the value is false, we treat this like a boolean codec
        if not value:
            return value_bits, value, {}

        # Otherwise, we want to encode a bit (to indicate that the target is present), and then the target
        target_bits, target_value = self.target_field_codec.encode(message_dict[self.target_field])
        value_bits.append(target_bits)

        return value_bits, value, {self.target_field: target_value}

    def decode_multiple(self, bits_to_decode: ConstBitStream) -> tuple[bool, dict]:
        """
        decode a nullable (optional) field: the boolean used to control the "nullable" target, and the target if present

        Args:
            bits_to_decode: the bits to decode

        Returns:
            value: the value of the controlling boolean field
            values_dict: Dictionary with other decoded field name: value pairs
        """

        value = bits_to_decode.read("bool")

        if not value:
            return value, {}

        target_value = self.target_field_codec.decode(bits_to_decode)
        return value, {self.target_field: target_value}

    @property
    def min_length_bits(self) -> int:
        return 1

    @property
    def max_length_bits(self) -> int:
        return 1 + self.target_field_codec.max_length_bits
