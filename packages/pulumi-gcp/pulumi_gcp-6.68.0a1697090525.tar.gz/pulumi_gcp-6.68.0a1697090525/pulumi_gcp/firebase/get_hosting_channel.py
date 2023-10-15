# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetHostingChannelResult',
    'AwaitableGetHostingChannelResult',
    'get_hosting_channel',
    'get_hosting_channel_output',
]

@pulumi.output_type
class GetHostingChannelResult:
    """
    A collection of values returned by getHostingChannel.
    """
    def __init__(__self__, channel_id=None, expire_time=None, id=None, labels=None, name=None, retained_release_count=None, site_id=None, ttl=None):
        if channel_id and not isinstance(channel_id, str):
            raise TypeError("Expected argument 'channel_id' to be a str")
        pulumi.set(__self__, "channel_id", channel_id)
        if expire_time and not isinstance(expire_time, str):
            raise TypeError("Expected argument 'expire_time' to be a str")
        pulumi.set(__self__, "expire_time", expire_time)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        pulumi.set(__self__, "labels", labels)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if retained_release_count and not isinstance(retained_release_count, int):
            raise TypeError("Expected argument 'retained_release_count' to be a int")
        pulumi.set(__self__, "retained_release_count", retained_release_count)
        if site_id and not isinstance(site_id, str):
            raise TypeError("Expected argument 'site_id' to be a str")
        pulumi.set(__self__, "site_id", site_id)
        if ttl and not isinstance(ttl, str):
            raise TypeError("Expected argument 'ttl' to be a str")
        pulumi.set(__self__, "ttl", ttl)

    @property
    @pulumi.getter(name="channelId")
    def channel_id(self) -> str:
        return pulumi.get(self, "channel_id")

    @property
    @pulumi.getter(name="expireTime")
    def expire_time(self) -> str:
        return pulumi.get(self, "expire_time")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def labels(self) -> Mapping[str, str]:
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The fully-qualified resource name for the channel, in the format: `sites/{{site_id}}/channels/{{channel_id}}`.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="retainedReleaseCount")
    def retained_release_count(self) -> int:
        return pulumi.get(self, "retained_release_count")

    @property
    @pulumi.getter(name="siteId")
    def site_id(self) -> str:
        return pulumi.get(self, "site_id")

    @property
    @pulumi.getter
    def ttl(self) -> str:
        return pulumi.get(self, "ttl")


class AwaitableGetHostingChannelResult(GetHostingChannelResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetHostingChannelResult(
            channel_id=self.channel_id,
            expire_time=self.expire_time,
            id=self.id,
            labels=self.labels,
            name=self.name,
            retained_release_count=self.retained_release_count,
            site_id=self.site_id,
            ttl=self.ttl)


def get_hosting_channel(channel_id: Optional[str] = None,
                        site_id: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetHostingChannelResult:
    """
    Use this data source to access information about an existing resource.

    :param str channel_id: The ID of the channel. Use `channel_id = "live"` for the default channel of a site.
    :param str site_id: The ID of the site this channel belongs to.
    """
    __args__ = dict()
    __args__['channelId'] = channel_id
    __args__['siteId'] = site_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('gcp:firebase/getHostingChannel:getHostingChannel', __args__, opts=opts, typ=GetHostingChannelResult).value

    return AwaitableGetHostingChannelResult(
        channel_id=pulumi.get(__ret__, 'channel_id'),
        expire_time=pulumi.get(__ret__, 'expire_time'),
        id=pulumi.get(__ret__, 'id'),
        labels=pulumi.get(__ret__, 'labels'),
        name=pulumi.get(__ret__, 'name'),
        retained_release_count=pulumi.get(__ret__, 'retained_release_count'),
        site_id=pulumi.get(__ret__, 'site_id'),
        ttl=pulumi.get(__ret__, 'ttl'))


@_utilities.lift_output_func(get_hosting_channel)
def get_hosting_channel_output(channel_id: Optional[pulumi.Input[str]] = None,
                               site_id: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetHostingChannelResult]:
    """
    Use this data source to access information about an existing resource.

    :param str channel_id: The ID of the channel. Use `channel_id = "live"` for the default channel of a site.
    :param str site_id: The ID of the site this channel belongs to.
    """
    ...
