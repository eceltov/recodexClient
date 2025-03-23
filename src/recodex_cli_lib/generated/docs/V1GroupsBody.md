# V1GroupsBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance_id** | **str** | An identifier of the instance where the group should be created | 
**external_id** | **str** | An informative, human readable identifier of the group | [optional] 
**parent_group_id** | **str** | Identifier of the parent group (if none is given, a top-level group is created) | [optional] 
**public_stats** | **bool** | Should students be able to see each other&#x27;s results? | [optional] 
**detaining** | **bool** | Are students prevented from leaving the group on their own? | [optional] 
**is_public** | **bool** | Should the group be visible to all student? | [optional] 
**is_organizational** | **bool** | Whether the group is organizational (no assignments nor students). | [optional] 
**is_exam** | **bool** | Whether the group is an exam group. | [optional] 
**localized_texts** | **list[object]** | Localized names and descriptions | [optional] 
**threshold** | **int** | A minimum percentage of points needed to pass the course | [optional] 
**points_limit** | **int** | A minimum of (absolute) points needed to pass the course | [optional] 
**no_admin** | **bool** | If true, no admin is assigned to group (current user is assigned as admin by default. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

