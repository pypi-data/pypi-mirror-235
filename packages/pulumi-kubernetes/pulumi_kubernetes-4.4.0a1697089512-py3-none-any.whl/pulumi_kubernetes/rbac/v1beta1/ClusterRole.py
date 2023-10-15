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
from ... import meta as _meta
from ._inputs import *

__all__ = ['ClusterRoleInitArgs', 'ClusterRole']

@pulumi.input_type
class ClusterRoleInitArgs:
    def __init__(__self__, *,
                 aggregation_rule: Optional[pulumi.Input['AggregationRuleArgs']] = None,
                 api_version: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input['_meta.v1.ObjectMetaArgs']] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input['PolicyRuleArgs']]]] = None):
        """
        The set of arguments for constructing a ClusterRole resource.
        :param pulumi.Input['AggregationRuleArgs'] aggregation_rule: AggregationRule is an optional field that describes how to build the Rules for this ClusterRole. If AggregationRule is set, then the Rules are controller managed and direct changes to Rules will be stomped by the controller.
        :param pulumi.Input[str] api_version: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
        :param pulumi.Input[str] kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
        :param pulumi.Input['_meta.v1.ObjectMetaArgs'] metadata: Standard object's metadata.
        :param pulumi.Input[Sequence[pulumi.Input['PolicyRuleArgs']]] rules: Rules holds all the PolicyRules for this ClusterRole
        """
        if aggregation_rule is not None:
            pulumi.set(__self__, "aggregation_rule", aggregation_rule)
        if api_version is not None:
            pulumi.set(__self__, "api_version", 'rbac.authorization.k8s.io/v1beta1')
        if kind is not None:
            pulumi.set(__self__, "kind", 'ClusterRole')
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if rules is not None:
            pulumi.set(__self__, "rules", rules)

    @property
    @pulumi.getter(name="aggregationRule")
    def aggregation_rule(self) -> Optional[pulumi.Input['AggregationRuleArgs']]:
        """
        AggregationRule is an optional field that describes how to build the Rules for this ClusterRole. If AggregationRule is set, then the Rules are controller managed and direct changes to Rules will be stomped by the controller.
        """
        return pulumi.get(self, "aggregation_rule")

    @aggregation_rule.setter
    def aggregation_rule(self, value: Optional[pulumi.Input['AggregationRuleArgs']]):
        pulumi.set(self, "aggregation_rule", value)

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
        Standard object's metadata.
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input['_meta.v1.ObjectMetaArgs']]):
        pulumi.set(self, "metadata", value)

    @property
    @pulumi.getter
    def rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['PolicyRuleArgs']]]]:
        """
        Rules holds all the PolicyRules for this ClusterRole
        """
        return pulumi.get(self, "rules")

    @rules.setter
    def rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['PolicyRuleArgs']]]]):
        pulumi.set(self, "rules", value)


class ClusterRole(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 aggregation_rule: Optional[pulumi.Input[pulumi.InputType['AggregationRuleArgs']]] = None,
                 api_version: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input[pulumi.InputType['_meta.v1.ObjectMetaArgs']]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PolicyRuleArgs']]]]] = None,
                 __props__=None):
        """
        ClusterRole is a cluster level, logical grouping of PolicyRules that can be referenced as a unit by a RoleBinding or ClusterRoleBinding. Deprecated in v1.17 in favor of rbac.authorization.k8s.io/v1 ClusterRole, and will no longer be served in v1.20.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['AggregationRuleArgs']] aggregation_rule: AggregationRule is an optional field that describes how to build the Rules for this ClusterRole. If AggregationRule is set, then the Rules are controller managed and direct changes to Rules will be stomped by the controller.
        :param pulumi.Input[str] api_version: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
        :param pulumi.Input[str] kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
        :param pulumi.Input[pulumi.InputType['_meta.v1.ObjectMetaArgs']] metadata: Standard object's metadata.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PolicyRuleArgs']]]] rules: Rules holds all the PolicyRules for this ClusterRole
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ClusterRoleInitArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ClusterRole is a cluster level, logical grouping of PolicyRules that can be referenced as a unit by a RoleBinding or ClusterRoleBinding. Deprecated in v1.17 in favor of rbac.authorization.k8s.io/v1 ClusterRole, and will no longer be served in v1.20.

        :param str resource_name: The name of the resource.
        :param ClusterRoleInitArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ClusterRoleInitArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 aggregation_rule: Optional[pulumi.Input[pulumi.InputType['AggregationRuleArgs']]] = None,
                 api_version: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input[pulumi.InputType['_meta.v1.ObjectMetaArgs']]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['PolicyRuleArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ClusterRoleInitArgs.__new__(ClusterRoleInitArgs)

            __props__.__dict__["aggregation_rule"] = aggregation_rule
            __props__.__dict__["api_version"] = 'rbac.authorization.k8s.io/v1beta1'
            __props__.__dict__["kind"] = 'ClusterRole'
            __props__.__dict__["metadata"] = metadata
            __props__.__dict__["rules"] = rules
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="kubernetes:rbac.authorization.k8s.io/v1:ClusterRole"), pulumi.Alias(type_="kubernetes:rbac.authorization.k8s.io/v1alpha1:ClusterRole")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ClusterRole, __self__).__init__(
            'kubernetes:rbac.authorization.k8s.io/v1beta1:ClusterRole',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ClusterRole':
        """
        Get an existing ClusterRole resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ClusterRoleInitArgs.__new__(ClusterRoleInitArgs)

        __props__.__dict__["aggregation_rule"] = None
        __props__.__dict__["api_version"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["metadata"] = None
        __props__.__dict__["rules"] = None
        return ClusterRole(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="aggregationRule")
    def aggregation_rule(self) -> pulumi.Output['outputs.AggregationRule']:
        """
        AggregationRule is an optional field that describes how to build the Rules for this ClusterRole. If AggregationRule is set, then the Rules are controller managed and direct changes to Rules will be stomped by the controller.
        """
        return pulumi.get(self, "aggregation_rule")

    @property
    @pulumi.getter(name="apiVersion")
    def api_version(self) -> pulumi.Output[str]:
        """
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
        """
        return pulumi.get(self, "api_version")

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
        Standard object's metadata.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def rules(self) -> pulumi.Output[Sequence['outputs.PolicyRule']]:
        """
        Rules holds all the PolicyRules for this ClusterRole
        """
        return pulumi.get(self, "rules")

