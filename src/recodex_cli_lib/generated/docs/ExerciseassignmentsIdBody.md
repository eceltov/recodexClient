# ExerciseassignmentsIdBody

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **int** | Version of the edited assignment | 
**is_public** | **bool** | Is the assignment ready to be displayed to students? | 
**localized_texts** | **list[object]** | A description of the assignment | 
**first_deadline** | **int** | First deadline for submission of the assignment | 
**max_points_before_first_deadline** | **int** | A maximum of points that can be awarded for a submission before first deadline | 
**submissions_count_limit** | **int** | A maximum amount of submissions by a student for the assignment | 
**solution_files_limit** | **int** | Maximal number of files in a solution being submitted | 
**solution_size_limit** | **int** | Maximal size (bytes) of all files in a solution being submitted | 
**allow_second_deadline** | **bool** | Should there be a second deadline for students who didn&#x27;t make the first one? | 
**visible_from** | **int** | Date from which this assignment will be visible to students | [optional] 
**can_view_limit_ratios** | **bool** | Can all users view ratio of theirs solution memory and time usages and assignment limits? | 
**can_view_measured_values** | **bool** | Can all users view absolute memory and time values? | 
**can_view_judge_stdout** | **bool** | Can all users view judge primary log (stdout) of theirs solution? | 
**can_view_judge_stderr** | **bool** | Can all users view judge secondary log (stderr) of theirs solution? | 
**second_deadline** | **int** | A second deadline for submission of the assignment (with different point award) | [optional] 
**max_points_before_second_deadline** | **int** | A maximum of points that can be awarded for a late submission | [optional] 
**max_points_deadline_interpolation** | **bool** | Use linear interpolation for max. points between 1st and 2nd deadline | 
**is_bonus** | **bool** | If true, points from this exercise will not be included in overall score of group | 
**points_percentual_threshold** | **float** | A minimum percentage of points needed to gain point from assignment | [optional] 
**disabled_runtime_environment_ids** | **list[object]** | Identifiers of runtime environments that should not be used for student submissions | [optional] 
**send_notification** | **bool** | If email notification (when assignment becomes public) should be sent | [optional] 
**is_exam** | **bool** | This assignemnt is dedicated for an exam (should be solved in exam mode) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

