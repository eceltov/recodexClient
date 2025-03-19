# ExercisesIdBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **int** | Version of the edited exercise | [optional] 
**difficulty** | **str** | Difficulty of an exercise, should be one of &#x27;easy&#x27;, &#x27;medium&#x27; or &#x27;hard&#x27; | [optional] 
**localized_texts** | **list[object]** | A description of the exercise | [optional] 
**is_public** | **bool** | Exercise can be public or private | [optional] 
**is_locked** | **bool** | If true, the exercise cannot be assigned | [optional] 
**configuration_type** | **str** | Identifies the way the evaluation of the exercise is configured | [optional] 
**solution_files_limit** | **int** | Maximal number of files in a solution being submitted (default for assignments) | [optional] 
**solution_size_limit** | **int** | Maximal size (bytes) of all files in a solution being submitted (default for assignments) | [optional] 
**merge_judge_logs** | **bool** | If true, judge stderr will be merged into stdout (default for assignments) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

