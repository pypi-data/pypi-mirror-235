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

__all__ = ['ValidatingAdmissionPolicyBindingPatchArgs', 'ValidatingAdmissionPolicyBindingPatch']

@pulumi.input_type
class ValidatingAdmissionPolicyBindingPatchArgs:
    def __init__(__self__, *,
                 api_version: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input['_meta.v1.ObjectMetaPatchArgs']] = None,
                 spec: Optional[pulumi.Input['ValidatingAdmissionPolicyBindingSpecPatchArgs']] = None):
        """
        The set of arguments for constructing a ValidatingAdmissionPolicyBindingPatch resource.
        :param pulumi.Input[str] api_version: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
        :param pulumi.Input[str] kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
        :param pulumi.Input['_meta.v1.ObjectMetaPatchArgs'] metadata: Standard object metadata; More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata.
        :param pulumi.Input['ValidatingAdmissionPolicyBindingSpecPatchArgs'] spec: Specification of the desired behavior of the ValidatingAdmissionPolicyBinding.
        """
        if api_version is not None:
            pulumi.set(__self__, "api_version", 'admissionregistration.k8s.io/v1alpha1')
        if kind is not None:
            pulumi.set(__self__, "kind", 'ValidatingAdmissionPolicyBinding')
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if spec is not None:
            pulumi.set(__self__, "spec", spec)

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
    def metadata(self) -> Optional[pulumi.Input['_meta.v1.ObjectMetaPatchArgs']]:
        """
        Standard object metadata; More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata.
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input['_meta.v1.ObjectMetaPatchArgs']]):
        pulumi.set(self, "metadata", value)

    @property
    @pulumi.getter
    def spec(self) -> Optional[pulumi.Input['ValidatingAdmissionPolicyBindingSpecPatchArgs']]:
        """
        Specification of the desired behavior of the ValidatingAdmissionPolicyBinding.
        """
        return pulumi.get(self, "spec")

    @spec.setter
    def spec(self, value: Optional[pulumi.Input['ValidatingAdmissionPolicyBindingSpecPatchArgs']]):
        pulumi.set(self, "spec", value)


class ValidatingAdmissionPolicyBindingPatch(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_version: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input[pulumi.InputType['_meta.v1.ObjectMetaPatchArgs']]] = None,
                 spec: Optional[pulumi.Input[pulumi.InputType['ValidatingAdmissionPolicyBindingSpecPatchArgs']]] = None,
                 __props__=None):
        """
        Patch resources are used to modify existing Kubernetes resources by using
        Server-Side Apply updates. The name of the resource must be specified, but all other properties are optional. More than
        one patch may be applied to the same resource, and a random FieldManager name will be used for each Patch resource.
        Conflicts will result in an error by default, but can be forced using the "pulumi.com/patchForce" annotation. See the
        [Server-Side Apply Docs](https://www.pulumi.com/registry/packages/kubernetes/how-to-guides/managing-resources-with-server-side-apply/) for
        additional information about using Server-Side Apply to manage Kubernetes resources with Pulumi.
        ValidatingAdmissionPolicyBinding binds the ValidatingAdmissionPolicy with paramerized resources. ValidatingAdmissionPolicyBinding and parameter CRDs together define how cluster administrators configure policies for clusters.

        For a given admission request, each binding will cause its policy to be evaluated N times, where N is 1 for policies/bindings that don't use params, otherwise N is the number of parameters selected by the binding.

        The CEL expressions of a policy must have a computed CEL cost below the maximum CEL budget. Each evaluation of the policy is given an independent CEL cost budget. Adding/removing policies, bindings, or params can not affect whether a given (policy, binding, param) combination is within its own CEL budget.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_version: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
        :param pulumi.Input[str] kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
        :param pulumi.Input[pulumi.InputType['_meta.v1.ObjectMetaPatchArgs']] metadata: Standard object metadata; More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata.
        :param pulumi.Input[pulumi.InputType['ValidatingAdmissionPolicyBindingSpecPatchArgs']] spec: Specification of the desired behavior of the ValidatingAdmissionPolicyBinding.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ValidatingAdmissionPolicyBindingPatchArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Patch resources are used to modify existing Kubernetes resources by using
        Server-Side Apply updates. The name of the resource must be specified, but all other properties are optional. More than
        one patch may be applied to the same resource, and a random FieldManager name will be used for each Patch resource.
        Conflicts will result in an error by default, but can be forced using the "pulumi.com/patchForce" annotation. See the
        [Server-Side Apply Docs](https://www.pulumi.com/registry/packages/kubernetes/how-to-guides/managing-resources-with-server-side-apply/) for
        additional information about using Server-Side Apply to manage Kubernetes resources with Pulumi.
        ValidatingAdmissionPolicyBinding binds the ValidatingAdmissionPolicy with paramerized resources. ValidatingAdmissionPolicyBinding and parameter CRDs together define how cluster administrators configure policies for clusters.

        For a given admission request, each binding will cause its policy to be evaluated N times, where N is 1 for policies/bindings that don't use params, otherwise N is the number of parameters selected by the binding.

        The CEL expressions of a policy must have a computed CEL cost below the maximum CEL budget. Each evaluation of the policy is given an independent CEL cost budget. Adding/removing policies, bindings, or params can not affect whether a given (policy, binding, param) combination is within its own CEL budget.

        :param str resource_name: The name of the resource.
        :param ValidatingAdmissionPolicyBindingPatchArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ValidatingAdmissionPolicyBindingPatchArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_version: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input[pulumi.InputType['_meta.v1.ObjectMetaPatchArgs']]] = None,
                 spec: Optional[pulumi.Input[pulumi.InputType['ValidatingAdmissionPolicyBindingSpecPatchArgs']]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ValidatingAdmissionPolicyBindingPatchArgs.__new__(ValidatingAdmissionPolicyBindingPatchArgs)

            __props__.__dict__["api_version"] = 'admissionregistration.k8s.io/v1alpha1'
            __props__.__dict__["kind"] = 'ValidatingAdmissionPolicyBinding'
            __props__.__dict__["metadata"] = metadata
            __props__.__dict__["spec"] = spec
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="kubernetes:admissionregistration.k8s.io/v1beta1:ValidatingAdmissionPolicyBindingPatch")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ValidatingAdmissionPolicyBindingPatch, __self__).__init__(
            'kubernetes:admissionregistration.k8s.io/v1alpha1:ValidatingAdmissionPolicyBindingPatch',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ValidatingAdmissionPolicyBindingPatch':
        """
        Get an existing ValidatingAdmissionPolicyBindingPatch resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ValidatingAdmissionPolicyBindingPatchArgs.__new__(ValidatingAdmissionPolicyBindingPatchArgs)

        __props__.__dict__["api_version"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["metadata"] = None
        __props__.__dict__["spec"] = None
        return ValidatingAdmissionPolicyBindingPatch(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="apiVersion")
    def api_version(self) -> pulumi.Output[Optional[str]]:
        """
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
        """
        return pulumi.get(self, "api_version")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[str]]:
        """
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[Optional['_meta.v1.outputs.ObjectMetaPatch']]:
        """
        Standard object metadata; More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def spec(self) -> pulumi.Output[Optional['outputs.ValidatingAdmissionPolicyBindingSpecPatch']]:
        """
        Specification of the desired behavior of the ValidatingAdmissionPolicyBinding.
        """
        return pulumi.get(self, "spec")

