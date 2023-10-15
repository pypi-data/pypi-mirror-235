# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ... import core as _core
from ... import meta as _meta
from ._inputs import *

__all__ = ['EventInitArgs', 'Event']

@pulumi.input_type
class EventInitArgs:
    def __init__(__self__, *,
                 event_time: pulumi.Input[str],
                 action: Optional[pulumi.Input[str]] = None,
                 api_version: Optional[pulumi.Input[str]] = None,
                 deprecated_count: Optional[pulumi.Input[int]] = None,
                 deprecated_first_timestamp: Optional[pulumi.Input[str]] = None,
                 deprecated_last_timestamp: Optional[pulumi.Input[str]] = None,
                 deprecated_source: Optional[pulumi.Input['_core.v1.EventSourceArgs']] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input['_meta.v1.ObjectMetaArgs']] = None,
                 note: Optional[pulumi.Input[str]] = None,
                 reason: Optional[pulumi.Input[str]] = None,
                 regarding: Optional[pulumi.Input['_core.v1.ObjectReferenceArgs']] = None,
                 related: Optional[pulumi.Input['_core.v1.ObjectReferenceArgs']] = None,
                 reporting_controller: Optional[pulumi.Input[str]] = None,
                 reporting_instance: Optional[pulumi.Input[str]] = None,
                 series: Optional[pulumi.Input['EventSeriesArgs']] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Event resource.
        :param pulumi.Input[str] event_time: eventTime is the time when this Event was first observed. It is required.
        :param pulumi.Input[str] action: action is what action was taken/failed regarding to the regarding object. It is machine-readable. This field cannot be empty for new Events and it can have at most 128 characters.
        :param pulumi.Input[str] api_version: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
        :param pulumi.Input[int] deprecated_count: deprecatedCount is the deprecated field assuring backward compatibility with core.v1 Event type.
        :param pulumi.Input[str] deprecated_first_timestamp: deprecatedFirstTimestamp is the deprecated field assuring backward compatibility with core.v1 Event type.
        :param pulumi.Input[str] deprecated_last_timestamp: deprecatedLastTimestamp is the deprecated field assuring backward compatibility with core.v1 Event type.
        :param pulumi.Input['_core.v1.EventSourceArgs'] deprecated_source: deprecatedSource is the deprecated field assuring backward compatibility with core.v1 Event type.
        :param pulumi.Input[str] kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
        :param pulumi.Input['_meta.v1.ObjectMetaArgs'] metadata: Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
        :param pulumi.Input[str] note: note is a human-readable description of the status of this operation. Maximal length of the note is 1kB, but libraries should be prepared to handle values up to 64kB.
        :param pulumi.Input[str] reason: reason is why the action was taken. It is human-readable. This field cannot be empty for new Events and it can have at most 128 characters.
        :param pulumi.Input['_core.v1.ObjectReferenceArgs'] regarding: regarding contains the object this Event is about. In most cases it's an Object reporting controller implements, e.g. ReplicaSetController implements ReplicaSets and this event is emitted because it acts on some changes in a ReplicaSet object.
        :param pulumi.Input['_core.v1.ObjectReferenceArgs'] related: related is the optional secondary object for more complex actions. E.g. when regarding object triggers a creation or deletion of related object.
        :param pulumi.Input[str] reporting_controller: reportingController is the name of the controller that emitted this Event, e.g. `kubernetes.io/kubelet`. This field cannot be empty for new Events.
        :param pulumi.Input[str] reporting_instance: reportingInstance is the ID of the controller instance, e.g. `kubelet-xyzf`. This field cannot be empty for new Events and it can have at most 128 characters.
        :param pulumi.Input['EventSeriesArgs'] series: series is data about the Event series this event represents or nil if it's a singleton Event.
        :param pulumi.Input[str] type: type is the type of this event (Normal, Warning), new types could be added in the future. It is machine-readable. This field cannot be empty for new Events.
        """
        pulumi.set(__self__, "event_time", event_time)
        if action is not None:
            pulumi.set(__self__, "action", action)
        if api_version is not None:
            pulumi.set(__self__, "api_version", 'events.k8s.io/v1')
        if deprecated_count is not None:
            pulumi.set(__self__, "deprecated_count", deprecated_count)
        if deprecated_first_timestamp is not None:
            pulumi.set(__self__, "deprecated_first_timestamp", deprecated_first_timestamp)
        if deprecated_last_timestamp is not None:
            pulumi.set(__self__, "deprecated_last_timestamp", deprecated_last_timestamp)
        if deprecated_source is not None:
            pulumi.set(__self__, "deprecated_source", deprecated_source)
        if kind is not None:
            pulumi.set(__self__, "kind", 'Event')
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if note is not None:
            pulumi.set(__self__, "note", note)
        if reason is not None:
            pulumi.set(__self__, "reason", reason)
        if regarding is not None:
            pulumi.set(__self__, "regarding", regarding)
        if related is not None:
            pulumi.set(__self__, "related", related)
        if reporting_controller is not None:
            pulumi.set(__self__, "reporting_controller", reporting_controller)
        if reporting_instance is not None:
            pulumi.set(__self__, "reporting_instance", reporting_instance)
        if series is not None:
            pulumi.set(__self__, "series", series)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="eventTime")
    def event_time(self) -> pulumi.Input[str]:
        """
        eventTime is the time when this Event was first observed. It is required.
        """
        return pulumi.get(self, "event_time")

    @event_time.setter
    def event_time(self, value: pulumi.Input[str]):
        pulumi.set(self, "event_time", value)

    @property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input[str]]:
        """
        action is what action was taken/failed regarding to the regarding object. It is machine-readable. This field cannot be empty for new Events and it can have at most 128 characters.
        """
        return pulumi.get(self, "action")

    @action.setter
    def action(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "action", value)

    @property
    @pulumi.getter(name="apiVersion")
    def api_version(self) -> Optional[pulumi.Input[str]]:
        """
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
        """
        return pulumi.get(self, "api_version")

    @api_version.setter
    def api_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_version", value)

    @property
    @pulumi.getter(name="deprecatedCount")
    def deprecated_count(self) -> Optional[pulumi.Input[int]]:
        """
        deprecatedCount is the deprecated field assuring backward compatibility with core.v1 Event type.
        """
        return pulumi.get(self, "deprecated_count")

    @deprecated_count.setter
    def deprecated_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "deprecated_count", value)

    @property
    @pulumi.getter(name="deprecatedFirstTimestamp")
    def deprecated_first_timestamp(self) -> Optional[pulumi.Input[str]]:
        """
        deprecatedFirstTimestamp is the deprecated field assuring backward compatibility with core.v1 Event type.
        """
        return pulumi.get(self, "deprecated_first_timestamp")

    @deprecated_first_timestamp.setter
    def deprecated_first_timestamp(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "deprecated_first_timestamp", value)

    @property
    @pulumi.getter(name="deprecatedLastTimestamp")
    def deprecated_last_timestamp(self) -> Optional[pulumi.Input[str]]:
        """
        deprecatedLastTimestamp is the deprecated field assuring backward compatibility with core.v1 Event type.
        """
        return pulumi.get(self, "deprecated_last_timestamp")

    @deprecated_last_timestamp.setter
    def deprecated_last_timestamp(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "deprecated_last_timestamp", value)

    @property
    @pulumi.getter(name="deprecatedSource")
    def deprecated_source(self) -> Optional[pulumi.Input['_core.v1.EventSourceArgs']]:
        """
        deprecatedSource is the deprecated field assuring backward compatibility with core.v1 Event type.
        """
        return pulumi.get(self, "deprecated_source")

    @deprecated_source.setter
    def deprecated_source(self, value: Optional[pulumi.Input['_core.v1.EventSourceArgs']]):
        pulumi.set(self, "deprecated_source", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[str]]:
        """
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input['_meta.v1.ObjectMetaArgs']]:
        """
        Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input['_meta.v1.ObjectMetaArgs']]):
        pulumi.set(self, "metadata", value)

    @property
    @pulumi.getter
    def note(self) -> Optional[pulumi.Input[str]]:
        """
        note is a human-readable description of the status of this operation. Maximal length of the note is 1kB, but libraries should be prepared to handle values up to 64kB.
        """
        return pulumi.get(self, "note")

    @note.setter
    def note(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "note", value)

    @property
    @pulumi.getter
    def reason(self) -> Optional[pulumi.Input[str]]:
        """
        reason is why the action was taken. It is human-readable. This field cannot be empty for new Events and it can have at most 128 characters.
        """
        return pulumi.get(self, "reason")

    @reason.setter
    def reason(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "reason", value)

    @property
    @pulumi.getter
    def regarding(self) -> Optional[pulumi.Input['_core.v1.ObjectReferenceArgs']]:
        """
        regarding contains the object this Event is about. In most cases it's an Object reporting controller implements, e.g. ReplicaSetController implements ReplicaSets and this event is emitted because it acts on some changes in a ReplicaSet object.
        """
        return pulumi.get(self, "regarding")

    @regarding.setter
    def regarding(self, value: Optional[pulumi.Input['_core.v1.ObjectReferenceArgs']]):
        pulumi.set(self, "regarding", value)

    @property
    @pulumi.getter
    def related(self) -> Optional[pulumi.Input['_core.v1.ObjectReferenceArgs']]:
        """
        related is the optional secondary object for more complex actions. E.g. when regarding object triggers a creation or deletion of related object.
        """
        return pulumi.get(self, "related")

    @related.setter
    def related(self, value: Optional[pulumi.Input['_core.v1.ObjectReferenceArgs']]):
        pulumi.set(self, "related", value)

    @property
    @pulumi.getter(name="reportingController")
    def reporting_controller(self) -> Optional[pulumi.Input[str]]:
        """
        reportingController is the name of the controller that emitted this Event, e.g. `kubernetes.io/kubelet`. This field cannot be empty for new Events.
        """
        return pulumi.get(self, "reporting_controller")

    @reporting_controller.setter
    def reporting_controller(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "reporting_controller", value)

    @property
    @pulumi.getter(name="reportingInstance")
    def reporting_instance(self) -> Optional[pulumi.Input[str]]:
        """
        reportingInstance is the ID of the controller instance, e.g. `kubelet-xyzf`. This field cannot be empty for new Events and it can have at most 128 characters.
        """
        return pulumi.get(self, "reporting_instance")

    @reporting_instance.setter
    def reporting_instance(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "reporting_instance", value)

    @property
    @pulumi.getter
    def series(self) -> Optional[pulumi.Input['EventSeriesArgs']]:
        """
        series is data about the Event series this event represents or nil if it's a singleton Event.
        """
        return pulumi.get(self, "series")

    @series.setter
    def series(self, value: Optional[pulumi.Input['EventSeriesArgs']]):
        pulumi.set(self, "series", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        type is the type of this event (Normal, Warning), new types could be added in the future. It is machine-readable. This field cannot be empty for new Events.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


class Event(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 action: Optional[pulumi.Input[str]] = None,
                 api_version: Optional[pulumi.Input[str]] = None,
                 deprecated_count: Optional[pulumi.Input[int]] = None,
                 deprecated_first_timestamp: Optional[pulumi.Input[str]] = None,
                 deprecated_last_timestamp: Optional[pulumi.Input[str]] = None,
                 deprecated_source: Optional[pulumi.Input[pulumi.InputType['_core.v1.EventSourceArgs']]] = None,
                 event_time: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input[pulumi.InputType['_meta.v1.ObjectMetaArgs']]] = None,
                 note: Optional[pulumi.Input[str]] = None,
                 reason: Optional[pulumi.Input[str]] = None,
                 regarding: Optional[pulumi.Input[pulumi.InputType['_core.v1.ObjectReferenceArgs']]] = None,
                 related: Optional[pulumi.Input[pulumi.InputType['_core.v1.ObjectReferenceArgs']]] = None,
                 reporting_controller: Optional[pulumi.Input[str]] = None,
                 reporting_instance: Optional[pulumi.Input[str]] = None,
                 series: Optional[pulumi.Input[pulumi.InputType['EventSeriesArgs']]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Event is a report of an event somewhere in the cluster. It generally denotes some state change in the system. Events have a limited retention time and triggers and messages may evolve with time.  Event consumers should not rely on the timing of an event with a given Reason reflecting a consistent underlying trigger, or the continued existence of events with that Reason.  Events should be treated as informative, best-effort, supplemental data.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] action: action is what action was taken/failed regarding to the regarding object. It is machine-readable. This field cannot be empty for new Events and it can have at most 128 characters.
        :param pulumi.Input[str] api_version: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
        :param pulumi.Input[int] deprecated_count: deprecatedCount is the deprecated field assuring backward compatibility with core.v1 Event type.
        :param pulumi.Input[str] deprecated_first_timestamp: deprecatedFirstTimestamp is the deprecated field assuring backward compatibility with core.v1 Event type.
        :param pulumi.Input[str] deprecated_last_timestamp: deprecatedLastTimestamp is the deprecated field assuring backward compatibility with core.v1 Event type.
        :param pulumi.Input[pulumi.InputType['_core.v1.EventSourceArgs']] deprecated_source: deprecatedSource is the deprecated field assuring backward compatibility with core.v1 Event type.
        :param pulumi.Input[str] event_time: eventTime is the time when this Event was first observed. It is required.
        :param pulumi.Input[str] kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
        :param pulumi.Input[pulumi.InputType['_meta.v1.ObjectMetaArgs']] metadata: Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
        :param pulumi.Input[str] note: note is a human-readable description of the status of this operation. Maximal length of the note is 1kB, but libraries should be prepared to handle values up to 64kB.
        :param pulumi.Input[str] reason: reason is why the action was taken. It is human-readable. This field cannot be empty for new Events and it can have at most 128 characters.
        :param pulumi.Input[pulumi.InputType['_core.v1.ObjectReferenceArgs']] regarding: regarding contains the object this Event is about. In most cases it's an Object reporting controller implements, e.g. ReplicaSetController implements ReplicaSets and this event is emitted because it acts on some changes in a ReplicaSet object.
        :param pulumi.Input[pulumi.InputType['_core.v1.ObjectReferenceArgs']] related: related is the optional secondary object for more complex actions. E.g. when regarding object triggers a creation or deletion of related object.
        :param pulumi.Input[str] reporting_controller: reportingController is the name of the controller that emitted this Event, e.g. `kubernetes.io/kubelet`. This field cannot be empty for new Events.
        :param pulumi.Input[str] reporting_instance: reportingInstance is the ID of the controller instance, e.g. `kubelet-xyzf`. This field cannot be empty for new Events and it can have at most 128 characters.
        :param pulumi.Input[pulumi.InputType['EventSeriesArgs']] series: series is data about the Event series this event represents or nil if it's a singleton Event.
        :param pulumi.Input[str] type: type is the type of this event (Normal, Warning), new types could be added in the future. It is machine-readable. This field cannot be empty for new Events.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: EventInitArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Event is a report of an event somewhere in the cluster. It generally denotes some state change in the system. Events have a limited retention time and triggers and messages may evolve with time.  Event consumers should not rely on the timing of an event with a given Reason reflecting a consistent underlying trigger, or the continued existence of events with that Reason.  Events should be treated as informative, best-effort, supplemental data.

        :param str resource_name: The name of the resource.
        :param EventInitArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(EventInitArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 action: Optional[pulumi.Input[str]] = None,
                 api_version: Optional[pulumi.Input[str]] = None,
                 deprecated_count: Optional[pulumi.Input[int]] = None,
                 deprecated_first_timestamp: Optional[pulumi.Input[str]] = None,
                 deprecated_last_timestamp: Optional[pulumi.Input[str]] = None,
                 deprecated_source: Optional[pulumi.Input[pulumi.InputType['_core.v1.EventSourceArgs']]] = None,
                 event_time: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input[pulumi.InputType['_meta.v1.ObjectMetaArgs']]] = None,
                 note: Optional[pulumi.Input[str]] = None,
                 reason: Optional[pulumi.Input[str]] = None,
                 regarding: Optional[pulumi.Input[pulumi.InputType['_core.v1.ObjectReferenceArgs']]] = None,
                 related: Optional[pulumi.Input[pulumi.InputType['_core.v1.ObjectReferenceArgs']]] = None,
                 reporting_controller: Optional[pulumi.Input[str]] = None,
                 reporting_instance: Optional[pulumi.Input[str]] = None,
                 series: Optional[pulumi.Input[pulumi.InputType['EventSeriesArgs']]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = EventInitArgs.__new__(EventInitArgs)

            __props__.__dict__["action"] = action
            __props__.__dict__["api_version"] = 'events.k8s.io/v1'
            __props__.__dict__["deprecated_count"] = deprecated_count
            __props__.__dict__["deprecated_first_timestamp"] = deprecated_first_timestamp
            __props__.__dict__["deprecated_last_timestamp"] = deprecated_last_timestamp
            __props__.__dict__["deprecated_source"] = deprecated_source
            if event_time is None and not opts.urn:
                raise TypeError("Missing required property 'event_time'")
            __props__.__dict__["event_time"] = event_time
            __props__.__dict__["kind"] = 'Event'
            __props__.__dict__["metadata"] = metadata
            __props__.__dict__["note"] = note
            __props__.__dict__["reason"] = reason
            __props__.__dict__["regarding"] = regarding
            __props__.__dict__["related"] = related
            __props__.__dict__["reporting_controller"] = reporting_controller
            __props__.__dict__["reporting_instance"] = reporting_instance
            __props__.__dict__["series"] = series
            __props__.__dict__["type"] = type
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="kubernetes:core/v1:Event"), pulumi.Alias(type_="kubernetes:events.k8s.io/v1beta1:Event")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Event, __self__).__init__(
            'kubernetes:events.k8s.io/v1:Event',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Event':
        """
        Get an existing Event resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = EventInitArgs.__new__(EventInitArgs)

        __props__.__dict__["action"] = None
        __props__.__dict__["api_version"] = None
        __props__.__dict__["deprecated_count"] = None
        __props__.__dict__["deprecated_first_timestamp"] = None
        __props__.__dict__["deprecated_last_timestamp"] = None
        __props__.__dict__["deprecated_source"] = None
        __props__.__dict__["event_time"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["metadata"] = None
        __props__.__dict__["note"] = None
        __props__.__dict__["reason"] = None
        __props__.__dict__["regarding"] = None
        __props__.__dict__["related"] = None
        __props__.__dict__["reporting_controller"] = None
        __props__.__dict__["reporting_instance"] = None
        __props__.__dict__["series"] = None
        __props__.__dict__["type"] = None
        return Event(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def action(self) -> pulumi.Output[str]:
        """
        action is what action was taken/failed regarding to the regarding object. It is machine-readable. This field cannot be empty for new Events and it can have at most 128 characters.
        """
        return pulumi.get(self, "action")

    @property
    @pulumi.getter(name="apiVersion")
    def api_version(self) -> pulumi.Output[str]:
        """
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
        """
        return pulumi.get(self, "api_version")

    @property
    @pulumi.getter(name="deprecatedCount")
    def deprecated_count(self) -> pulumi.Output[int]:
        """
        deprecatedCount is the deprecated field assuring backward compatibility with core.v1 Event type.
        """
        return pulumi.get(self, "deprecated_count")

    @property
    @pulumi.getter(name="deprecatedFirstTimestamp")
    def deprecated_first_timestamp(self) -> pulumi.Output[str]:
        """
        deprecatedFirstTimestamp is the deprecated field assuring backward compatibility with core.v1 Event type.
        """
        return pulumi.get(self, "deprecated_first_timestamp")

    @property
    @pulumi.getter(name="deprecatedLastTimestamp")
    def deprecated_last_timestamp(self) -> pulumi.Output[str]:
        """
        deprecatedLastTimestamp is the deprecated field assuring backward compatibility with core.v1 Event type.
        """
        return pulumi.get(self, "deprecated_last_timestamp")

    @property
    @pulumi.getter(name="deprecatedSource")
    def deprecated_source(self) -> pulumi.Output['_core.v1.outputs.EventSource']:
        """
        deprecatedSource is the deprecated field assuring backward compatibility with core.v1 Event type.
        """
        return pulumi.get(self, "deprecated_source")

    @property
    @pulumi.getter(name="eventTime")
    def event_time(self) -> pulumi.Output[str]:
        """
        eventTime is the time when this Event was first observed. It is required.
        """
        return pulumi.get(self, "event_time")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def metadata(self) -> pulumi.Output['_meta.v1.outputs.ObjectMeta']:
        """
        Standard object's metadata. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def note(self) -> pulumi.Output[str]:
        """
        note is a human-readable description of the status of this operation. Maximal length of the note is 1kB, but libraries should be prepared to handle values up to 64kB.
        """
        return pulumi.get(self, "note")

    @property
    @pulumi.getter
    def reason(self) -> pulumi.Output[str]:
        """
        reason is why the action was taken. It is human-readable. This field cannot be empty for new Events and it can have at most 128 characters.
        """
        return pulumi.get(self, "reason")

    @property
    @pulumi.getter
    def regarding(self) -> pulumi.Output['_core.v1.outputs.ObjectReference']:
        """
        regarding contains the object this Event is about. In most cases it's an Object reporting controller implements, e.g. ReplicaSetController implements ReplicaSets and this event is emitted because it acts on some changes in a ReplicaSet object.
        """
        return pulumi.get(self, "regarding")

    @property
    @pulumi.getter
    def related(self) -> pulumi.Output['_core.v1.outputs.ObjectReference']:
        """
        related is the optional secondary object for more complex actions. E.g. when regarding object triggers a creation or deletion of related object.
        """
        return pulumi.get(self, "related")

    @property
    @pulumi.getter(name="reportingController")
    def reporting_controller(self) -> pulumi.Output[str]:
        """
        reportingController is the name of the controller that emitted this Event, e.g. `kubernetes.io/kubelet`. This field cannot be empty for new Events.
        """
        return pulumi.get(self, "reporting_controller")

    @property
    @pulumi.getter(name="reportingInstance")
    def reporting_instance(self) -> pulumi.Output[str]:
        """
        reportingInstance is the ID of the controller instance, e.g. `kubelet-xyzf`. This field cannot be empty for new Events and it can have at most 128 characters.
        """
        return pulumi.get(self, "reporting_instance")

    @property
    @pulumi.getter
    def series(self) -> pulumi.Output['outputs.EventSeries']:
        """
        series is data about the Event series this event represents or nil if it's a singleton Event.
        """
        return pulumi.get(self, "series")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        type is the type of this event (Normal, Warning), new types could be added in the future. It is machine-readable. This field cannot be empty for new Events.
        """
        return pulumi.get(self, "type")

