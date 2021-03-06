# coding: utf-8

"""
    Chat API SDK

    The SDK allows you to receive and send messages through your WhatsApp account. [Sign up now](https://app.chat-api.com/)  The Chat API is based on the WhatsApp WEB protocol and excludes the ban both when using libraries from mgp25 and the like. Despite this, your account can be banned by anti-spam system WhatsApp after several clicking the \"block\" button.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: sale@chat-api.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import
import re  # noqa: F401
import sys  # noqa: F401

import six  # noqa: F401

from openapi_client.model_utils import (  # noqa: F401
    ModelComposed,
    ModelNormal,
    ModelSimple,
    date,
    datetime,
    file_type,
    int,
    none_type,
    str,
    validate_get_composed_info,
)


class InlineResponse2005Update(ModelNormal):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
    }

    validations = {
    }

    additional_properties_type = None

    @staticmethod
    def openapi_types():
        """
        This must be a class method so a model may have properties that are
        of type self, this ensures that we don't create a cyclic import

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        return {
            'webhook_url': (str, none_type,),  # noqa: E501
            'ack_notifications_on': (bool, none_type,),  # noqa: E501
            'chat_update_on': (bool, none_type,),  # noqa: E501
            'video_upload_on': (bool, none_type,),  # noqa: E501
            'proxy': (str, none_type,),  # noqa: E501
            'guaranteed_hooks': (bool, none_type,),  # noqa: E501
            'ignore_old_messages': (bool, none_type,),  # noqa: E501
            'process_archive': (bool, none_type,),  # noqa: E501
            'instance_statuses': (bool, none_type,),  # noqa: E501
            'webhook_statuses': (bool, none_type,),  # noqa: E501
            'status_notifications_on': (bool, none_type,),  # noqa: E501
        }

    @staticmethod
    def discriminator():
        return None

    attribute_map = {
        'webhook_url': 'webhookUrl',  # noqa: E501
        'ack_notifications_on': 'ackNotificationsOn',  # noqa: E501
        'chat_update_on': 'chatUpdateOn',  # noqa: E501
        'video_upload_on': 'videoUploadOn',  # noqa: E501
        'proxy': 'proxy',  # noqa: E501
        'guaranteed_hooks': 'guaranteedHooks',  # noqa: E501
        'ignore_old_messages': 'ignoreOldMessages',  # noqa: E501
        'process_archive': 'processArchive',  # noqa: E501
        'instance_statuses': 'instanceStatuses',  # noqa: E501
        'webhook_statuses': 'webhookStatuses',  # noqa: E501
        'status_notifications_on': 'statusNotificationsOn',  # noqa: E501
    }

    @staticmethod
    def _composed_schemas():
        return None

    required_properties = set([
        '_data_store',
        '_check_type',
        '_from_server',
        '_path_to_item',
        '_configuration',
    ])

    def __init__(self, _check_type=True, _from_server=False, _path_to_item=(), _configuration=None, **kwargs):  # noqa: E501
        """inline_response2005_update.InlineResponse2005Update - a model defined in OpenAPI


        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _from_server (bool): True if the data is from the server
                                False if the data is from the client (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            webhook_url (str, none_type): [optional]  # noqa: E501
            ack_notifications_on (bool, none_type): [optional]  # noqa: E501
            chat_update_on (bool, none_type): [optional]  # noqa: E501
            video_upload_on (bool, none_type): [optional]  # noqa: E501
            proxy (str, none_type): [optional]  # noqa: E501
            guaranteed_hooks (bool, none_type): [optional]  # noqa: E501
            ignore_old_messages (bool, none_type): [optional]  # noqa: E501
            process_archive (bool, none_type): [optional]  # noqa: E501
            instance_statuses (bool, none_type): [optional]  # noqa: E501
            webhook_statuses (bool, none_type): [optional]  # noqa: E501
            status_notifications_on (bool, none_type): [optional]  # noqa: E501
        """

        self._data_store = {}
        self._check_type = _check_type
        self._from_server = _from_server
        self._path_to_item = _path_to_item
        self._configuration = _configuration

        for var_name, var_value in six.iteritems(kwargs):
            setattr(self, var_name, var_value)
