# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetVolumeResult',
    'AwaitableGetVolumeResult',
    'get_volume',
    'get_volume_output',
]

@pulumi.output_type
class GetVolumeResult:
    """
    A collection of values returned by getVolume.
    """
    def __init__(__self__, description=None, droplet_ids=None, filesystem_label=None, filesystem_type=None, id=None, name=None, region=None, size=None, tags=None, urn=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if droplet_ids and not isinstance(droplet_ids, list):
            raise TypeError("Expected argument 'droplet_ids' to be a list")
        pulumi.set(__self__, "droplet_ids", droplet_ids)
        if filesystem_label and not isinstance(filesystem_label, str):
            raise TypeError("Expected argument 'filesystem_label' to be a str")
        pulumi.set(__self__, "filesystem_label", filesystem_label)
        if filesystem_type and not isinstance(filesystem_type, str):
            raise TypeError("Expected argument 'filesystem_type' to be a str")
        pulumi.set(__self__, "filesystem_type", filesystem_type)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)
        if size and not isinstance(size, int):
            raise TypeError("Expected argument 'size' to be a int")
        pulumi.set(__self__, "size", size)
        if tags and not isinstance(tags, list):
            raise TypeError("Expected argument 'tags' to be a list")
        pulumi.set(__self__, "tags", tags)
        if urn and not isinstance(urn, str):
            raise TypeError("Expected argument 'urn' to be a str")
        pulumi.set(__self__, "urn", urn)

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Text describing a block storage volume.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="dropletIds")
    def droplet_ids(self) -> Sequence[int]:
        """
        A list of associated Droplet ids.
        """
        return pulumi.get(self, "droplet_ids")

    @property
    @pulumi.getter(name="filesystemLabel")
    def filesystem_label(self) -> str:
        """
        Filesystem label currently in-use on the block storage volume.
        """
        return pulumi.get(self, "filesystem_label")

    @property
    @pulumi.getter(name="filesystemType")
    def filesystem_type(self) -> str:
        """
        Filesystem type currently in-use on the block storage volume.
        """
        return pulumi.get(self, "filesystem_type")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def region(self) -> Optional[str]:
        return pulumi.get(self, "region")

    @property
    @pulumi.getter
    def size(self) -> int:
        """
        The size of the block storage volume in GiB.
        """
        return pulumi.get(self, "size")

    @property
    @pulumi.getter
    def tags(self) -> Sequence[str]:
        """
        A list of the tags associated to the Volume.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def urn(self) -> str:
        """
        The uniform resource name for the storage volume.
        """
        return pulumi.get(self, "urn")


class AwaitableGetVolumeResult(GetVolumeResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVolumeResult(
            description=self.description,
            droplet_ids=self.droplet_ids,
            filesystem_label=self.filesystem_label,
            filesystem_type=self.filesystem_type,
            id=self.id,
            name=self.name,
            region=self.region,
            size=self.size,
            tags=self.tags,
            urn=self.urn)


def get_volume(description: Optional[str] = None,
               name: Optional[str] = None,
               region: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVolumeResult:
    """
    Get information on a volume for use in other resources. This data source provides
    all of the volumes properties as configured on your DigitalOcean account. This is
    useful if the volume in question is not managed by the provider or you need to utilize
    any of the volumes data.

    An error is triggered if the provided volume name does not exist.

    ## Example Usage

    Get the volume:

    ```python
    import pulumi
    import pulumi_digitalocean as digitalocean

    example = digitalocean.get_volume(name="app-data",
        region="nyc3")
    ```

    Reuse the data about a volume to attach it to a Droplet:

    ```python
    import pulumi
    import pulumi_digitalocean as digitalocean

    example_volume = digitalocean.get_volume(name="app-data",
        region="nyc3")
    example_droplet = digitalocean.Droplet("exampleDroplet",
        size="s-1vcpu-1gb",
        image="ubuntu-18-04-x64",
        region="nyc3")
    foobar = digitalocean.VolumeAttachment("foobar",
        droplet_id=example_droplet.id,
        volume_id=example_volume.id)
    ```


    :param str description: Text describing a block storage volume.
    :param str name: The name of block storage volume.
    :param str region: The region the block storage volume is provisioned in.
    """
    __args__ = dict()
    __args__['description'] = description
    __args__['name'] = name
    __args__['region'] = region
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('digitalocean:index/getVolume:getVolume', __args__, opts=opts, typ=GetVolumeResult).value

    return AwaitableGetVolumeResult(
        description=pulumi.get(__ret__, 'description'),
        droplet_ids=pulumi.get(__ret__, 'droplet_ids'),
        filesystem_label=pulumi.get(__ret__, 'filesystem_label'),
        filesystem_type=pulumi.get(__ret__, 'filesystem_type'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        region=pulumi.get(__ret__, 'region'),
        size=pulumi.get(__ret__, 'size'),
        tags=pulumi.get(__ret__, 'tags'),
        urn=pulumi.get(__ret__, 'urn'))


@_utilities.lift_output_func(get_volume)
def get_volume_output(description: Optional[pulumi.Input[Optional[str]]] = None,
                      name: Optional[pulumi.Input[str]] = None,
                      region: Optional[pulumi.Input[Optional[str]]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVolumeResult]:
    """
    Get information on a volume for use in other resources. This data source provides
    all of the volumes properties as configured on your DigitalOcean account. This is
    useful if the volume in question is not managed by the provider or you need to utilize
    any of the volumes data.

    An error is triggered if the provided volume name does not exist.

    ## Example Usage

    Get the volume:

    ```python
    import pulumi
    import pulumi_digitalocean as digitalocean

    example = digitalocean.get_volume(name="app-data",
        region="nyc3")
    ```

    Reuse the data about a volume to attach it to a Droplet:

    ```python
    import pulumi
    import pulumi_digitalocean as digitalocean

    example_volume = digitalocean.get_volume(name="app-data",
        region="nyc3")
    example_droplet = digitalocean.Droplet("exampleDroplet",
        size="s-1vcpu-1gb",
        image="ubuntu-18-04-x64",
        region="nyc3")
    foobar = digitalocean.VolumeAttachment("foobar",
        droplet_id=example_droplet.id,
        volume_id=example_volume.id)
    ```


    :param str description: Text describing a block storage volume.
    :param str name: The name of block storage volume.
    :param str region: The region the block storage volume is provisioned in.
    """
    ...
