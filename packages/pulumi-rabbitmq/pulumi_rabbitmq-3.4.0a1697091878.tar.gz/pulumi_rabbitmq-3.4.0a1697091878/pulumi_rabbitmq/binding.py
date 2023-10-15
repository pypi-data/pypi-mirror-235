# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['BindingArgs', 'Binding']

@pulumi.input_type
class BindingArgs:
    def __init__(__self__, *,
                 destination: pulumi.Input[str],
                 destination_type: pulumi.Input[str],
                 source: pulumi.Input[str],
                 vhost: pulumi.Input[str],
                 arguments: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 arguments_json: Optional[pulumi.Input[str]] = None,
                 routing_key: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Binding resource.
        :param pulumi.Input[str] destination: The destination queue or exchange.
        :param pulumi.Input[str] destination_type: The type of destination (queue or exchange).
        :param pulumi.Input[str] source: The source exchange.
        :param pulumi.Input[str] vhost: The vhost to create the resource in.
        :param pulumi.Input[Mapping[str, Any]] arguments: Additional key/value arguments for the binding.
        :param pulumi.Input[str] routing_key: A routing key for the binding.
        """
        BindingArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            destination=destination,
            destination_type=destination_type,
            source=source,
            vhost=vhost,
            arguments=arguments,
            arguments_json=arguments_json,
            routing_key=routing_key,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             destination: pulumi.Input[str],
             destination_type: pulumi.Input[str],
             source: pulumi.Input[str],
             vhost: pulumi.Input[str],
             arguments: Optional[pulumi.Input[Mapping[str, Any]]] = None,
             arguments_json: Optional[pulumi.Input[str]] = None,
             routing_key: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("destination", destination)
        _setter("destination_type", destination_type)
        _setter("source", source)
        _setter("vhost", vhost)
        if arguments is not None:
            _setter("arguments", arguments)
        if arguments_json is not None:
            _setter("arguments_json", arguments_json)
        if routing_key is not None:
            _setter("routing_key", routing_key)

    @property
    @pulumi.getter
    def destination(self) -> pulumi.Input[str]:
        """
        The destination queue or exchange.
        """
        return pulumi.get(self, "destination")

    @destination.setter
    def destination(self, value: pulumi.Input[str]):
        pulumi.set(self, "destination", value)

    @property
    @pulumi.getter(name="destinationType")
    def destination_type(self) -> pulumi.Input[str]:
        """
        The type of destination (queue or exchange).
        """
        return pulumi.get(self, "destination_type")

    @destination_type.setter
    def destination_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "destination_type", value)

    @property
    @pulumi.getter
    def source(self) -> pulumi.Input[str]:
        """
        The source exchange.
        """
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: pulumi.Input[str]):
        pulumi.set(self, "source", value)

    @property
    @pulumi.getter
    def vhost(self) -> pulumi.Input[str]:
        """
        The vhost to create the resource in.
        """
        return pulumi.get(self, "vhost")

    @vhost.setter
    def vhost(self, value: pulumi.Input[str]):
        pulumi.set(self, "vhost", value)

    @property
    @pulumi.getter
    def arguments(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        Additional key/value arguments for the binding.
        """
        return pulumi.get(self, "arguments")

    @arguments.setter
    def arguments(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "arguments", value)

    @property
    @pulumi.getter(name="argumentsJson")
    def arguments_json(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "arguments_json")

    @arguments_json.setter
    def arguments_json(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "arguments_json", value)

    @property
    @pulumi.getter(name="routingKey")
    def routing_key(self) -> Optional[pulumi.Input[str]]:
        """
        A routing key for the binding.
        """
        return pulumi.get(self, "routing_key")

    @routing_key.setter
    def routing_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "routing_key", value)


@pulumi.input_type
class _BindingState:
    def __init__(__self__, *,
                 arguments: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 arguments_json: Optional[pulumi.Input[str]] = None,
                 destination: Optional[pulumi.Input[str]] = None,
                 destination_type: Optional[pulumi.Input[str]] = None,
                 properties_key: Optional[pulumi.Input[str]] = None,
                 routing_key: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[str]] = None,
                 vhost: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Binding resources.
        :param pulumi.Input[Mapping[str, Any]] arguments: Additional key/value arguments for the binding.
        :param pulumi.Input[str] destination: The destination queue or exchange.
        :param pulumi.Input[str] destination_type: The type of destination (queue or exchange).
        :param pulumi.Input[str] properties_key: A unique key to refer to the binding.
        :param pulumi.Input[str] routing_key: A routing key for the binding.
        :param pulumi.Input[str] source: The source exchange.
        :param pulumi.Input[str] vhost: The vhost to create the resource in.
        """
        _BindingState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            arguments=arguments,
            arguments_json=arguments_json,
            destination=destination,
            destination_type=destination_type,
            properties_key=properties_key,
            routing_key=routing_key,
            source=source,
            vhost=vhost,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             arguments: Optional[pulumi.Input[Mapping[str, Any]]] = None,
             arguments_json: Optional[pulumi.Input[str]] = None,
             destination: Optional[pulumi.Input[str]] = None,
             destination_type: Optional[pulumi.Input[str]] = None,
             properties_key: Optional[pulumi.Input[str]] = None,
             routing_key: Optional[pulumi.Input[str]] = None,
             source: Optional[pulumi.Input[str]] = None,
             vhost: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if arguments is not None:
            _setter("arguments", arguments)
        if arguments_json is not None:
            _setter("arguments_json", arguments_json)
        if destination is not None:
            _setter("destination", destination)
        if destination_type is not None:
            _setter("destination_type", destination_type)
        if properties_key is not None:
            _setter("properties_key", properties_key)
        if routing_key is not None:
            _setter("routing_key", routing_key)
        if source is not None:
            _setter("source", source)
        if vhost is not None:
            _setter("vhost", vhost)

    @property
    @pulumi.getter
    def arguments(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        Additional key/value arguments for the binding.
        """
        return pulumi.get(self, "arguments")

    @arguments.setter
    def arguments(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "arguments", value)

    @property
    @pulumi.getter(name="argumentsJson")
    def arguments_json(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "arguments_json")

    @arguments_json.setter
    def arguments_json(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "arguments_json", value)

    @property
    @pulumi.getter
    def destination(self) -> Optional[pulumi.Input[str]]:
        """
        The destination queue or exchange.
        """
        return pulumi.get(self, "destination")

    @destination.setter
    def destination(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "destination", value)

    @property
    @pulumi.getter(name="destinationType")
    def destination_type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of destination (queue or exchange).
        """
        return pulumi.get(self, "destination_type")

    @destination_type.setter
    def destination_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "destination_type", value)

    @property
    @pulumi.getter(name="propertiesKey")
    def properties_key(self) -> Optional[pulumi.Input[str]]:
        """
        A unique key to refer to the binding.
        """
        return pulumi.get(self, "properties_key")

    @properties_key.setter
    def properties_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "properties_key", value)

    @property
    @pulumi.getter(name="routingKey")
    def routing_key(self) -> Optional[pulumi.Input[str]]:
        """
        A routing key for the binding.
        """
        return pulumi.get(self, "routing_key")

    @routing_key.setter
    def routing_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "routing_key", value)

    @property
    @pulumi.getter
    def source(self) -> Optional[pulumi.Input[str]]:
        """
        The source exchange.
        """
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source", value)

    @property
    @pulumi.getter
    def vhost(self) -> Optional[pulumi.Input[str]]:
        """
        The vhost to create the resource in.
        """
        return pulumi.get(self, "vhost")

    @vhost.setter
    def vhost(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vhost", value)


class Binding(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 arguments: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 arguments_json: Optional[pulumi.Input[str]] = None,
                 destination: Optional[pulumi.Input[str]] = None,
                 destination_type: Optional[pulumi.Input[str]] = None,
                 routing_key: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[str]] = None,
                 vhost: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The ``Binding`` resource creates and manages a binding relationship
        between a queue an exchange.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_rabbitmq as rabbitmq

        test_v_host = rabbitmq.VHost("testVHost")
        guest = rabbitmq.Permissions("guest",
            permissions=rabbitmq.PermissionsPermissionsArgs(
                configure=".*",
                read=".*",
                write=".*",
            ),
            user="guest",
            vhost=test_v_host.name)
        test_exchange = rabbitmq.Exchange("testExchange",
            settings=rabbitmq.ExchangeSettingsArgs(
                auto_delete=True,
                durable=False,
                type="fanout",
            ),
            vhost=guest.vhost)
        test_queue = rabbitmq.Queue("testQueue",
            settings=rabbitmq.QueueSettingsArgs(
                auto_delete=False,
                durable=True,
            ),
            vhost=guest.vhost)
        test_binding = rabbitmq.Binding("testBinding",
            destination=test_queue.name,
            destination_type="queue",
            routing_key="#",
            source=test_exchange.name,
            vhost=test_v_host.name)
        ```

        ## Import

        Bindings can be imported using the `id` which is composed of

         `vhost/source/destination/destination_type/properties_key`. E.g.

        ```sh
         $ pulumi import rabbitmq:index/binding:Binding test test/test/test/queue/%23
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, Any]] arguments: Additional key/value arguments for the binding.
        :param pulumi.Input[str] destination: The destination queue or exchange.
        :param pulumi.Input[str] destination_type: The type of destination (queue or exchange).
        :param pulumi.Input[str] routing_key: A routing key for the binding.
        :param pulumi.Input[str] source: The source exchange.
        :param pulumi.Input[str] vhost: The vhost to create the resource in.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BindingArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The ``Binding`` resource creates and manages a binding relationship
        between a queue an exchange.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_rabbitmq as rabbitmq

        test_v_host = rabbitmq.VHost("testVHost")
        guest = rabbitmq.Permissions("guest",
            permissions=rabbitmq.PermissionsPermissionsArgs(
                configure=".*",
                read=".*",
                write=".*",
            ),
            user="guest",
            vhost=test_v_host.name)
        test_exchange = rabbitmq.Exchange("testExchange",
            settings=rabbitmq.ExchangeSettingsArgs(
                auto_delete=True,
                durable=False,
                type="fanout",
            ),
            vhost=guest.vhost)
        test_queue = rabbitmq.Queue("testQueue",
            settings=rabbitmq.QueueSettingsArgs(
                auto_delete=False,
                durable=True,
            ),
            vhost=guest.vhost)
        test_binding = rabbitmq.Binding("testBinding",
            destination=test_queue.name,
            destination_type="queue",
            routing_key="#",
            source=test_exchange.name,
            vhost=test_v_host.name)
        ```

        ## Import

        Bindings can be imported using the `id` which is composed of

         `vhost/source/destination/destination_type/properties_key`. E.g.

        ```sh
         $ pulumi import rabbitmq:index/binding:Binding test test/test/test/queue/%23
        ```

        :param str resource_name: The name of the resource.
        :param BindingArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BindingArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            BindingArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 arguments: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 arguments_json: Optional[pulumi.Input[str]] = None,
                 destination: Optional[pulumi.Input[str]] = None,
                 destination_type: Optional[pulumi.Input[str]] = None,
                 routing_key: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[str]] = None,
                 vhost: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = BindingArgs.__new__(BindingArgs)

            __props__.__dict__["arguments"] = arguments
            __props__.__dict__["arguments_json"] = arguments_json
            if destination is None and not opts.urn:
                raise TypeError("Missing required property 'destination'")
            __props__.__dict__["destination"] = destination
            if destination_type is None and not opts.urn:
                raise TypeError("Missing required property 'destination_type'")
            __props__.__dict__["destination_type"] = destination_type
            __props__.__dict__["routing_key"] = routing_key
            if source is None and not opts.urn:
                raise TypeError("Missing required property 'source'")
            __props__.__dict__["source"] = source
            if vhost is None and not opts.urn:
                raise TypeError("Missing required property 'vhost'")
            __props__.__dict__["vhost"] = vhost
            __props__.__dict__["properties_key"] = None
        super(Binding, __self__).__init__(
            'rabbitmq:index/binding:Binding',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            arguments: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            arguments_json: Optional[pulumi.Input[str]] = None,
            destination: Optional[pulumi.Input[str]] = None,
            destination_type: Optional[pulumi.Input[str]] = None,
            properties_key: Optional[pulumi.Input[str]] = None,
            routing_key: Optional[pulumi.Input[str]] = None,
            source: Optional[pulumi.Input[str]] = None,
            vhost: Optional[pulumi.Input[str]] = None) -> 'Binding':
        """
        Get an existing Binding resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, Any]] arguments: Additional key/value arguments for the binding.
        :param pulumi.Input[str] destination: The destination queue or exchange.
        :param pulumi.Input[str] destination_type: The type of destination (queue or exchange).
        :param pulumi.Input[str] properties_key: A unique key to refer to the binding.
        :param pulumi.Input[str] routing_key: A routing key for the binding.
        :param pulumi.Input[str] source: The source exchange.
        :param pulumi.Input[str] vhost: The vhost to create the resource in.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _BindingState.__new__(_BindingState)

        __props__.__dict__["arguments"] = arguments
        __props__.__dict__["arguments_json"] = arguments_json
        __props__.__dict__["destination"] = destination
        __props__.__dict__["destination_type"] = destination_type
        __props__.__dict__["properties_key"] = properties_key
        __props__.__dict__["routing_key"] = routing_key
        __props__.__dict__["source"] = source
        __props__.__dict__["vhost"] = vhost
        return Binding(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def arguments(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        """
        Additional key/value arguments for the binding.
        """
        return pulumi.get(self, "arguments")

    @property
    @pulumi.getter(name="argumentsJson")
    def arguments_json(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "arguments_json")

    @property
    @pulumi.getter
    def destination(self) -> pulumi.Output[str]:
        """
        The destination queue or exchange.
        """
        return pulumi.get(self, "destination")

    @property
    @pulumi.getter(name="destinationType")
    def destination_type(self) -> pulumi.Output[str]:
        """
        The type of destination (queue or exchange).
        """
        return pulumi.get(self, "destination_type")

    @property
    @pulumi.getter(name="propertiesKey")
    def properties_key(self) -> pulumi.Output[str]:
        """
        A unique key to refer to the binding.
        """
        return pulumi.get(self, "properties_key")

    @property
    @pulumi.getter(name="routingKey")
    def routing_key(self) -> pulumi.Output[Optional[str]]:
        """
        A routing key for the binding.
        """
        return pulumi.get(self, "routing_key")

    @property
    @pulumi.getter
    def source(self) -> pulumi.Output[str]:
        """
        The source exchange.
        """
        return pulumi.get(self, "source")

    @property
    @pulumi.getter
    def vhost(self) -> pulumi.Output[str]:
        """
        The vhost to create the resource in.
        """
        return pulumi.get(self, "vhost")

