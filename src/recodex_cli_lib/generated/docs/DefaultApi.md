# swagger_client.DefaultApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assignment_solution_reviews_default**](DefaultApi.md#assignment_solution_reviews_default) | **GET** /v1/assignment-solutions/{id}/review | Get detail of the solution and a list of review comments.
[**assignment_solution_reviews_delete_comment**](DefaultApi.md#assignment_solution_reviews_delete_comment) | **DELETE** /v1/assignment-solutions/{id}/review-comment/{commentId} | Remove one comment from a review.
[**assignment_solution_reviews_edit_comment**](DefaultApi.md#assignment_solution_reviews_edit_comment) | **POST** /v1/assignment-solutions/{id}/review-comment/{commentId} | Update existing comment within a review.
[**assignment_solution_reviews_new_comment**](DefaultApi.md#assignment_solution_reviews_new_comment) | **POST** /v1/assignment-solutions/{id}/review-comment | Create a new comment within a review.
[**assignment_solution_reviews_pending**](DefaultApi.md#assignment_solution_reviews_pending) | **GET** /v1/users/{id}/pending-reviews | Return all solutions with pending reviews that given user teaches (is admin/supervisor in corresponding groups). Along with that it returns all assignment entities of the corresponding solutions.
[**assignment_solution_reviews_remove**](DefaultApi.md#assignment_solution_reviews_remove) | **DELETE** /v1/assignment-solutions/{id}/review | Update the state of the review process of the solution.
[**assignment_solution_reviews_update**](DefaultApi.md#assignment_solution_reviews_update) | **POST** /v1/assignment-solutions/{id}/review | Update the state of the review process of the solution.
[**assignment_solutions_delete_solution**](DefaultApi.md#assignment_solutions_delete_solution) | **DELETE** /v1/assignment-solutions/{id} | Delete assignment solution with given identification.
[**assignment_solutions_delete_submission**](DefaultApi.md#assignment_solutions_delete_submission) | **DELETE** /v1/assignment-solutions/submission/{submissionId} | Remove the submission permanently
[**assignment_solutions_download_result_archive**](DefaultApi.md#assignment_solutions_download_result_archive) | **GET** /v1/assignment-solutions/submission/{submissionId}/download-result | Download result archive from backend for particular submission.
[**assignment_solutions_download_solution_archive**](DefaultApi.md#assignment_solutions_download_solution_archive) | **GET** /v1/assignment-solutions/{id}/download-solution | Download archive containing all solution files for particular solution.
[**assignment_solutions_evaluation_score_config**](DefaultApi.md#assignment_solutions_evaluation_score_config) | **GET** /v1/assignment-solutions/submission/{submissionId}/score-config | Get score configuration associated with given submission evaluation
[**assignment_solutions_files**](DefaultApi.md#assignment_solutions_files) | **GET** /v1/assignment-solutions/{id}/files | Get the list of submitted files of the solution.
[**assignment_solutions_review_requests**](DefaultApi.md#assignment_solutions_review_requests) | **GET** /v1/users/{id}/review-requests | Return all solutions with reviewRequest flag that given user might need to review (is admin/supervisor in corresponding groups). Along with that it returns all assignment entities of the corresponding solutions.
[**assignment_solutions_set_bonus_points**](DefaultApi.md#assignment_solutions_set_bonus_points) | **POST** /v1/assignment-solutions/{id}/bonus-points | Set new amount of bonus points for a solution (and optionally points override) Returns array of solution entities that has been changed by this.
[**assignment_solutions_set_flag**](DefaultApi.md#assignment_solutions_set_flag) | **POST** /v1/assignment-solutions/{id}/set-flag/{flag} | Set flag of the assignment solution.
[**assignment_solutions_solution**](DefaultApi.md#assignment_solutions_solution) | **GET** /v1/assignment-solutions/{id} | Get information about solutions.
[**assignment_solutions_submission**](DefaultApi.md#assignment_solutions_submission) | **GET** /v1/assignment-solutions/submission/{submissionId} | Get information about the evaluation of a submission
[**assignment_solutions_submissions**](DefaultApi.md#assignment_solutions_submissions) | **GET** /v1/assignment-solutions/{id}/submissions | Get list of all submissions of a solution
[**assignment_solutions_update_solution**](DefaultApi.md#assignment_solutions_update_solution) | **POST** /v1/assignment-solutions/{id} | Update details about the solution (note, etc...)
[**assignment_solvers_default**](DefaultApi.md#assignment_solvers_default) | **GET** /v1/assignment-solvers | Get a list of assignment solvers based on given parameters (assignment/group and solver user). Either assignment or group ID must be set (group is ignored if assignment is set), user ID is optional.
[**assignments_best_solution**](DefaultApi.md#assignments_best_solution) | **GET** /v1/exercise-assignments/{id}/users/{userId}/best-solution | Get the best solution by a user to an assignment
[**assignments_best_solutions**](DefaultApi.md#assignments_best_solutions) | **GET** /v1/exercise-assignments/{id}/best-solutions | Get the best solutions to an assignment for all students in group.
[**assignments_create**](DefaultApi.md#assignments_create) | **POST** /v1/exercise-assignments | Assign an exercise to a group
[**assignments_detail**](DefaultApi.md#assignments_detail) | **GET** /v1/exercise-assignments/{id} | Get details of an assignment
[**assignments_download_best_solutions_archive**](DefaultApi.md#assignments_download_best_solutions_archive) | **GET** /v1/exercise-assignments/{id}/download-best-solutions | Download the best solutions of an assignment for all students in group.
[**assignments_remove**](DefaultApi.md#assignments_remove) | **DELETE** /v1/exercise-assignments/{id} | Delete an assignment
[**assignments_solutions**](DefaultApi.md#assignments_solutions) | **GET** /v1/exercise-assignments/{id}/solutions | Get a list of solutions of all users for the assignment
[**assignments_sync_with_exercise**](DefaultApi.md#assignments_sync_with_exercise) | **POST** /v1/exercise-assignments/{id}/sync-exercise | Update the assignment so that it matches with the current version of the exercise (limits, texts, etc.)
[**assignments_update_detail**](DefaultApi.md#assignments_update_detail) | **POST** /v1/exercise-assignments/{id} | Update details of an assignment
[**assignments_user_solutions**](DefaultApi.md#assignments_user_solutions) | **GET** /v1/exercise-assignments/{id}/users/{userId}/solutions | Get a list of solutions created by a user of an assignment
[**assignments_validate**](DefaultApi.md#assignments_validate) | **POST** /v1/exercise-assignments/{id}/validate | Check if the version of the assignment is up-to-date.
[**async_jobs_abort**](DefaultApi.md#async_jobs_abort) | **POST** /v1/async-jobs/{id}/abort | Retrieves details about particular async job.
[**async_jobs_assignment_jobs**](DefaultApi.md#async_jobs_assignment_jobs) | **GET** /v1/exercise-assignments/{id}/async-jobs | Get all pending async jobs related to a particular assignment.
[**async_jobs_default**](DefaultApi.md#async_jobs_default) | **GET** /v1/async-jobs/{id} | Retrieves details about particular async job.
[**async_jobs_list**](DefaultApi.md#async_jobs_list) | **GET** /v1/async-jobs | Retrieves details about async jobs that are either pending or were recently completed.
[**async_jobs_ping**](DefaultApi.md#async_jobs_ping) | **POST** /v1/async-jobs/ping | Initiates ping job. An empty job designed to verify the async handler is running.
[**broker_freeze**](DefaultApi.md#broker_freeze) | **POST** /v1/broker/freeze | Freeze broker and its execution.
[**broker_reports_error**](DefaultApi.md#broker_reports_error) | **POST** /v1/broker-reports/error | Announce a backend error that is not related to any job (meant to be called by the backend)
[**broker_reports_job_status**](DefaultApi.md#broker_reports_job_status) | **POST** /v1/broker-reports/job-status/{jobId} | Update the status of a job (meant to be called by the backend)
[**broker_stats**](DefaultApi.md#broker_stats) | **GET** /v1/broker/stats | Get current statistics from broker.
[**broker_unfreeze**](DefaultApi.md#broker_unfreeze) | **POST** /v1/broker/unfreeze | Unfreeze broker and its execution.
[**comments_add_comment**](DefaultApi.md#comments_add_comment) | **POST** /v1/comments/{id} | Add a comment to a thread
[**comments_default**](DefaultApi.md#comments_default) | **GET** /v1/comments/{id} | Get a comment thread
[**comments_delete**](DefaultApi.md#comments_delete) | **DELETE** /v1/comments/{threadId}/comment/{commentId} | Delete a comment
[**comments_set_private**](DefaultApi.md#comments_set_private) | **POST** /v1/comments/{threadId}/comment/{commentId}/private | Set the private flag of a comment
[**comments_toggle_private**](DefaultApi.md#comments_toggle_private) | **POST** /v1/comments/{threadId}/comment/{commentId}/toggle | Make a private comment public or vice versa
[**email_verification_email_verification**](DefaultApi.md#email_verification_email_verification) | **POST** /v1/email-verification/verify | Verify users email.
[**email_verification_resend_verification_email**](DefaultApi.md#email_verification_resend_verification_email) | **POST** /v1/email-verification/resend | Resend the email for the current user to verify his/her email address.
[**emails_default**](DefaultApi.md#emails_default) | **POST** /v1/emails | Sends an email with provided subject and message to all ReCodEx users.
[**emails_send_to_group_members**](DefaultApi.md#emails_send_to_group_members) | **POST** /v1/emails/groups/{groupId} | Sends an email with provided subject and message to regular members of given group and optionally to supervisors and admins.
[**emails_send_to_regular_users**](DefaultApi.md#emails_send_to_regular_users) | **POST** /v1/emails/regular-users | Sends an email with provided subject and message to all regular users.
[**emails_send_to_supervisors**](DefaultApi.md#emails_send_to_supervisors) | **POST** /v1/emails/supervisors | Sends an email with provided subject and message to all supervisors and superadmins.
[**exercise_files_delete_attachment_file**](DefaultApi.md#exercise_files_delete_attachment_file) | **DELETE** /v1/exercises/{id}/attachment-files/{fileId} | Delete attachment exercise file with given id
[**exercise_files_delete_supplementary_file**](DefaultApi.md#exercise_files_delete_supplementary_file) | **DELETE** /v1/exercises/{id}/supplementary-files/{fileId} | Delete supplementary exercise file with given id
[**exercise_files_download_attachment_files_archive**](DefaultApi.md#exercise_files_download_attachment_files_archive) | **GET** /v1/exercises/{id}/attachment-files/download-archive | Download archive containing all attachment files for exercise.
[**exercise_files_download_supplementary_files_archive**](DefaultApi.md#exercise_files_download_supplementary_files_archive) | **GET** /v1/exercises/{id}/supplementary-files/download-archive | Download archive containing all supplementary files for exercise.
[**exercise_files_get_attachment_files**](DefaultApi.md#exercise_files_get_attachment_files) | **GET** /v1/exercises/{id}/attachment-files | Get a list of all attachment files for an exercise
[**exercise_files_get_supplementary_files**](DefaultApi.md#exercise_files_get_supplementary_files) | **GET** /v1/exercises/{id}/supplementary-files | Get list of all supplementary files for an exercise
[**exercise_files_upload_attachment_files**](DefaultApi.md#exercise_files_upload_attachment_files) | **POST** /v1/exercises/{id}/attachment-files | Associate attachment exercise files with an exercise
[**exercise_files_upload_supplementary_files**](DefaultApi.md#exercise_files_upload_supplementary_files) | **POST** /v1/exercises/{id}/supplementary-files | Associate supplementary files with an exercise and upload them to remote file server
[**exercises_add_tag**](DefaultApi.md#exercises_add_tag) | **POST** /v1/exercises/{id}/tags/{name} | Add tag with given name to the exercise.
[**exercises_all_tags**](DefaultApi.md#exercises_all_tags) | **GET** /v1/exercises/tags | Get list of global exercise tag names which are currently registered.
[**exercises_assignments**](DefaultApi.md#exercises_assignments) | **GET** /v1/exercises/{id}/assignments | Get all non-archived assignments created from this exercise.
[**exercises_attach_group**](DefaultApi.md#exercises_attach_group) | **POST** /v1/exercises/{id}/groups/{groupId} | Attach exercise to group with given identification.
[**exercises_authors**](DefaultApi.md#exercises_authors) | **GET** /v1/exercises/authors | List authors of all exercises, possibly filtered by a group in which the exercises appear.
[**exercises_config_get_configuration**](DefaultApi.md#exercises_config_get_configuration) | **GET** /v1/exercises/{id}/config | Get a basic exercise high level configuration.
[**exercises_config_get_environment_configs**](DefaultApi.md#exercises_config_get_environment_configs) | **GET** /v1/exercises/{id}/environment-configs | Get runtime configurations for exercise.
[**exercises_config_get_hardware_group_limits**](DefaultApi.md#exercises_config_get_hardware_group_limits) | **GET** /v1/exercises/{id}/environment/{runtimeEnvironmentId}/hwgroup/{hwGroupId}/limits | Get a description of resource limits for an exercise for given hwgroup.
[**exercises_config_get_limits**](DefaultApi.md#exercises_config_get_limits) | **GET** /v1/exercises/{id}/limits | Get a description of resource limits for given exercise (all hwgroups all environments).
[**exercises_config_get_score_config**](DefaultApi.md#exercises_config_get_score_config) | **GET** /v1/exercises/{id}/score-config | Get score configuration for exercise based on given identification.
[**exercises_config_get_tests**](DefaultApi.md#exercises_config_get_tests) | **GET** /v1/exercises/{id}/tests | Get tests for exercise based on given identification.
[**exercises_config_get_variables_for_exercise_config**](DefaultApi.md#exercises_config_get_variables_for_exercise_config) | **POST** /v1/exercises/{id}/config/variables | Get variables for exercise configuration which are derived from given pipelines and runtime environment.
[**exercises_config_remove_hardware_group_limits**](DefaultApi.md#exercises_config_remove_hardware_group_limits) | **DELETE** /v1/exercises/{id}/environment/{runtimeEnvironmentId}/hwgroup/{hwGroupId}/limits | Remove resource limits of given hwgroup from an exercise.
[**exercises_config_set_configuration**](DefaultApi.md#exercises_config_set_configuration) | **POST** /v1/exercises/{id}/config | Set basic exercise configuration
[**exercises_config_set_hardware_group_limits**](DefaultApi.md#exercises_config_set_hardware_group_limits) | **POST** /v1/exercises/{id}/environment/{runtimeEnvironmentId}/hwgroup/{hwGroupId}/limits | Set resource limits for an exercise for given hwgroup.
[**exercises_config_set_limits**](DefaultApi.md#exercises_config_set_limits) | **POST** /v1/exercises/{id}/limits | Update resource limits for given exercise. If limits for particular hwGroup or environment are not posted, no change occurs. If limits for particular hwGroup or environment are posted as null, they are removed.
[**exercises_config_set_score_config**](DefaultApi.md#exercises_config_set_score_config) | **POST** /v1/exercises/{id}/score-config | Set score configuration for exercise.
[**exercises_config_set_tests**](DefaultApi.md#exercises_config_set_tests) | **POST** /v1/exercises/{id}/tests | Set tests for exercise based on given identification.
[**exercises_config_update_environment_configs**](DefaultApi.md#exercises_config_update_environment_configs) | **POST** /v1/exercises/{id}/environment-configs | Change runtime configuration of exercise. Configurations can be added or deleted here, based on what is provided in arguments.
[**exercises_create**](DefaultApi.md#exercises_create) | **POST** /v1/exercises | Create exercise with all default values. Exercise detail can be then changed in appropriate endpoint.
[**exercises_default**](DefaultApi.md#exercises_default) | **GET** /v1/exercises | Get a list of all exercises matching given filters in given pagination rage. The result conforms to pagination protocol.
[**exercises_detach_group**](DefaultApi.md#exercises_detach_group) | **DELETE** /v1/exercises/{id}/groups/{groupId} | Detach exercise from given group.
[**exercises_detail**](DefaultApi.md#exercises_detail) | **GET** /v1/exercises/{id} | Get details of an exercise
[**exercises_fork_from**](DefaultApi.md#exercises_fork_from) | **POST** /v1/exercises/{id}/fork | Fork exercise from given one into the completely new one.
[**exercises_hardware_groups**](DefaultApi.md#exercises_hardware_groups) | **POST** /v1/exercises/{id}/hardware-groups | Set hardware groups which are associated with exercise.
[**exercises_list_by_ids**](DefaultApi.md#exercises_list_by_ids) | **POST** /v1/exercises/list | Get a list of exercises based on given ids.
[**exercises_remove**](DefaultApi.md#exercises_remove) | **DELETE** /v1/exercises/{id} | Delete an exercise
[**exercises_remove_tag**](DefaultApi.md#exercises_remove_tag) | **DELETE** /v1/exercises/{id}/tags/{name} | Remove tag with given name from exercise.
[**exercises_send_notification**](DefaultApi.md#exercises_send_notification) | **POST** /v1/exercises/{id}/notification | Sends an email to all group admins and supervisors, where the exercise is assigned. The purpose of this is to quickly notify all relevant teachers when a bug is found or the exercise is modified significantly. The response is number of emails sent (number of notified users).
[**exercises_set_admins**](DefaultApi.md#exercises_set_admins) | **POST** /v1/exercises/{id}/admins | Change who the admins of an exercise are (all users on the list are added, prior admins not on the list are removed).
[**exercises_set_archived**](DefaultApi.md#exercises_set_archived) | **POST** /v1/exercises/{id}/archived | (Un)mark the exercise as archived. Nothing happens if the exercise is already in the requested state.
[**exercises_set_author**](DefaultApi.md#exercises_set_author) | **POST** /v1/exercises/{id}/author | Change the author of the exercise. This is a very special operation reserved for powerful users.
[**exercises_tags_stats**](DefaultApi.md#exercises_tags_stats) | **GET** /v1/exercises/tags-stats | Get list of global exercise tag names along with how many times they have been used.
[**exercises_tags_update_global**](DefaultApi.md#exercises_tags_update_global) | **POST** /v1/exercises/tags/{tag} | Update the tag globally. At the moment, the only &#x27;update&#x27; function is &#x27;rename&#x27;. Other types of updates may be implemented in the future.
[**exercises_update_detail**](DefaultApi.md#exercises_update_detail) | **POST** /v1/exercises/{id} | Update detail of an exercise
[**exercises_validate**](DefaultApi.md#exercises_validate) | **POST** /v1/exercises/{id}/validate | Check if the version of the exercise is up-to-date.
[**extensions_token**](DefaultApi.md#extensions_token) | **POST** /v1/extensions/{extId} | This endpoint is used by a backend of an extension to get a proper access token (from a temp token passed via URL). It also returns details about authenticated user.
[**extensions_url**](DefaultApi.md#extensions_url) | **GET** /v1/extensions/{extId}/{instanceId} | Return URL refering to the extension with properly injected temporary JWT token.
[**forgotten_password_change**](DefaultApi.md#forgotten_password_change) | **POST** /v1/forgotten-password/change | Change the user&#x27;s password
[**forgotten_password_default**](DefaultApi.md#forgotten_password_default) | **POST** /v1/forgotten-password | Request a password reset (user will receive an e-mail that prompts them to reset their password)
[**forgotten_password_validate_password_strength**](DefaultApi.md#forgotten_password_validate_password_strength) | **POST** /v1/forgotten-password/validate-password-strength | Check if a password is strong enough
[**group_external_attributes_add**](DefaultApi.md#group_external_attributes_add) | **POST** /v1/group-attributes/{groupId} | Create an external attribute for given group.
[**group_external_attributes_default**](DefaultApi.md#group_external_attributes_default) | **GET** /v1/group-attributes | Return all attributes that correspond to given filtering parameters.
[**group_external_attributes_remove**](DefaultApi.md#group_external_attributes_remove) | **DELETE** /v1/group-attributes/{id} | Remove selected attribute
[**group_invitations_accept**](DefaultApi.md#group_invitations_accept) | **POST** /v1/group-invitations/{id}/accept | Allow the current user to join the corresponding group using the invitation.
[**group_invitations_create**](DefaultApi.md#group_invitations_create) | **POST** /v1/groups/{groupId}/invitations | Create a new invitation for given group.
[**group_invitations_default**](DefaultApi.md#group_invitations_default) | **GET** /v1/group-invitations/{id} | Return invitation details including all relevant group entities (so a name can be constructed).
[**group_invitations_list**](DefaultApi.md#group_invitations_list) | **GET** /v1/groups/{groupId}/invitations | List all invitations of a group.
[**group_invitations_remove**](DefaultApi.md#group_invitations_remove) | **DELETE** /v1/group-invitations/{id} | 
[**group_invitations_update**](DefaultApi.md#group_invitations_update) | **POST** /v1/group-invitations/{id} | Edit the invitation.
[**groups_add_group**](DefaultApi.md#groups_add_group) | **POST** /v1/groups | Create a new group
[**groups_add_member**](DefaultApi.md#groups_add_member) | **POST** /v1/groups/{id}/members/{userId} | Add/update a membership (other than student) for given user
[**groups_add_student**](DefaultApi.md#groups_add_student) | **POST** /v1/groups/{id}/students/{userId} | Add a student to a group
[**groups_assignments**](DefaultApi.md#groups_assignments) | **GET** /v1/groups/{id}/assignments | Get all exercise assignments for a group
[**groups_default**](DefaultApi.md#groups_default) | **GET** /v1/groups | Get a list of all non-archived groups a user can see. The return set is filtered by parameters.
[**groups_detail**](DefaultApi.md#groups_detail) | **GET** /v1/groups/{id} | Get details of a group
[**groups_get_exam_locks**](DefaultApi.md#groups_get_exam_locks) | **GET** /v1/groups/{id}/exam/{examId} | Retrieve a list of locks for given exam
[**groups_lock_student**](DefaultApi.md#groups_lock_student) | **POST** /v1/groups/{id}/lock/{userId} | Lock student in a group and with an IP from which the request was made.
[**groups_members**](DefaultApi.md#groups_members) | **GET** /v1/groups/{id}/members | Get a list of members of a group
[**groups_relocate**](DefaultApi.md#groups_relocate) | **POST** /v1/groups/{id}/relocate/{newParentId} | Relocate the group under a different parent.
[**groups_remove_exam_period**](DefaultApi.md#groups_remove_exam_period) | **DELETE** /v1/groups/{id}/examPeriod | Change the group back to regular group (remove information about an exam).
[**groups_remove_group**](DefaultApi.md#groups_remove_group) | **DELETE** /v1/groups/{id} | Delete a group
[**groups_remove_member**](DefaultApi.md#groups_remove_member) | **DELETE** /v1/groups/{id}/members/{userId} | Remove a member (other than student) from a group
[**groups_remove_student**](DefaultApi.md#groups_remove_student) | **DELETE** /v1/groups/{id}/students/{userId} | Remove a student from a group
[**groups_set_archived**](DefaultApi.md#groups_set_archived) | **POST** /v1/groups/{id}/archived | Set the &#x27;isArchived&#x27; flag for a group
[**groups_set_exam_period**](DefaultApi.md#groups_set_exam_period) | **POST** /v1/groups/{id}/examPeriod | Set an examination period (in the future) when the group will be secured for submitting. Only locked students may submit solutions in the group during this period. This endpoint is also used to update already planned exam period, but only dates in the future can be editted (e.g., once an exam begins, the beginning may no longer be updated).
[**groups_set_organizational**](DefaultApi.md#groups_set_organizational) | **POST** /v1/groups/{id}/organizational | Set the &#x27;isOrganizational&#x27; flag for a group
[**groups_shadow_assignments**](DefaultApi.md#groups_shadow_assignments) | **GET** /v1/groups/{id}/shadow-assignments | Get all shadow assignments for a group
[**groups_stats**](DefaultApi.md#groups_stats) | **GET** /v1/groups/{id}/students/stats | Get statistics of a group. If the user does not have the rights to view all of these, try to at least return their statistics.
[**groups_students_solutions**](DefaultApi.md#groups_students_solutions) | **GET** /v1/groups/{id}/students/{userId}/solutions | Get all solutions of a single student from all assignments in a group
[**groups_students_stats**](DefaultApi.md#groups_students_stats) | **GET** /v1/groups/{id}/students/{userId} | Get statistics of a single student in a group
[**groups_subgroups**](DefaultApi.md#groups_subgroups) | **GET** /v1/groups/{id}/subgroups | Get a list of subgroups of a group
[**groups_unlock_student**](DefaultApi.md#groups_unlock_student) | **DELETE** /v1/groups/{id}/lock/{userId} | Unlock a student currently locked in a group.
[**groups_update_group**](DefaultApi.md#groups_update_group) | **POST** /v1/groups/{id} | Update group info
[**groups_validate_add_group_data**](DefaultApi.md#groups_validate_add_group_data) | **POST** /v1/groups/validate-add-group-data | Validate group creation data
[**hardware_groups_default**](DefaultApi.md#hardware_groups_default) | **GET** /v1/hardware-groups | Get a list of all hardware groups in system
[**instances_create_instance**](DefaultApi.md#instances_create_instance) | **POST** /v1/instances | Create a new instance
[**instances_create_licence**](DefaultApi.md#instances_create_licence) | **POST** /v1/instances/{id}/licences | Create a new license for an instance
[**instances_default**](DefaultApi.md#instances_default) | **GET** /v1/instances | Get a list of all instances
[**instances_delete_instance**](DefaultApi.md#instances_delete_instance) | **DELETE** /v1/instances/{id} | Delete an instance
[**instances_delete_licence**](DefaultApi.md#instances_delete_licence) | **DELETE** /v1/instances/licences/{licenceId} | Remove existing license for an instance
[**instances_detail**](DefaultApi.md#instances_detail) | **GET** /v1/instances/{id} | Get details of an instance
[**instances_licences**](DefaultApi.md#instances_licences) | **GET** /v1/instances/{id}/licences | Get a list of licenses associated with an instance
[**instances_update_instance**](DefaultApi.md#instances_update_instance) | **POST** /v1/instances/{id} | Update an instance
[**instances_update_licence**](DefaultApi.md#instances_update_licence) | **POST** /v1/instances/licences/{licenceId} | Update an existing license for an instance
[**login_default**](DefaultApi.md#login_default) | **POST** /v1/login | Log in using user credentials
[**login_external**](DefaultApi.md#login_external) | **POST** /v1/login/{authenticatorName} | Log in using an external authentication service
[**login_issue_restricted_token**](DefaultApi.md#login_issue_restricted_token) | **POST** /v1/login/issue-restricted-token | Issue a new access token with a restricted set of scopes
[**login_refresh**](DefaultApi.md#login_refresh) | **GET** /v1/login/refresh | Refresh the access token of current user
[**login_take_over**](DefaultApi.md#login_take_over) | **POST** /v1/login/takeover/{userId} | Takeover user account with specified user identification.
[**notifications_all**](DefaultApi.md#notifications_all) | **GET** /v1/notifications/all | Get all notifications in the system.
[**notifications_create**](DefaultApi.md#notifications_create) | **POST** /v1/notifications | Create notification with given attributes
[**notifications_default**](DefaultApi.md#notifications_default) | **GET** /v1/notifications | Get all notifications which are currently active. If groupsIds is given returns only the ones from given groups (and their ancestors) and global ones (without group).
[**notifications_remove**](DefaultApi.md#notifications_remove) | **DELETE** /v1/notifications/{id} | Delete a notification
[**notifications_update**](DefaultApi.md#notifications_update) | **POST** /v1/notifications/{id} | Update notification
[**pipelines_create_pipeline**](DefaultApi.md#pipelines_create_pipeline) | **POST** /v1/pipelines | Create a brand new pipeline.
[**pipelines_default**](DefaultApi.md#pipelines_default) | **GET** /v1/pipelines | Get a list of pipelines with an optional filter, ordering, and pagination pruning. The result conforms to pagination protocol.
[**pipelines_delete_supplementary_file**](DefaultApi.md#pipelines_delete_supplementary_file) | **DELETE** /v1/pipelines/{id}/supplementary-files/{fileId} | Delete supplementary pipeline file with given id
[**pipelines_fork_pipeline**](DefaultApi.md#pipelines_fork_pipeline) | **POST** /v1/pipelines/{id}/fork | Create a complete copy of given pipeline.
[**pipelines_get_default_boxes**](DefaultApi.md#pipelines_get_default_boxes) | **GET** /v1/pipelines/boxes | Get a list of default boxes which might be used in pipeline.
[**pipelines_get_pipeline**](DefaultApi.md#pipelines_get_pipeline) | **GET** /v1/pipelines/{id} | Get pipeline based on given identification.
[**pipelines_get_pipeline_exercises**](DefaultApi.md#pipelines_get_pipeline_exercises) | **GET** /v1/pipelines/{id}/exercises | Get all exercises that use given pipeline. Only bare minimum is retrieved for each exercise (localized name and author).
[**pipelines_get_supplementary_files**](DefaultApi.md#pipelines_get_supplementary_files) | **GET** /v1/pipelines/{id}/supplementary-files | Get list of all supplementary files for a pipeline
[**pipelines_remove_pipeline**](DefaultApi.md#pipelines_remove_pipeline) | **DELETE** /v1/pipelines/{id} | Delete an pipeline
[**pipelines_update_pipeline**](DefaultApi.md#pipelines_update_pipeline) | **POST** /v1/pipelines/{id} | Update pipeline with given data.
[**pipelines_update_runtime_environments**](DefaultApi.md#pipelines_update_runtime_environments) | **POST** /v1/pipelines/{id}/runtime-environments | Set runtime environments associated with given pipeline.
[**pipelines_upload_supplementary_files**](DefaultApi.md#pipelines_upload_supplementary_files) | **POST** /v1/pipelines/{id}/supplementary-files | Associate supplementary files with a pipeline and upload them to remote file server
[**pipelines_validate_pipeline**](DefaultApi.md#pipelines_validate_pipeline) | **POST** /v1/pipelines/{id}/validate | Check if the version of the pipeline is up-to-date.
[**plagiarism_add_similarities**](DefaultApi.md#plagiarism_add_similarities) | **POST** /v1/plagiarism/{id}/{solutionId} | Appends one detected similarity record (similarities associated with one file and one other author) into a detected batch. This division was selected to make the appends relatively small and managable.
[**plagiarism_batch_detail**](DefaultApi.md#plagiarism_batch_detail) | **GET** /v1/plagiarism/{id} | Fetch a detail of a particular batch record.
[**plagiarism_create_batch**](DefaultApi.md#plagiarism_create_batch) | **POST** /v1/plagiarism | Create new detection batch record
[**plagiarism_get_similarities**](DefaultApi.md#plagiarism_get_similarities) | **GET** /v1/plagiarism/{id}/{solutionId} | Retrieve detected plagiarism records from a specific batch related to one solution. Returns a list of detected similarities entities (similar file records are nested within).
[**plagiarism_list_batches**](DefaultApi.md#plagiarism_list_batches) | **GET** /v1/plagiarism | Get a list of all batches, optionally filtered by query params.
[**plagiarism_update_batch**](DefaultApi.md#plagiarism_update_batch) | **POST** /v1/plagiarism/{id} | Update dectection bath record. At the momeny, only the uploadCompletedAt can be changed.
[**reference_exercise_solutions_delete_reference_solution**](DefaultApi.md#reference_exercise_solutions_delete_reference_solution) | **DELETE** /v1/reference-solutions/{solutionId} | Delete reference solution with given identification.
[**reference_exercise_solutions_delete_submission**](DefaultApi.md#reference_exercise_solutions_delete_submission) | **DELETE** /v1/reference-solutions/submission/{submissionId} | Remove reference solution evaluation (submission) permanently.
[**reference_exercise_solutions_detail**](DefaultApi.md#reference_exercise_solutions_detail) | **GET** /v1/reference-solutions/{solutionId} | Get details of a reference solution
[**reference_exercise_solutions_download_result_archive**](DefaultApi.md#reference_exercise_solutions_download_result_archive) | **GET** /v1/reference-solutions/submission/{submissionId}/download-result | Download result archive from backend for a reference solution evaluation
[**reference_exercise_solutions_download_solution_archive**](DefaultApi.md#reference_exercise_solutions_download_solution_archive) | **GET** /v1/reference-solutions/{solutionId}/download-solution | Download archive containing all solution files for particular reference solution.
[**reference_exercise_solutions_evaluation_score_config**](DefaultApi.md#reference_exercise_solutions_evaluation_score_config) | **GET** /v1/reference-solutions/submission/{submissionId}/score-config | Get score configuration associated with given submission evaluation
[**reference_exercise_solutions_files**](DefaultApi.md#reference_exercise_solutions_files) | **GET** /v1/reference-solutions/{id}/files | Get the list of submitted files of the solution.
[**reference_exercise_solutions_pre_submit**](DefaultApi.md#reference_exercise_solutions_pre_submit) | **POST** /v1/reference-solutions/exercise/{exerciseId}/pre-submit | Pre submit action which will, based on given files, detect possible runtime environments for the exercise. Also it can be further used for entry points and other important things that should be provided by user during submit.
[**reference_exercise_solutions_resubmit**](DefaultApi.md#reference_exercise_solutions_resubmit) | **POST** /v1/reference-solutions/{id}/resubmit | Evaluate a single reference exercise solution for all configured hardware groups
[**reference_exercise_solutions_resubmit_all**](DefaultApi.md#reference_exercise_solutions_resubmit_all) | **POST** /v1/reference-solutions/exercise/{exerciseId}/resubmit-all | Evaluate all reference solutions for an exercise (and for all configured hardware groups).
[**reference_exercise_solutions_set_visibility**](DefaultApi.md#reference_exercise_solutions_set_visibility) | **POST** /v1/reference-solutions/{solutionId}/visibility | Set visibility of given reference solution.
[**reference_exercise_solutions_solutions**](DefaultApi.md#reference_exercise_solutions_solutions) | **GET** /v1/reference-solutions/exercise/{exerciseId} | Get reference solutions for an exercise
[**reference_exercise_solutions_submission**](DefaultApi.md#reference_exercise_solutions_submission) | **GET** /v1/reference-solutions/submission/{submissionId} | Get reference solution evaluation (i.e., submission) for an exercise solution.
[**reference_exercise_solutions_submissions**](DefaultApi.md#reference_exercise_solutions_submissions) | **GET** /v1/reference-solutions/{solutionId}/submissions | Get a list of submissions for given reference solution.
[**reference_exercise_solutions_submit**](DefaultApi.md#reference_exercise_solutions_submit) | **POST** /v1/reference-solutions/exercise/{exerciseId}/submit | Add new reference solution to an exercise
[**reference_exercise_solutions_update**](DefaultApi.md#reference_exercise_solutions_update) | **POST** /v1/reference-solutions/{solutionId} | Update details about the ref. solution (note, etc...)
[**registration_accept_invitation**](DefaultApi.md#registration_accept_invitation) | **POST** /v1/users/accept-invitation | Accept invitation and create corresponding user account.
[**registration_create_account**](DefaultApi.md#registration_create_account) | **POST** /v1/users | Create a user account
[**registration_create_invitation**](DefaultApi.md#registration_create_invitation) | **POST** /v1/users/invite | Create an invitation for a user and send it over via email
[**registration_debug**](DefaultApi.md#registration_debug) | **POST** /v1/users/debug/{param} | Debug endpoint.
[**registration_validate_registration_data**](DefaultApi.md#registration_validate_registration_data) | **POST** /v1/users/validate-registration-data | Check if the registered E-mail isn&#x27;t already used and if the password is strong enough
[**runtime_environments_default**](DefaultApi.md#runtime_environments_default) | **GET** /v1/runtime-environments | Get a list of all runtime environments
[**security_check**](DefaultApi.md#security_check) | **POST** /v1/security/check | 
[**shadow_assignments_create**](DefaultApi.md#shadow_assignments_create) | **POST** /v1/shadow-assignments | Create new shadow assignment in given group.
[**shadow_assignments_create_points**](DefaultApi.md#shadow_assignments_create_points) | **POST** /v1/shadow-assignments/{id}/create-points | Create new points for shadow assignment and user.
[**shadow_assignments_detail**](DefaultApi.md#shadow_assignments_detail) | **GET** /v1/shadow-assignments/{id} | Get details of a shadow assignment
[**shadow_assignments_remove**](DefaultApi.md#shadow_assignments_remove) | **DELETE** /v1/shadow-assignments/{id} | Delete shadow assignment
[**shadow_assignments_remove_points**](DefaultApi.md#shadow_assignments_remove_points) | **DELETE** /v1/shadow-assignments/points/{pointsId} | Remove points of shadow assignment.
[**shadow_assignments_update_detail**](DefaultApi.md#shadow_assignments_update_detail) | **POST** /v1/shadow-assignments/{id} | Update details of an shadow assignment
[**shadow_assignments_update_points**](DefaultApi.md#shadow_assignments_update_points) | **POST** /v1/shadow-assignments/points/{pointsId} | Update detail of shadow assignment points.
[**shadow_assignments_validate**](DefaultApi.md#shadow_assignments_validate) | **POST** /v1/shadow-assignments/{id}/validate | Check if the version of the shadow assignment is up-to-date.
[**sis_bind_group**](DefaultApi.md#sis_bind_group) | **POST** /v1/extensions/sis/remote-courses/{courseId}/bind | Bind an existing local group to a SIS group
[**sis_create_group**](DefaultApi.md#sis_create_group) | **POST** /v1/extensions/sis/remote-courses/{courseId}/create | Create a new group based on a SIS group
[**sis_delete_term**](DefaultApi.md#sis_delete_term) | **DELETE** /v1/extensions/sis/terms/{id} | Delete a term
[**sis_edit_term**](DefaultApi.md#sis_edit_term) | **POST** /v1/extensions/sis/terms/{id} | Set details of a term
[**sis_get_terms**](DefaultApi.md#sis_get_terms) | **GET** /v1/extensions/sis/terms/ | Get a list of all registered SIS terms
[**sis_possible_parents**](DefaultApi.md#sis_possible_parents) | **GET** /v1/extensions/sis/remote-courses/{courseId}/possible-parents | Find groups that can be chosen as parents of a group created from given SIS group by current user
[**sis_register_term**](DefaultApi.md#sis_register_term) | **POST** /v1/extensions/sis/terms/ | Register a new term
[**sis_status**](DefaultApi.md#sis_status) | **GET** /v1/extensions/sis/status/ | 
[**sis_subscribed_courses**](DefaultApi.md#sis_subscribed_courses) | **GET** /v1/extensions/sis/users/{userId}/subscribed-groups/{year}/{term}/as-student | Get all courses subscirbed by a student and corresponding ReCodEx groups. Organizational and archived groups are filtered out from the result. Each course holds bound group IDs and group objects are returned in a separate array. Whole ancestral closure of groups is returned, so the webapp may properly assemble hiarichial group names.
[**sis_supervised_courses**](DefaultApi.md#sis_supervised_courses) | **GET** /v1/extensions/sis/users/{userId}/supervised-courses/{year}/{term} | Get supervised SIS courses and corresponding ReCodEx groups. Each course holds bound group IDs and group objects are returned in a separate array. Whole ancestral closure of groups is returned, so the webapp may properly assemble hiarichial group names.
[**sis_unbind_group**](DefaultApi.md#sis_unbind_group) | **DELETE** /v1/extensions/sis/remote-courses/{courseId}/bindings/{groupId} | Delete a binding between a local group and a SIS group
[**submission_failures_default**](DefaultApi.md#submission_failures_default) | **GET** /v1/submission-failures | List all submission failures, ever
[**submission_failures_detail**](DefaultApi.md#submission_failures_detail) | **GET** /v1/submission-failures/{id} | Get details of a failure
[**submission_failures_resolve**](DefaultApi.md#submission_failures_resolve) | **POST** /v1/submission-failures/{id}/resolve | Mark a submission failure as resolved
[**submission_failures_unresolved**](DefaultApi.md#submission_failures_unresolved) | **GET** /v1/submission-failures/unresolved | List all unresolved submission failures
[**submit_can_submit**](DefaultApi.md#submit_can_submit) | **GET** /v1/exercise-assignments/{id}/can-submit | Check if the given user can submit solutions to the assignment
[**submit_pre_submit**](DefaultApi.md#submit_pre_submit) | **POST** /v1/exercise-assignments/{id}/pre-submit | Pre submit action which will, based on given files, detect possible runtime environments for the assignment. Also it can be further used for entry points and other important things that should be provided by user during submit.
[**submit_resubmit**](DefaultApi.md#submit_resubmit) | **POST** /v1/assignment-solutions/{id}/resubmit | Resubmit a solution (i.e., create a new submission)
[**submit_resubmit_all**](DefaultApi.md#submit_resubmit_all) | **POST** /v1/exercise-assignments/{id}/resubmit-all | Start async job that resubmits all submissions of an assignment. No job is started when there are pending resubmit jobs for the selected assignment. Returns list of pending async jobs (same as GET call)
[**submit_resubmit_all_async_job_status**](DefaultApi.md#submit_resubmit_all_async_job_status) | **GET** /v1/exercise-assignments/{id}/resubmit-all | Return a list of all pending resubmit async jobs associated with given assignment. Under normal circumstances, the list shoul be either empty, or contian only one job.
[**submit_submit**](DefaultApi.md#submit_submit) | **POST** /v1/exercise-assignments/{id}/submit | Submit a solution of an assignment
[**uploaded_files_append_partial**](DefaultApi.md#uploaded_files_append_partial) | **PUT** /v1/uploaded-files/partial/{id} | Add another chunk to partial upload.
[**uploaded_files_cancel_partial**](DefaultApi.md#uploaded_files_cancel_partial) | **DELETE** /v1/uploaded-files/partial/{id} | Cancel partial upload and remove all uploaded chunks.
[**uploaded_files_complete_partial**](DefaultApi.md#uploaded_files_complete_partial) | **POST** /v1/uploaded-files/partial/{id} | Finalize partial upload and convert the partial file into UploadFile. All data chunks are extracted from the store, assembled into one file, and is moved back into the store.
[**uploaded_files_content**](DefaultApi.md#uploaded_files_content) | **GET** /v1/uploaded-files/{id}/content | Get the contents of a file
[**uploaded_files_detail**](DefaultApi.md#uploaded_files_detail) | **GET** /v1/uploaded-files/{id} | Get details of a file
[**uploaded_files_digest**](DefaultApi.md#uploaded_files_digest) | **GET** /v1/uploaded-files/{id}/digest | Compute a digest using a hashing algorithm. This feature is intended for upload checksums only. In the future, we might want to add algorithm selection via query parameter (default is SHA1).
[**uploaded_files_download**](DefaultApi.md#uploaded_files_download) | **GET** /v1/uploaded-files/{id}/download | Download a file
[**uploaded_files_download_supplementary_file**](DefaultApi.md#uploaded_files_download_supplementary_file) | **GET** /v1/uploaded-files/supplementary-file/{id}/download | Download supplementary file
[**uploaded_files_start_partial**](DefaultApi.md#uploaded_files_start_partial) | **POST** /v1/uploaded-files/partial | Start new upload per-partes. This process expects the file is uploaded as a sequence of PUT requests, each one carrying a chunk of data. Once all the chunks are in place, the complete request assembles them together in one file and transforms UploadPartialFile into UploadFile entity.
[**uploaded_files_upload**](DefaultApi.md#uploaded_files_upload) | **POST** /v1/uploaded-files | Upload a file
[**user_calendars_create_calendar**](DefaultApi.md#user_calendars_create_calendar) | **POST** /v1/users/{id}/calendar-tokens | Create new iCal token for a particular user.
[**user_calendars_default**](DefaultApi.md#user_calendars_default) | **GET** /v1/users/ical/{id} | Get calendar values in iCal format that correspond to given token.
[**user_calendars_expire_calendar**](DefaultApi.md#user_calendars_expire_calendar) | **DELETE** /v1/users/ical/{id} | Set given iCal token to expired state. Expired tokens cannot be used to retrieve calendars.
[**user_calendars_user_calendars**](DefaultApi.md#user_calendars_user_calendars) | **GET** /v1/users/{id}/calendar-tokens | Get all iCal tokens of one user (including expired ones).
[**users_all_groups**](DefaultApi.md#users_all_groups) | **GET** /v1/users/{id}/groups/all | Get a list of all groups for a user
[**users_create_local_account**](DefaultApi.md#users_create_local_account) | **POST** /v1/users/{id}/create-local | If user is registered externally, add local account as another login method. Created password is empty and has to be changed in order to use it.
[**users_default**](DefaultApi.md#users_default) | **GET** /v1/users | Get a list of all users matching given filters in given pagination rage. The result conforms to pagination protocol.
[**users_delete**](DefaultApi.md#users_delete) | **DELETE** /v1/users/{id} | Delete a user account
[**users_detail**](DefaultApi.md#users_detail) | **GET** /v1/users/{id} | Get details of a user account
[**users_groups**](DefaultApi.md#users_groups) | **GET** /v1/users/{id}/groups | Get a list of non-archived groups for a user
[**users_instances**](DefaultApi.md#users_instances) | **GET** /v1/users/{id}/instances | Get a list of instances where a user is registered
[**users_invalidate_tokens**](DefaultApi.md#users_invalidate_tokens) | **POST** /v1/users/{id}/invalidate-tokens | Invalidate all existing tokens issued for given user
[**users_list_by_ids**](DefaultApi.md#users_list_by_ids) | **POST** /v1/users/list | Get a list of users based on given ids.
[**users_remove_external_login**](DefaultApi.md#users_remove_external_login) | **DELETE** /v1/users/{id}/external-login/{service} | Remove external ID of given authentication service.
[**users_set_role**](DefaultApi.md#users_set_role) | **POST** /v1/users/{id}/role | Set a given role to the given user.
[**users_update_external_login**](DefaultApi.md#users_update_external_login) | **POST** /v1/users/{id}/external-login/{service} | Add or update existing external ID of given authentication service.
[**users_update_profile**](DefaultApi.md#users_update_profile) | **POST** /v1/users/{id} | Update the profile associated with a user account
[**users_update_settings**](DefaultApi.md#users_update_settings) | **POST** /v1/users/{id}/settings | Update the profile settings
[**users_update_ui_data**](DefaultApi.md#users_update_ui_data) | **POST** /v1/users/{id}/ui-data | Update the user-specific structured UI data
[**worker_files_download_supplementary_file**](DefaultApi.md#worker_files_download_supplementary_file) | **GET** /v1/worker-files/supplementary-file/{hash} | Sends over an exercise supplementary file (a data file required by the tests).

# **assignment_solution_reviews_default**
> assignment_solution_reviews_default(id)

Get detail of the solution and a list of review comments.

Get detail of the solution and a list of review comments.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | identifier of the solution

try:
    # Get detail of the solution and a list of review comments.
    api_instance.assignment_solution_reviews_default(id)
except ApiException as e:
    print("Exception when calling DefaultApi->assignment_solution_reviews_default: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of the solution | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assignment_solution_reviews_delete_comment**
> assignment_solution_reviews_delete_comment(id, comment_id)

Remove one comment from a review.

Remove one comment from a review.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | identifier of the solution
comment_id = 'comment_id_example' # str | identifier of the review comment

try:
    # Remove one comment from a review.
    api_instance.assignment_solution_reviews_delete_comment(id, comment_id)
except ApiException as e:
    print("Exception when calling DefaultApi->assignment_solution_reviews_delete_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of the solution | 
 **comment_id** | **str**| identifier of the review comment | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assignment_solution_reviews_edit_comment**
> assignment_solution_reviews_edit_comment(id, comment_id, body=body)

Update existing comment within a review.

Update existing comment within a review.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | identifier of the solution
comment_id = 'comment_id_example' # str | identifier of the review comment
body = swagger_client.ReviewcommentCommentIdBody() # ReviewcommentCommentIdBody |  (optional)

try:
    # Update existing comment within a review.
    api_instance.assignment_solution_reviews_edit_comment(id, comment_id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->assignment_solution_reviews_edit_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of the solution | 
 **comment_id** | **str**| identifier of the review comment | 
 **body** | [**ReviewcommentCommentIdBody**](ReviewcommentCommentIdBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assignment_solution_reviews_new_comment**
> assignment_solution_reviews_new_comment(id, body=body)

Create a new comment within a review.

Create a new comment within a review.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | identifier of the solution
body = swagger_client.IdReviewcommentBody() # IdReviewcommentBody |  (optional)

try:
    # Create a new comment within a review.
    api_instance.assignment_solution_reviews_new_comment(id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->assignment_solution_reviews_new_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of the solution | 
 **body** | [**IdReviewcommentBody**](IdReviewcommentBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assignment_solution_reviews_pending**
> assignment_solution_reviews_pending(id)

Return all solutions with pending reviews that given user teaches (is admin/supervisor in corresponding groups). Along with that it returns all assignment entities of the corresponding solutions.

Return all solutions with pending reviews that given user teaches (is admin/supervisor in corresponding groups). Along with that it returns all assignment entities of the corresponding solutions.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | of the user whose pending reviews are listed

try:
    # Return all solutions with pending reviews that given user teaches (is admin/supervisor in corresponding groups). Along with that it returns all assignment entities of the corresponding solutions.
    api_instance.assignment_solution_reviews_pending(id)
except ApiException as e:
    print("Exception when calling DefaultApi->assignment_solution_reviews_pending: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| of the user whose pending reviews are listed | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assignment_solution_reviews_remove**
> assignment_solution_reviews_remove(id)

Update the state of the review process of the solution.

Update the state of the review process of the solution.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | identifier of the solution

try:
    # Update the state of the review process of the solution.
    api_instance.assignment_solution_reviews_remove(id)
except ApiException as e:
    print("Exception when calling DefaultApi->assignment_solution_reviews_remove: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of the solution | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assignment_solution_reviews_update**
> assignment_solution_reviews_update(id, body=body)

Update the state of the review process of the solution.

Update the state of the review process of the solution.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | identifier of the solution
body = swagger_client.IdReviewBody() # IdReviewBody |  (optional)

try:
    # Update the state of the review process of the solution.
    api_instance.assignment_solution_reviews_update(id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->assignment_solution_reviews_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of the solution | 
 **body** | [**IdReviewBody**](IdReviewBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assignment_solutions_delete_solution**
> assignment_solutions_delete_solution(id)

Delete assignment solution with given identification.

Delete assignment solution with given identification.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | identifier of assignment solution

try:
    # Delete assignment solution with given identification.
    api_instance.assignment_solutions_delete_solution(id)
except ApiException as e:
    print("Exception when calling DefaultApi->assignment_solutions_delete_solution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of assignment solution | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assignment_solutions_delete_submission**
> assignment_solutions_delete_submission(submission_id)

Remove the submission permanently

Remove the submission permanently

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
submission_id = 'submission_id_example' # str | Identifier of the submission

try:
    # Remove the submission permanently
    api_instance.assignment_solutions_delete_submission(submission_id)
except ApiException as e:
    print("Exception when calling DefaultApi->assignment_solutions_delete_submission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submission_id** | **str**| Identifier of the submission | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assignment_solutions_download_result_archive**
> assignment_solutions_download_result_archive(submission_id)

Download result archive from backend for particular submission.

Download result archive from backend for particular submission.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
submission_id = 'submission_id_example' # str | 

try:
    # Download result archive from backend for particular submission.
    api_instance.assignment_solutions_download_result_archive(submission_id)
except ApiException as e:
    print("Exception when calling DefaultApi->assignment_solutions_download_result_archive: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submission_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assignment_solutions_download_solution_archive**
> assignment_solutions_download_solution_archive(id)

Download archive containing all solution files for particular solution.

Download archive containing all solution files for particular solution.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | of assignment solution

try:
    # Download archive containing all solution files for particular solution.
    api_instance.assignment_solutions_download_solution_archive(id)
except ApiException as e:
    print("Exception when calling DefaultApi->assignment_solutions_download_solution_archive: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| of assignment solution | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assignment_solutions_evaluation_score_config**
> assignment_solutions_evaluation_score_config(submission_id)

Get score configuration associated with given submission evaluation

Get score configuration associated with given submission evaluation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
submission_id = 'submission_id_example' # str | Identifier of the submission

try:
    # Get score configuration associated with given submission evaluation
    api_instance.assignment_solutions_evaluation_score_config(submission_id)
except ApiException as e:
    print("Exception when calling DefaultApi->assignment_solutions_evaluation_score_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submission_id** | **str**| Identifier of the submission | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assignment_solutions_files**
> assignment_solutions_files(id)

Get the list of submitted files of the solution.

Get the list of submitted files of the solution.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | of assignment solution

try:
    # Get the list of submitted files of the solution.
    api_instance.assignment_solutions_files(id)
except ApiException as e:
    print("Exception when calling DefaultApi->assignment_solutions_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| of assignment solution | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assignment_solutions_review_requests**
> assignment_solutions_review_requests(id)

Return all solutions with reviewRequest flag that given user might need to review (is admin/supervisor in corresponding groups). Along with that it returns all assignment entities of the corresponding solutions.

Return all solutions with reviewRequest flag that given user might need to review (is admin/supervisor in corresponding groups). Along with that it returns all assignment entities of the corresponding solutions.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | of the user whose solutions with requested reviews are listed

try:
    # Return all solutions with reviewRequest flag that given user might need to review (is admin/supervisor in corresponding groups). Along with that it returns all assignment entities of the corresponding solutions.
    api_instance.assignment_solutions_review_requests(id)
except ApiException as e:
    print("Exception when calling DefaultApi->assignment_solutions_review_requests: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| of the user whose solutions with requested reviews are listed | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assignment_solutions_set_bonus_points**
> assignment_solutions_set_bonus_points(id, body=body)

Set new amount of bonus points for a solution (and optionally points override) Returns array of solution entities that has been changed by this.

Set new amount of bonus points for a solution (and optionally points override) Returns array of solution entities that has been changed by this.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the solution
body = swagger_client.IdBonuspointsBody() # IdBonuspointsBody |  (optional)

try:
    # Set new amount of bonus points for a solution (and optionally points override) Returns array of solution entities that has been changed by this.
    api_instance.assignment_solutions_set_bonus_points(id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->assignment_solutions_set_bonus_points: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the solution | 
 **body** | [**IdBonuspointsBody**](IdBonuspointsBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assignment_solutions_set_flag**
> assignment_solutions_set_flag(id, flag, body=body)

Set flag of the assignment solution.

Set flag of the assignment solution.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | identifier of the solution
flag = 'flag_example' # str | name of the flag which should to be changed
body = swagger_client.SetflagFlagBody() # SetflagFlagBody |  (optional)

try:
    # Set flag of the assignment solution.
    api_instance.assignment_solutions_set_flag(id, flag, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->assignment_solutions_set_flag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of the solution | 
 **flag** | **str**| name of the flag which should to be changed | 
 **body** | [**SetflagFlagBody**](SetflagFlagBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assignment_solutions_solution**
> assignment_solutions_solution(id)

Get information about solutions.

Get information about solutions.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the solution

try:
    # Get information about solutions.
    api_instance.assignment_solutions_solution(id)
except ApiException as e:
    print("Exception when calling DefaultApi->assignment_solutions_solution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the solution | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assignment_solutions_submission**
> assignment_solutions_submission(submission_id)

Get information about the evaluation of a submission

Get information about the evaluation of a submission

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
submission_id = 'submission_id_example' # str | Identifier of the submission

try:
    # Get information about the evaluation of a submission
    api_instance.assignment_solutions_submission(submission_id)
except ApiException as e:
    print("Exception when calling DefaultApi->assignment_solutions_submission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submission_id** | **str**| Identifier of the submission | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assignment_solutions_submissions**
> assignment_solutions_submissions(id)

Get list of all submissions of a solution

Get list of all submissions of a solution

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the solution

try:
    # Get list of all submissions of a solution
    api_instance.assignment_solutions_submissions(id)
except ApiException as e:
    print("Exception when calling DefaultApi->assignment_solutions_submissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the solution | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assignment_solutions_update_solution**
> assignment_solutions_update_solution(id, body=body)

Update details about the solution (note, etc...)

Update details about the solution (note, etc...)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the solution
body = swagger_client.AssignmentsolutionsIdBody() # AssignmentsolutionsIdBody |  (optional)

try:
    # Update details about the solution (note, etc...)
    api_instance.assignment_solutions_update_solution(id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->assignment_solutions_update_solution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the solution | 
 **body** | [**AssignmentsolutionsIdBody**](AssignmentsolutionsIdBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assignment_solvers_default**
> assignment_solvers_default(assignment_id=assignment_id, group_id=group_id, user_id=user_id)

Get a list of assignment solvers based on given parameters (assignment/group and solver user). Either assignment or group ID must be set (group is ignored if assignment is set), user ID is optional.

Get a list of assignment solvers based on given parameters (assignment/group and solver user). Either assignment or group ID must be set (group is ignored if assignment is set), user ID is optional.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
assignment_id = 'assignment_id_example' # str |  (optional)
group_id = 'group_id_example' # str | An alternative for assignment ID, selects all assignments from a group. (optional)
user_id = 'user_id_example' # str |  (optional)

try:
    # Get a list of assignment solvers based on given parameters (assignment/group and solver user). Either assignment or group ID must be set (group is ignored if assignment is set), user ID is optional.
    api_instance.assignment_solvers_default(assignment_id=assignment_id, group_id=group_id, user_id=user_id)
except ApiException as e:
    print("Exception when calling DefaultApi->assignment_solvers_default: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assignment_id** | **str**|  | [optional] 
 **group_id** | **str**| An alternative for assignment ID, selects all assignments from a group. | [optional] 
 **user_id** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assignments_best_solution**
> assignments_best_solution(id, user_id)

Get the best solution by a user to an assignment

Get the best solution by a user to an assignment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the assignment
user_id = 'user_id_example' # str | Identifier of the user

try:
    # Get the best solution by a user to an assignment
    api_instance.assignments_best_solution(id, user_id)
except ApiException as e:
    print("Exception when calling DefaultApi->assignments_best_solution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the assignment | 
 **user_id** | **str**| Identifier of the user | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assignments_best_solutions**
> assignments_best_solutions(id)

Get the best solutions to an assignment for all students in group.

Get the best solutions to an assignment for all students in group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the assignment

try:
    # Get the best solutions to an assignment for all students in group.
    api_instance.assignments_best_solutions(id)
except ApiException as e:
    print("Exception when calling DefaultApi->assignments_best_solutions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the assignment | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assignments_create**
> assignments_create(body=body)

Assign an exercise to a group

Assign an exercise to a group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.V1ExerciseassignmentsBody() # V1ExerciseassignmentsBody |  (optional)

try:
    # Assign an exercise to a group
    api_instance.assignments_create(body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->assignments_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1ExerciseassignmentsBody**](V1ExerciseassignmentsBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assignments_detail**
> assignments_detail(id)

Get details of an assignment

Get details of an assignment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the assignment

try:
    # Get details of an assignment
    api_instance.assignments_detail(id)
except ApiException as e:
    print("Exception when calling DefaultApi->assignments_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the assignment | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assignments_download_best_solutions_archive**
> assignments_download_best_solutions_archive(id)

Download the best solutions of an assignment for all students in group.

Download the best solutions of an assignment for all students in group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the assignment

try:
    # Download the best solutions of an assignment for all students in group.
    api_instance.assignments_download_best_solutions_archive(id)
except ApiException as e:
    print("Exception when calling DefaultApi->assignments_download_best_solutions_archive: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the assignment | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assignments_remove**
> assignments_remove(id)

Delete an assignment

Delete an assignment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the assignment to be removed

try:
    # Delete an assignment
    api_instance.assignments_remove(id)
except ApiException as e:
    print("Exception when calling DefaultApi->assignments_remove: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the assignment to be removed | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assignments_solutions**
> assignments_solutions(id)

Get a list of solutions of all users for the assignment

Get a list of solutions of all users for the assignment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the assignment

try:
    # Get a list of solutions of all users for the assignment
    api_instance.assignments_solutions(id)
except ApiException as e:
    print("Exception when calling DefaultApi->assignments_solutions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the assignment | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assignments_sync_with_exercise**
> assignments_sync_with_exercise(id)

Update the assignment so that it matches with the current version of the exercise (limits, texts, etc.)

Update the assignment so that it matches with the current version of the exercise (limits, texts, etc.)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the assignment that should be synchronized

try:
    # Update the assignment so that it matches with the current version of the exercise (limits, texts, etc.)
    api_instance.assignments_sync_with_exercise(id)
except ApiException as e:
    print("Exception when calling DefaultApi->assignments_sync_with_exercise: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the assignment that should be synchronized | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assignments_update_detail**
> assignments_update_detail(id, body=body)

Update details of an assignment

Update details of an assignment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the updated assignment
body = swagger_client.ExerciseassignmentsIdBody() # ExerciseassignmentsIdBody |  (optional)

try:
    # Update details of an assignment
    api_instance.assignments_update_detail(id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->assignments_update_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the updated assignment | 
 **body** | [**ExerciseassignmentsIdBody**](ExerciseassignmentsIdBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assignments_user_solutions**
> assignments_user_solutions(id, user_id)

Get a list of solutions created by a user of an assignment

Get a list of solutions created by a user of an assignment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the assignment
user_id = 'user_id_example' # str | Identifier of the user

try:
    # Get a list of solutions created by a user of an assignment
    api_instance.assignments_user_solutions(id, user_id)
except ApiException as e:
    print("Exception when calling DefaultApi->assignments_user_solutions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the assignment | 
 **user_id** | **str**| Identifier of the user | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **assignments_validate**
> assignments_validate(id, body=body)

Check if the version of the assignment is up-to-date.

Check if the version of the assignment is up-to-date.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the assignment
body = swagger_client.IdValidateBody1() # IdValidateBody1 |  (optional)

try:
    # Check if the version of the assignment is up-to-date.
    api_instance.assignments_validate(id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->assignments_validate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the assignment | 
 **body** | [**IdValidateBody1**](IdValidateBody1.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **async_jobs_abort**
> async_jobs_abort(id)

Retrieves details about particular async job.

Retrieves details about particular async job.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | job identifier

try:
    # Retrieves details about particular async job.
    api_instance.async_jobs_abort(id)
except ApiException as e:
    print("Exception when calling DefaultApi->async_jobs_abort: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| job identifier | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **async_jobs_assignment_jobs**
> async_jobs_assignment_jobs(id)

Get all pending async jobs related to a particular assignment.

Get all pending async jobs related to a particular assignment.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | 

try:
    # Get all pending async jobs related to a particular assignment.
    api_instance.async_jobs_assignment_jobs(id)
except ApiException as e:
    print("Exception when calling DefaultApi->async_jobs_assignment_jobs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **async_jobs_default**
> async_jobs_default(id)

Retrieves details about particular async job.

Retrieves details about particular async job.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | job identifier

try:
    # Retrieves details about particular async job.
    api_instance.async_jobs_default(id)
except ApiException as e:
    print("Exception when calling DefaultApi->async_jobs_default: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| job identifier | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **async_jobs_list**
> async_jobs_list(age_threshold=age_threshold, include_scheduled=include_scheduled)

Retrieves details about async jobs that are either pending or were recently completed.

Retrieves details about async jobs that are either pending or were recently completed.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
age_threshold = 56 # int | Maximal time since completion (in seconds), null = only pending operations (optional)
include_scheduled = true # bool | If true, pending scheduled events will be listed as well (optional)

try:
    # Retrieves details about async jobs that are either pending or were recently completed.
    api_instance.async_jobs_list(age_threshold=age_threshold, include_scheduled=include_scheduled)
except ApiException as e:
    print("Exception when calling DefaultApi->async_jobs_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **age_threshold** | **int**| Maximal time since completion (in seconds), null &#x3D; only pending operations | [optional] 
 **include_scheduled** | **bool**| If true, pending scheduled events will be listed as well | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **async_jobs_ping**
> async_jobs_ping()

Initiates ping job. An empty job designed to verify the async handler is running.

Initiates ping job. An empty job designed to verify the async handler is running.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    # Initiates ping job. An empty job designed to verify the async handler is running.
    api_instance.async_jobs_ping()
except ApiException as e:
    print("Exception when calling DefaultApi->async_jobs_ping: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **broker_freeze**
> broker_freeze()

Freeze broker and its execution.

Freeze broker and its execution.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    # Freeze broker and its execution.
    api_instance.broker_freeze()
except ApiException as e:
    print("Exception when calling DefaultApi->broker_freeze: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **broker_reports_error**
> broker_reports_error(body=body)

Announce a backend error that is not related to any job (meant to be called by the backend)

Announce a backend error that is not related to any job (meant to be called by the backend)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.BrokerreportsErrorBody() # BrokerreportsErrorBody |  (optional)

try:
    # Announce a backend error that is not related to any job (meant to be called by the backend)
    api_instance.broker_reports_error(body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->broker_reports_error: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**BrokerreportsErrorBody**](BrokerreportsErrorBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **broker_reports_job_status**
> broker_reports_job_status(job_id, body=body)

Update the status of a job (meant to be called by the backend)

Update the status of a job (meant to be called by the backend)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
job_id = 'job_id_example' # str | Identifier of the job whose status is being reported
body = swagger_client.JobstatusJobIdBody() # JobstatusJobIdBody |  (optional)

try:
    # Update the status of a job (meant to be called by the backend)
    api_instance.broker_reports_job_status(job_id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->broker_reports_job_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **str**| Identifier of the job whose status is being reported | 
 **body** | [**JobstatusJobIdBody**](JobstatusJobIdBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **broker_stats**
> broker_stats()

Get current statistics from broker.

Get current statistics from broker.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    # Get current statistics from broker.
    api_instance.broker_stats()
except ApiException as e:
    print("Exception when calling DefaultApi->broker_stats: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **broker_unfreeze**
> broker_unfreeze()

Unfreeze broker and its execution.

Unfreeze broker and its execution.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    # Unfreeze broker and its execution.
    api_instance.broker_unfreeze()
except ApiException as e:
    print("Exception when calling DefaultApi->broker_unfreeze: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **comments_add_comment**
> comments_add_comment(id, body=body)

Add a comment to a thread

Add a comment to a thread

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the comment thread
body = swagger_client.CommentsIdBody() # CommentsIdBody |  (optional)

try:
    # Add a comment to a thread
    api_instance.comments_add_comment(id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->comments_add_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the comment thread | 
 **body** | [**CommentsIdBody**](CommentsIdBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **comments_default**
> comments_default(id)

Get a comment thread

Get a comment thread

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the comment thread

try:
    # Get a comment thread
    api_instance.comments_default(id)
except ApiException as e:
    print("Exception when calling DefaultApi->comments_default: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the comment thread | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **comments_delete**
> comments_delete(thread_id, comment_id)

Delete a comment

Delete a comment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
thread_id = 'thread_id_example' # str | Identifier of the comment thread
comment_id = 'comment_id_example' # str | Identifier of the comment

try:
    # Delete a comment
    api_instance.comments_delete(thread_id, comment_id)
except ApiException as e:
    print("Exception when calling DefaultApi->comments_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_id** | **str**| Identifier of the comment thread | 
 **comment_id** | **str**| Identifier of the comment | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **comments_set_private**
> comments_set_private(thread_id, comment_id, body=body)

Set the private flag of a comment

Set the private flag of a comment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
thread_id = 'thread_id_example' # str | Identifier of the comment thread
comment_id = 'comment_id_example' # str | Identifier of the comment
body = swagger_client.CommentIdPrivateBody() # CommentIdPrivateBody |  (optional)

try:
    # Set the private flag of a comment
    api_instance.comments_set_private(thread_id, comment_id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->comments_set_private: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_id** | **str**| Identifier of the comment thread | 
 **comment_id** | **str**| Identifier of the comment | 
 **body** | [**CommentIdPrivateBody**](CommentIdPrivateBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **comments_toggle_private**
> comments_toggle_private(thread_id, comment_id)

Make a private comment public or vice versa

Make a private comment public or vice versa

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
thread_id = 'thread_id_example' # str | Identifier of the comment thread
comment_id = 'comment_id_example' # str | Identifier of the comment

try:
    # Make a private comment public or vice versa
    api_instance.comments_toggle_private(thread_id, comment_id)
except ApiException as e:
    print("Exception when calling DefaultApi->comments_toggle_private: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_id** | **str**| Identifier of the comment thread | 
 **comment_id** | **str**| Identifier of the comment | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_verification_email_verification**
> email_verification_email_verification()

Verify users email.

Verify users email.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    # Verify users email.
    api_instance.email_verification_email_verification()
except ApiException as e:
    print("Exception when calling DefaultApi->email_verification_email_verification: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **email_verification_resend_verification_email**
> email_verification_resend_verification_email()

Resend the email for the current user to verify his/her email address.

Resend the email for the current user to verify his/her email address.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    # Resend the email for the current user to verify his/her email address.
    api_instance.email_verification_resend_verification_email()
except ApiException as e:
    print("Exception when calling DefaultApi->email_verification_resend_verification_email: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **emails_default**
> emails_default(body=body)

Sends an email with provided subject and message to all ReCodEx users.

Sends an email with provided subject and message to all ReCodEx users.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.V1EmailsBody() # V1EmailsBody |  (optional)

try:
    # Sends an email with provided subject and message to all ReCodEx users.
    api_instance.emails_default(body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->emails_default: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1EmailsBody**](V1EmailsBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **emails_send_to_group_members**
> emails_send_to_group_members(group_id, body=body)

Sends an email with provided subject and message to regular members of given group and optionally to supervisors and admins.

Sends an email with provided subject and message to regular members of given group and optionally to supervisors and admins.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
group_id = 'group_id_example' # str | 
body = swagger_client.GroupsGroupIdBody() # GroupsGroupIdBody |  (optional)

try:
    # Sends an email with provided subject and message to regular members of given group and optionally to supervisors and admins.
    api_instance.emails_send_to_group_members(group_id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->emails_send_to_group_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 
 **body** | [**GroupsGroupIdBody**](GroupsGroupIdBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **emails_send_to_regular_users**
> emails_send_to_regular_users(body=body)

Sends an email with provided subject and message to all regular users.

Sends an email with provided subject and message to all regular users.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.EmailsRegularusersBody() # EmailsRegularusersBody |  (optional)

try:
    # Sends an email with provided subject and message to all regular users.
    api_instance.emails_send_to_regular_users(body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->emails_send_to_regular_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmailsRegularusersBody**](EmailsRegularusersBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **emails_send_to_supervisors**
> emails_send_to_supervisors(body=body)

Sends an email with provided subject and message to all supervisors and superadmins.

Sends an email with provided subject and message to all supervisors and superadmins.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.EmailsSupervisorsBody() # EmailsSupervisorsBody |  (optional)

try:
    # Sends an email with provided subject and message to all supervisors and superadmins.
    api_instance.emails_send_to_supervisors(body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->emails_send_to_supervisors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EmailsSupervisorsBody**](EmailsSupervisorsBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exercise_files_delete_attachment_file**
> exercise_files_delete_attachment_file(id, file_id)

Delete attachment exercise file with given id

Delete attachment exercise file with given id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | identification of exercise
file_id = 'file_id_example' # str | identification of file

try:
    # Delete attachment exercise file with given id
    api_instance.exercise_files_delete_attachment_file(id, file_id)
except ApiException as e:
    print("Exception when calling DefaultApi->exercise_files_delete_attachment_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identification of exercise | 
 **file_id** | **str**| identification of file | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exercise_files_delete_supplementary_file**
> exercise_files_delete_supplementary_file(id, file_id)

Delete supplementary exercise file with given id

Delete supplementary exercise file with given id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | identification of exercise
file_id = 'file_id_example' # str | identification of file

try:
    # Delete supplementary exercise file with given id
    api_instance.exercise_files_delete_supplementary_file(id, file_id)
except ApiException as e:
    print("Exception when calling DefaultApi->exercise_files_delete_supplementary_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identification of exercise | 
 **file_id** | **str**| identification of file | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exercise_files_download_attachment_files_archive**
> exercise_files_download_attachment_files_archive(id)

Download archive containing all attachment files for exercise.

Download archive containing all attachment files for exercise.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | of exercise

try:
    # Download archive containing all attachment files for exercise.
    api_instance.exercise_files_download_attachment_files_archive(id)
except ApiException as e:
    print("Exception when calling DefaultApi->exercise_files_download_attachment_files_archive: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| of exercise | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exercise_files_download_supplementary_files_archive**
> exercise_files_download_supplementary_files_archive(id)

Download archive containing all supplementary files for exercise.

Download archive containing all supplementary files for exercise.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | of exercise

try:
    # Download archive containing all supplementary files for exercise.
    api_instance.exercise_files_download_supplementary_files_archive(id)
except ApiException as e:
    print("Exception when calling DefaultApi->exercise_files_download_supplementary_files_archive: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| of exercise | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exercise_files_get_attachment_files**
> exercise_files_get_attachment_files(id)

Get a list of all attachment files for an exercise

Get a list of all attachment files for an exercise

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | identification of exercise

try:
    # Get a list of all attachment files for an exercise
    api_instance.exercise_files_get_attachment_files(id)
except ApiException as e:
    print("Exception when calling DefaultApi->exercise_files_get_attachment_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identification of exercise | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exercise_files_get_supplementary_files**
> exercise_files_get_supplementary_files(id)

Get list of all supplementary files for an exercise

Get list of all supplementary files for an exercise

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | identification of exercise

try:
    # Get list of all supplementary files for an exercise
    api_instance.exercise_files_get_supplementary_files(id)
except ApiException as e:
    print("Exception when calling DefaultApi->exercise_files_get_supplementary_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identification of exercise | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exercise_files_upload_attachment_files**
> exercise_files_upload_attachment_files(id, body=body)

Associate attachment exercise files with an exercise

Associate attachment exercise files with an exercise

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | identification of exercise
body = swagger_client.IdAttachmentfilesBody() # IdAttachmentfilesBody |  (optional)

try:
    # Associate attachment exercise files with an exercise
    api_instance.exercise_files_upload_attachment_files(id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->exercise_files_upload_attachment_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identification of exercise | 
 **body** | [**IdAttachmentfilesBody**](IdAttachmentfilesBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exercise_files_upload_supplementary_files**
> exercise_files_upload_supplementary_files(id, body=body)

Associate supplementary files with an exercise and upload them to remote file server

Associate supplementary files with an exercise and upload them to remote file server

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | identification of exercise
body = swagger_client.IdSupplementaryfilesBody() # IdSupplementaryfilesBody |  (optional)

try:
    # Associate supplementary files with an exercise and upload them to remote file server
    api_instance.exercise_files_upload_supplementary_files(id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->exercise_files_upload_supplementary_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identification of exercise | 
 **body** | [**IdSupplementaryfilesBody**](IdSupplementaryfilesBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exercises_add_tag**
> exercises_add_tag(id, name)

Add tag with given name to the exercise.

Add tag with given name to the exercise.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | 
name = 'name_example' # str | Name of the newly added tag to given exercise

try:
    # Add tag with given name to the exercise.
    api_instance.exercises_add_tag(id, name)
except ApiException as e:
    print("Exception when calling DefaultApi->exercises_add_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **name** | **str**| Name of the newly added tag to given exercise | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exercises_all_tags**
> exercises_all_tags()

Get list of global exercise tag names which are currently registered.

Get list of global exercise tag names which are currently registered.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    # Get list of global exercise tag names which are currently registered.
    api_instance.exercises_all_tags()
except ApiException as e:
    print("Exception when calling DefaultApi->exercises_all_tags: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exercises_assignments**
> exercises_assignments(id, archived=archived)

Get all non-archived assignments created from this exercise.

Get all non-archived assignments created from this exercise.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the exercise
archived = true # bool | Include also archived groups in the result (optional)

try:
    # Get all non-archived assignments created from this exercise.
    api_instance.exercises_assignments(id, archived=archived)
except ApiException as e:
    print("Exception when calling DefaultApi->exercises_assignments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the exercise | 
 **archived** | **bool**| Include also archived groups in the result | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exercises_attach_group**
> exercises_attach_group(id, group_id)

Attach exercise to group with given identification.

Attach exercise to group with given identification.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the exercise
group_id = 'group_id_example' # str | Identifier of the group to which exercise should be attached

try:
    # Attach exercise to group with given identification.
    api_instance.exercises_attach_group(id, group_id)
except ApiException as e:
    print("Exception when calling DefaultApi->exercises_attach_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the exercise | 
 **group_id** | **str**| Identifier of the group to which exercise should be attached | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exercises_authors**
> exercises_authors(instance_id=instance_id, group_id=group_id)

List authors of all exercises, possibly filtered by a group in which the exercises appear.

List authors of all exercises, possibly filtered by a group in which the exercises appear.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
instance_id = 'instance_id_example' # str | Id of an instance from which the authors are listed. (optional)
group_id = 'group_id_example' # str | A group where the relevant exercises can be seen (assigned). (optional)

try:
    # List authors of all exercises, possibly filtered by a group in which the exercises appear.
    api_instance.exercises_authors(instance_id=instance_id, group_id=group_id)
except ApiException as e:
    print("Exception when calling DefaultApi->exercises_authors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Id of an instance from which the authors are listed. | [optional] 
 **group_id** | **str**| A group where the relevant exercises can be seen (assigned). | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exercises_config_get_configuration**
> exercises_config_get_configuration(id)

Get a basic exercise high level configuration.

Get a basic exercise high level configuration.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the exercise

try:
    # Get a basic exercise high level configuration.
    api_instance.exercises_config_get_configuration(id)
except ApiException as e:
    print("Exception when calling DefaultApi->exercises_config_get_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the exercise | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exercises_config_get_environment_configs**
> exercises_config_get_environment_configs(id)

Get runtime configurations for exercise.

Get runtime configurations for exercise.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the exercise

try:
    # Get runtime configurations for exercise.
    api_instance.exercises_config_get_environment_configs(id)
except ApiException as e:
    print("Exception when calling DefaultApi->exercises_config_get_environment_configs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the exercise | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exercises_config_get_hardware_group_limits**
> exercises_config_get_hardware_group_limits(id, runtime_environment_id, hw_group_id)

Get a description of resource limits for an exercise for given hwgroup.

Get a description of resource limits for an exercise for given hwgroup.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the exercise
runtime_environment_id = 'runtime_environment_id_example' # str | 
hw_group_id = 'hw_group_id_example' # str | 

try:
    # Get a description of resource limits for an exercise for given hwgroup.
    api_instance.exercises_config_get_hardware_group_limits(id, runtime_environment_id, hw_group_id)
except ApiException as e:
    print("Exception when calling DefaultApi->exercises_config_get_hardware_group_limits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the exercise | 
 **runtime_environment_id** | **str**|  | 
 **hw_group_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exercises_config_get_limits**
> exercises_config_get_limits(id)

Get a description of resource limits for given exercise (all hwgroups all environments).

Get a description of resource limits for given exercise (all hwgroups all environments).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the exercise

try:
    # Get a description of resource limits for given exercise (all hwgroups all environments).
    api_instance.exercises_config_get_limits(id)
except ApiException as e:
    print("Exception when calling DefaultApi->exercises_config_get_limits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the exercise | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exercises_config_get_score_config**
> exercises_config_get_score_config(id)

Get score configuration for exercise based on given identification.

Get score configuration for exercise based on given identification.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the exercise

try:
    # Get score configuration for exercise based on given identification.
    api_instance.exercises_config_get_score_config(id)
except ApiException as e:
    print("Exception when calling DefaultApi->exercises_config_get_score_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the exercise | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exercises_config_get_tests**
> exercises_config_get_tests(id)

Get tests for exercise based on given identification.

Get tests for exercise based on given identification.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the exercise

try:
    # Get tests for exercise based on given identification.
    api_instance.exercises_config_get_tests(id)
except ApiException as e:
    print("Exception when calling DefaultApi->exercises_config_get_tests: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the exercise | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exercises_config_get_variables_for_exercise_config**
> exercises_config_get_variables_for_exercise_config(id, body=body)

Get variables for exercise configuration which are derived from given pipelines and runtime environment.

Get variables for exercise configuration which are derived from given pipelines and runtime environment.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the exercise
body = swagger_client.ConfigVariablesBody() # ConfigVariablesBody |  (optional)

try:
    # Get variables for exercise configuration which are derived from given pipelines and runtime environment.
    api_instance.exercises_config_get_variables_for_exercise_config(id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->exercises_config_get_variables_for_exercise_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the exercise | 
 **body** | [**ConfigVariablesBody**](ConfigVariablesBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exercises_config_remove_hardware_group_limits**
> exercises_config_remove_hardware_group_limits(id, runtime_environment_id, hw_group_id)

Remove resource limits of given hwgroup from an exercise.

Remove resource limits of given hwgroup from an exercise.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the exercise
runtime_environment_id = 'runtime_environment_id_example' # str | 
hw_group_id = 'hw_group_id_example' # str | 

try:
    # Remove resource limits of given hwgroup from an exercise.
    api_instance.exercises_config_remove_hardware_group_limits(id, runtime_environment_id, hw_group_id)
except ApiException as e:
    print("Exception when calling DefaultApi->exercises_config_remove_hardware_group_limits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the exercise | 
 **runtime_environment_id** | **str**|  | 
 **hw_group_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exercises_config_set_configuration**
> exercises_config_set_configuration(id, body=body)

Set basic exercise configuration

Set basic exercise configuration

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the exercise
body = swagger_client.IdConfigBody() # IdConfigBody |  (optional)

try:
    # Set basic exercise configuration
    api_instance.exercises_config_set_configuration(id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->exercises_config_set_configuration: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the exercise | 
 **body** | [**IdConfigBody**](IdConfigBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exercises_config_set_hardware_group_limits**
> exercises_config_set_hardware_group_limits(id, runtime_environment_id, hw_group_id, body=body)

Set resource limits for an exercise for given hwgroup.

Set resource limits for an exercise for given hwgroup.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the exercise
runtime_environment_id = 'runtime_environment_id_example' # str | 
hw_group_id = 'hw_group_id_example' # str | 
body = swagger_client.HwGroupIdLimitsBody() # HwGroupIdLimitsBody |  (optional)

try:
    # Set resource limits for an exercise for given hwgroup.
    api_instance.exercises_config_set_hardware_group_limits(id, runtime_environment_id, hw_group_id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->exercises_config_set_hardware_group_limits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the exercise | 
 **runtime_environment_id** | **str**|  | 
 **hw_group_id** | **str**|  | 
 **body** | [**HwGroupIdLimitsBody**](HwGroupIdLimitsBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exercises_config_set_limits**
> exercises_config_set_limits(id, body=body)

Update resource limits for given exercise. If limits for particular hwGroup or environment are not posted, no change occurs. If limits for particular hwGroup or environment are posted as null, they are removed.

Update resource limits for given exercise. If limits for particular hwGroup or environment are not posted, no change occurs. If limits for particular hwGroup or environment are posted as null, they are removed.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the exercise
body = swagger_client.IdLimitsBody() # IdLimitsBody |  (optional)

try:
    # Update resource limits for given exercise. If limits for particular hwGroup or environment are not posted, no change occurs. If limits for particular hwGroup or environment are posted as null, they are removed.
    api_instance.exercises_config_set_limits(id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->exercises_config_set_limits: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the exercise | 
 **body** | [**IdLimitsBody**](IdLimitsBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exercises_config_set_score_config**
> exercises_config_set_score_config(id, body=body)

Set score configuration for exercise.

Set score configuration for exercise.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the exercise
body = swagger_client.IdScoreconfigBody() # IdScoreconfigBody |  (optional)

try:
    # Set score configuration for exercise.
    api_instance.exercises_config_set_score_config(id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->exercises_config_set_score_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the exercise | 
 **body** | [**IdScoreconfigBody**](IdScoreconfigBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exercises_config_set_tests**
> exercises_config_set_tests(id, body=body)

Set tests for exercise based on given identification.

Set tests for exercise based on given identification.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the exercise
body = swagger_client.IdTestsBody() # IdTestsBody |  (optional)

try:
    # Set tests for exercise based on given identification.
    api_instance.exercises_config_set_tests(id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->exercises_config_set_tests: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the exercise | 
 **body** | [**IdTestsBody**](IdTestsBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exercises_config_update_environment_configs**
> exercises_config_update_environment_configs(id, body=body)

Change runtime configuration of exercise. Configurations can be added or deleted here, based on what is provided in arguments.

Change runtime configuration of exercise. Configurations can be added or deleted here, based on what is provided in arguments.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | identification of exercise
body = swagger_client.IdEnvironmentconfigsBody() # IdEnvironmentconfigsBody |  (optional)

try:
    # Change runtime configuration of exercise. Configurations can be added or deleted here, based on what is provided in arguments.
    api_instance.exercises_config_update_environment_configs(id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->exercises_config_update_environment_configs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identification of exercise | 
 **body** | [**IdEnvironmentconfigsBody**](IdEnvironmentconfigsBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exercises_create**
> exercises_create(body=body)

Create exercise with all default values. Exercise detail can be then changed in appropriate endpoint.

Create exercise with all default values. Exercise detail can be then changed in appropriate endpoint.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.V1ExercisesBody() # V1ExercisesBody |  (optional)

try:
    # Create exercise with all default values. Exercise detail can be then changed in appropriate endpoint.
    api_instance.exercises_create(body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->exercises_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1ExercisesBody**](V1ExercisesBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exercises_default**
> exercises_default(offset=offset, limit=limit, order_by=order_by, filters=filters, locale=locale)

Get a list of all exercises matching given filters in given pagination rage. The result conforms to pagination protocol.

Get a list of all exercises matching given filters in given pagination rage. The result conforms to pagination protocol.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
offset = 56 # int | Index of the first result. (optional)
limit = 56 # int | Maximal number of results returned. (optional)
order_by = 'order_by_example' # str | Name of the column (column concept). The '!' prefix indicate descending order. (optional)
filters = NULL # list[object] | Named filters that prune the result. (optional)
locale = 'locale_example' # str | Currently set locale (used to augment order by clause if necessary), (optional)

try:
    # Get a list of all exercises matching given filters in given pagination rage. The result conforms to pagination protocol.
    api_instance.exercises_default(offset=offset, limit=limit, order_by=order_by, filters=filters, locale=locale)
except ApiException as e:
    print("Exception when calling DefaultApi->exercises_default: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Index of the first result. | [optional] 
 **limit** | **int**| Maximal number of results returned. | [optional] 
 **order_by** | **str**| Name of the column (column concept). The &#x27;!&#x27; prefix indicate descending order. | [optional] 
 **filters** | [**list[object]**](object.md)| Named filters that prune the result. | [optional] 
 **locale** | **str**| Currently set locale (used to augment order by clause if necessary), | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exercises_detach_group**
> exercises_detach_group(id, group_id)

Detach exercise from given group.

Detach exercise from given group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the exercise
group_id = 'group_id_example' # str | Identifier of the group which should be detached from exercise

try:
    # Detach exercise from given group.
    api_instance.exercises_detach_group(id, group_id)
except ApiException as e:
    print("Exception when calling DefaultApi->exercises_detach_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the exercise | 
 **group_id** | **str**| Identifier of the group which should be detached from exercise | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exercises_detail**
> exercises_detail(id)

Get details of an exercise

Get details of an exercise

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | identification of exercise

try:
    # Get details of an exercise
    api_instance.exercises_detail(id)
except ApiException as e:
    print("Exception when calling DefaultApi->exercises_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identification of exercise | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exercises_fork_from**
> exercises_fork_from(id, body=body)

Fork exercise from given one into the completely new one.

Fork exercise from given one into the completely new one.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the exercise
body = swagger_client.IdForkBody() # IdForkBody |  (optional)

try:
    # Fork exercise from given one into the completely new one.
    api_instance.exercises_fork_from(id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->exercises_fork_from: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the exercise | 
 **body** | [**IdForkBody**](IdForkBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exercises_hardware_groups**
> exercises_hardware_groups(id, body=body)

Set hardware groups which are associated with exercise.

Set hardware groups which are associated with exercise.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | identifier of exercise
body = swagger_client.IdHardwaregroupsBody() # IdHardwaregroupsBody |  (optional)

try:
    # Set hardware groups which are associated with exercise.
    api_instance.exercises_hardware_groups(id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->exercises_hardware_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of exercise | 
 **body** | [**IdHardwaregroupsBody**](IdHardwaregroupsBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exercises_list_by_ids**
> exercises_list_by_ids(body=body)

Get a list of exercises based on given ids.

Get a list of exercises based on given ids.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.ExercisesListBody() # ExercisesListBody |  (optional)

try:
    # Get a list of exercises based on given ids.
    api_instance.exercises_list_by_ids(body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->exercises_list_by_ids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ExercisesListBody**](ExercisesListBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exercises_remove**
> exercises_remove(id)

Delete an exercise

Delete an exercise

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | 

try:
    # Delete an exercise
    api_instance.exercises_remove(id)
except ApiException as e:
    print("Exception when calling DefaultApi->exercises_remove: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exercises_remove_tag**
> exercises_remove_tag(id, name)

Remove tag with given name from exercise.

Remove tag with given name from exercise.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | 
name = 'name_example' # str | 

try:
    # Remove tag with given name from exercise.
    api_instance.exercises_remove_tag(id, name)
except ApiException as e:
    print("Exception when calling DefaultApi->exercises_remove_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **name** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exercises_send_notification**
> exercises_send_notification(id, body=body)

Sends an email to all group admins and supervisors, where the exercise is assigned. The purpose of this is to quickly notify all relevant teachers when a bug is found or the exercise is modified significantly. The response is number of emails sent (number of notified users).

Sends an email to all group admins and supervisors, where the exercise is assigned. The purpose of this is to quickly notify all relevant teachers when a bug is found or the exercise is modified significantly. The response is number of emails sent (number of notified users).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | identifier of the exercise
body = swagger_client.IdNotificationBody() # IdNotificationBody |  (optional)

try:
    # Sends an email to all group admins and supervisors, where the exercise is assigned. The purpose of this is to quickly notify all relevant teachers when a bug is found or the exercise is modified significantly. The response is number of emails sent (number of notified users).
    api_instance.exercises_send_notification(id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->exercises_send_notification: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of the exercise | 
 **body** | [**IdNotificationBody**](IdNotificationBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exercises_set_admins**
> exercises_set_admins(id, body=body)

Change who the admins of an exercise are (all users on the list are added, prior admins not on the list are removed).

Change who the admins of an exercise are (all users on the list are added, prior admins not on the list are removed).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | identifier of the exercise
body = swagger_client.IdAdminsBody() # IdAdminsBody |  (optional)

try:
    # Change who the admins of an exercise are (all users on the list are added, prior admins not on the list are removed).
    api_instance.exercises_set_admins(id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->exercises_set_admins: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of the exercise | 
 **body** | [**IdAdminsBody**](IdAdminsBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exercises_set_archived**
> exercises_set_archived(id, body=body)

(Un)mark the exercise as archived. Nothing happens if the exercise is already in the requested state.

(Un)mark the exercise as archived. Nothing happens if the exercise is already in the requested state.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | identifier of the exercise
body = swagger_client.IdArchivedBody() # IdArchivedBody |  (optional)

try:
    # (Un)mark the exercise as archived. Nothing happens if the exercise is already in the requested state.
    api_instance.exercises_set_archived(id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->exercises_set_archived: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of the exercise | 
 **body** | [**IdArchivedBody**](IdArchivedBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exercises_set_author**
> exercises_set_author(id, body=body)

Change the author of the exercise. This is a very special operation reserved for powerful users.

Change the author of the exercise. This is a very special operation reserved for powerful users.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | identifier of the exercise
body = swagger_client.IdAuthorBody() # IdAuthorBody |  (optional)

try:
    # Change the author of the exercise. This is a very special operation reserved for powerful users.
    api_instance.exercises_set_author(id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->exercises_set_author: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of the exercise | 
 **body** | [**IdAuthorBody**](IdAuthorBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exercises_tags_stats**
> exercises_tags_stats()

Get list of global exercise tag names along with how many times they have been used.

Get list of global exercise tag names along with how many times they have been used.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    # Get list of global exercise tag names along with how many times they have been used.
    api_instance.exercises_tags_stats()
except ApiException as e:
    print("Exception when calling DefaultApi->exercises_tags_stats: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exercises_tags_update_global**
> exercises_tags_update_global(tag, rename_to=rename_to, force=force)

Update the tag globally. At the moment, the only 'update' function is 'rename'. Other types of updates may be implemented in the future.

Update the tag globally. At the moment, the only 'update' function is 'rename'. Other types of updates may be implemented in the future.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
tag = 'tag_example' # str | Tag to be updated
rename_to = 'rename_to_example' # str | New name of the tag (optional)
force = true # bool | If true, the rename will be allowed even if the new tag name exists (tags will be merged). Otherwise, name collisions will result in error. (optional)

try:
    # Update the tag globally. At the moment, the only 'update' function is 'rename'. Other types of updates may be implemented in the future.
    api_instance.exercises_tags_update_global(tag, rename_to=rename_to, force=force)
except ApiException as e:
    print("Exception when calling DefaultApi->exercises_tags_update_global: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tag** | **str**| Tag to be updated | 
 **rename_to** | **str**| New name of the tag | [optional] 
 **force** | **bool**| If true, the rename will be allowed even if the new tag name exists (tags will be merged). Otherwise, name collisions will result in error. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exercises_update_detail**
> exercises_update_detail(id, body=body)

Update detail of an exercise

Update detail of an exercise

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | identification of exercise
body = swagger_client.ExercisesIdBody() # ExercisesIdBody |  (optional)

try:
    # Update detail of an exercise
    api_instance.exercises_update_detail(id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->exercises_update_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identification of exercise | 
 **body** | [**ExercisesIdBody**](ExercisesIdBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **exercises_validate**
> exercises_validate(id, body=body)

Check if the version of the exercise is up-to-date.

Check if the version of the exercise is up-to-date.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the exercise
body = swagger_client.IdValidateBody() # IdValidateBody |  (optional)

try:
    # Check if the version of the exercise is up-to-date.
    api_instance.exercises_validate(id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->exercises_validate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the exercise | 
 **body** | [**IdValidateBody**](IdValidateBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extensions_token**
> extensions_token(ext_id)

This endpoint is used by a backend of an extension to get a proper access token (from a temp token passed via URL). It also returns details about authenticated user.

This endpoint is used by a backend of an extension to get a proper access token (from a temp token passed via URL). It also returns details about authenticated user.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
ext_id = 'ext_id_example' # str | 

try:
    # This endpoint is used by a backend of an extension to get a proper access token (from a temp token passed via URL). It also returns details about authenticated user.
    api_instance.extensions_token(ext_id)
except ApiException as e:
    print("Exception when calling DefaultApi->extensions_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ext_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **extensions_url**
> extensions_url(ext_id, instance_id, locale=locale, _return=_return)

Return URL refering to the extension with properly injected temporary JWT token.

Return URL refering to the extension with properly injected temporary JWT token.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
ext_id = 'ext_id_example' # str | 
instance_id = 'instance_id_example' # str | 
locale = 'locale_example' # str |  (optional)
_return = '_return_example' # str |  (optional)

try:
    # Return URL refering to the extension with properly injected temporary JWT token.
    api_instance.extensions_url(ext_id, instance_id, locale=locale, _return=_return)
except ApiException as e:
    print("Exception when calling DefaultApi->extensions_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ext_id** | **str**|  | 
 **instance_id** | **str**|  | 
 **locale** | **str**|  | [optional] 
 **_return** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forgotten_password_change**
> forgotten_password_change(body=body)

Change the user's password

Change the user's password

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.ForgottenpasswordChangeBody() # ForgottenpasswordChangeBody |  (optional)

try:
    # Change the user's password
    api_instance.forgotten_password_change(body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->forgotten_password_change: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ForgottenpasswordChangeBody**](ForgottenpasswordChangeBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forgotten_password_default**
> forgotten_password_default(body=body)

Request a password reset (user will receive an e-mail that prompts them to reset their password)

Request a password reset (user will receive an e-mail that prompts them to reset their password)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.V1ForgottenpasswordBody() # V1ForgottenpasswordBody |  (optional)

try:
    # Request a password reset (user will receive an e-mail that prompts them to reset their password)
    api_instance.forgotten_password_default(body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->forgotten_password_default: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1ForgottenpasswordBody**](V1ForgottenpasswordBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **forgotten_password_validate_password_strength**
> forgotten_password_validate_password_strength(body=body)

Check if a password is strong enough

Check if a password is strong enough

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.ForgottenpasswordValidatepasswordstrengthBody() # ForgottenpasswordValidatepasswordstrengthBody |  (optional)

try:
    # Check if a password is strong enough
    api_instance.forgotten_password_validate_password_strength(body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->forgotten_password_validate_password_strength: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ForgottenpasswordValidatepasswordstrengthBody**](ForgottenpasswordValidatepasswordstrengthBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_external_attributes_add**
> group_external_attributes_add(group_id, body=body)

Create an external attribute for given group.

Create an external attribute for given group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
group_id = 'group_id_example' # str | 
body = swagger_client.GroupattributesGroupIdBody() # GroupattributesGroupIdBody |  (optional)

try:
    # Create an external attribute for given group.
    api_instance.group_external_attributes_add(group_id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->group_external_attributes_add: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 
 **body** | [**GroupattributesGroupIdBody**](GroupattributesGroupIdBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_external_attributes_default**
> group_external_attributes_default(filter)

Return all attributes that correspond to given filtering parameters.

Return all attributes that correspond to given filtering parameters.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
filter = 'filter_example' # str | JSON-encoded filter query in DNF as [clause OR clause...]

try:
    # Return all attributes that correspond to given filtering parameters.
    api_instance.group_external_attributes_default(filter)
except ApiException as e:
    print("Exception when calling DefaultApi->group_external_attributes_default: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| JSON-encoded filter query in DNF as [clause OR clause...] | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_external_attributes_remove**
> group_external_attributes_remove(id)

Remove selected attribute

Remove selected attribute

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | 

try:
    # Remove selected attribute
    api_instance.group_external_attributes_remove(id)
except ApiException as e:
    print("Exception when calling DefaultApi->group_external_attributes_remove: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_invitations_accept**
> group_invitations_accept(id)

Allow the current user to join the corresponding group using the invitation.

Allow the current user to join the corresponding group using the invitation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | 

try:
    # Allow the current user to join the corresponding group using the invitation.
    api_instance.group_invitations_accept(id)
except ApiException as e:
    print("Exception when calling DefaultApi->group_invitations_accept: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_invitations_create**
> group_invitations_create(group_id, body=body)

Create a new invitation for given group.

Create a new invitation for given group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
group_id = 'group_id_example' # str | 
body = swagger_client.GroupIdInvitationsBody() # GroupIdInvitationsBody |  (optional)

try:
    # Create a new invitation for given group.
    api_instance.group_invitations_create(group_id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->group_invitations_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 
 **body** | [**GroupIdInvitationsBody**](GroupIdInvitationsBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_invitations_default**
> group_invitations_default(id)

Return invitation details including all relevant group entities (so a name can be constructed).

Return invitation details including all relevant group entities (so a name can be constructed).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | 

try:
    # Return invitation details including all relevant group entities (so a name can be constructed).
    api_instance.group_invitations_default(id)
except ApiException as e:
    print("Exception when calling DefaultApi->group_invitations_default: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_invitations_list**
> group_invitations_list(group_id)

List all invitations of a group.

List all invitations of a group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
group_id = 'group_id_example' # str | 

try:
    # List all invitations of a group.
    api_instance.group_invitations_list(group_id)
except ApiException as e:
    print("Exception when calling DefaultApi->group_invitations_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **group_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_invitations_remove**
> group_invitations_remove(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | 

try:
    api_instance.group_invitations_remove(id)
except ApiException as e:
    print("Exception when calling DefaultApi->group_invitations_remove: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **group_invitations_update**
> group_invitations_update(id, body=body)

Edit the invitation.

Edit the invitation.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | 
body = swagger_client.GroupinvitationsIdBody() # GroupinvitationsIdBody |  (optional)

try:
    # Edit the invitation.
    api_instance.group_invitations_update(id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->group_invitations_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**GroupinvitationsIdBody**](GroupinvitationsIdBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_add_group**
> groups_add_group(body=body)

Create a new group

Create a new group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.V1GroupsBody() # V1GroupsBody |  (optional)

try:
    # Create a new group
    api_instance.groups_add_group(body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->groups_add_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1GroupsBody**](V1GroupsBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_add_member**
> groups_add_member(id, user_id, body=body)

Add/update a membership (other than student) for given user

Add/update a membership (other than student) for given user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the group
user_id = 'user_id_example' # str | Identifier of the supervisor
body = swagger_client.MembersUserIdBody() # MembersUserIdBody |  (optional)

try:
    # Add/update a membership (other than student) for given user
    api_instance.groups_add_member(id, user_id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->groups_add_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the group | 
 **user_id** | **str**| Identifier of the supervisor | 
 **body** | [**MembersUserIdBody**](MembersUserIdBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_add_student**
> groups_add_student(id, user_id)

Add a student to a group

Add a student to a group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the group
user_id = 'user_id_example' # str | Identifier of the student

try:
    # Add a student to a group
    api_instance.groups_add_student(id, user_id)
except ApiException as e:
    print("Exception when calling DefaultApi->groups_add_student: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the group | 
 **user_id** | **str**| Identifier of the student | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_assignments**
> groups_assignments(id)

Get all exercise assignments for a group

Get all exercise assignments for a group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the group

try:
    # Get all exercise assignments for a group
    api_instance.groups_assignments(id)
except ApiException as e:
    print("Exception when calling DefaultApi->groups_assignments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the group | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_default**
> groups_default(instance_id=instance_id, ancestors=ancestors, search=search, archived=archived, only_archived=only_archived)

Get a list of all non-archived groups a user can see. The return set is filtered by parameters.

Get a list of all non-archived groups a user can see. The return set is filtered by parameters.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
instance_id = 'instance_id_example' # str | Only groups of this instance are returned. (optional)
ancestors = true # bool | If true, returns an ancestral closure of the initial result set. Included ancestral groups do not respect other filters (archived, search, ...). (optional)
search = 'search_example' # str | Search string. Only groups containing this string as a substring of their names are returned. (optional)
archived = true # bool | Include also archived groups in the result. (optional)
only_archived = true # bool | Automatically implies $archived flag and returns only archived groups. (optional)

try:
    # Get a list of all non-archived groups a user can see. The return set is filtered by parameters.
    api_instance.groups_default(instance_id=instance_id, ancestors=ancestors, search=search, archived=archived, only_archived=only_archived)
except ApiException as e:
    print("Exception when calling DefaultApi->groups_default: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_id** | **str**| Only groups of this instance are returned. | [optional] 
 **ancestors** | **bool**| If true, returns an ancestral closure of the initial result set. Included ancestral groups do not respect other filters (archived, search, ...). | [optional] 
 **search** | **str**| Search string. Only groups containing this string as a substring of their names are returned. | [optional] 
 **archived** | **bool**| Include also archived groups in the result. | [optional] 
 **only_archived** | **bool**| Automatically implies $archived flag and returns only archived groups. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_detail**
> groups_detail(id)

Get details of a group

Get details of a group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the group

try:
    # Get details of a group
    api_instance.groups_detail(id)
except ApiException as e:
    print("Exception when calling DefaultApi->groups_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the group | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_get_exam_locks**
> groups_get_exam_locks(id, exam_id)

Retrieve a list of locks for given exam

Retrieve a list of locks for given exam

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | An identifier of the related group
exam_id = 56 # int | An identifier of the exam

try:
    # Retrieve a list of locks for given exam
    api_instance.groups_get_exam_locks(id, exam_id)
except ApiException as e:
    print("Exception when calling DefaultApi->groups_get_exam_locks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An identifier of the related group | 
 **exam_id** | **int**| An identifier of the exam | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_lock_student**
> groups_lock_student(id, user_id)

Lock student in a group and with an IP from which the request was made.

Lock student in a group and with an IP from which the request was made.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the group
user_id = 'user_id_example' # str | Identifier of the student

try:
    # Lock student in a group and with an IP from which the request was made.
    api_instance.groups_lock_student(id, user_id)
except ApiException as e:
    print("Exception when calling DefaultApi->groups_lock_student: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the group | 
 **user_id** | **str**| Identifier of the student | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_members**
> groups_members(id)

Get a list of members of a group

Get a list of members of a group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the group

try:
    # Get a list of members of a group
    api_instance.groups_members(id)
except ApiException as e:
    print("Exception when calling DefaultApi->groups_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the group | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_relocate**
> groups_relocate(id, new_parent_id)

Relocate the group under a different parent.

Relocate the group under a different parent.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | An identifier of the relocated group
new_parent_id = 'new_parent_id_example' # str | An identifier of the new parent group

try:
    # Relocate the group under a different parent.
    api_instance.groups_relocate(id, new_parent_id)
except ApiException as e:
    print("Exception when calling DefaultApi->groups_relocate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An identifier of the relocated group | 
 **new_parent_id** | **str**| An identifier of the new parent group | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_remove_exam_period**
> groups_remove_exam_period(id)

Change the group back to regular group (remove information about an exam).

Change the group back to regular group (remove information about an exam).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | An identifier of the updated group

try:
    # Change the group back to regular group (remove information about an exam).
    api_instance.groups_remove_exam_period(id)
except ApiException as e:
    print("Exception when calling DefaultApi->groups_remove_exam_period: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An identifier of the updated group | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_remove_group**
> groups_remove_group(id)

Delete a group

Delete a group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the group

try:
    # Delete a group
    api_instance.groups_remove_group(id)
except ApiException as e:
    print("Exception when calling DefaultApi->groups_remove_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the group | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_remove_member**
> groups_remove_member(id, user_id)

Remove a member (other than student) from a group

Remove a member (other than student) from a group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the group
user_id = 'user_id_example' # str | Identifier of the supervisor

try:
    # Remove a member (other than student) from a group
    api_instance.groups_remove_member(id, user_id)
except ApiException as e:
    print("Exception when calling DefaultApi->groups_remove_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the group | 
 **user_id** | **str**| Identifier of the supervisor | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_remove_student**
> groups_remove_student(id, user_id)

Remove a student from a group

Remove a student from a group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the group
user_id = 'user_id_example' # str | Identifier of the student

try:
    # Remove a student from a group
    api_instance.groups_remove_student(id, user_id)
except ApiException as e:
    print("Exception when calling DefaultApi->groups_remove_student: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the group | 
 **user_id** | **str**| Identifier of the student | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_set_archived**
> groups_set_archived(id, body=body)

Set the 'isArchived' flag for a group

Set the 'isArchived' flag for a group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | An identifier of the updated group
body = swagger_client.IdArchivedBody1() # IdArchivedBody1 |  (optional)

try:
    # Set the 'isArchived' flag for a group
    api_instance.groups_set_archived(id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->groups_set_archived: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An identifier of the updated group | 
 **body** | [**IdArchivedBody1**](IdArchivedBody1.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_set_exam_period**
> groups_set_exam_period(id, body=body)

Set an examination period (in the future) when the group will be secured for submitting. Only locked students may submit solutions in the group during this period. This endpoint is also used to update already planned exam period, but only dates in the future can be editted (e.g., once an exam begins, the beginning may no longer be updated).

Set an examination period (in the future) when the group will be secured for submitting. Only locked students may submit solutions in the group during this period. This endpoint is also used to update already planned exam period, but only dates in the future can be editted (e.g., once an exam begins, the beginning may no longer be updated).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | An identifier of the updated group
body = swagger_client.IdExamPeriodBody() # IdExamPeriodBody |  (optional)

try:
    # Set an examination period (in the future) when the group will be secured for submitting. Only locked students may submit solutions in the group during this period. This endpoint is also used to update already planned exam period, but only dates in the future can be editted (e.g., once an exam begins, the beginning may no longer be updated).
    api_instance.groups_set_exam_period(id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->groups_set_exam_period: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An identifier of the updated group | 
 **body** | [**IdExamPeriodBody**](IdExamPeriodBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_set_organizational**
> groups_set_organizational(id, body=body)

Set the 'isOrganizational' flag for a group

Set the 'isOrganizational' flag for a group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | An identifier of the updated group
body = swagger_client.IdOrganizationalBody() # IdOrganizationalBody |  (optional)

try:
    # Set the 'isOrganizational' flag for a group
    api_instance.groups_set_organizational(id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->groups_set_organizational: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An identifier of the updated group | 
 **body** | [**IdOrganizationalBody**](IdOrganizationalBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_shadow_assignments**
> groups_shadow_assignments(id)

Get all shadow assignments for a group

Get all shadow assignments for a group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the group

try:
    # Get all shadow assignments for a group
    api_instance.groups_shadow_assignments(id)
except ApiException as e:
    print("Exception when calling DefaultApi->groups_shadow_assignments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the group | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_stats**
> groups_stats(id)

Get statistics of a group. If the user does not have the rights to view all of these, try to at least return their statistics.

Get statistics of a group. If the user does not have the rights to view all of these, try to at least return their statistics.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the group

try:
    # Get statistics of a group. If the user does not have the rights to view all of these, try to at least return their statistics.
    api_instance.groups_stats(id)
except ApiException as e:
    print("Exception when calling DefaultApi->groups_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the group | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_students_solutions**
> groups_students_solutions(id, user_id)

Get all solutions of a single student from all assignments in a group

Get all solutions of a single student from all assignments in a group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the group
user_id = 'user_id_example' # str | Identifier of the student

try:
    # Get all solutions of a single student from all assignments in a group
    api_instance.groups_students_solutions(id, user_id)
except ApiException as e:
    print("Exception when calling DefaultApi->groups_students_solutions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the group | 
 **user_id** | **str**| Identifier of the student | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_students_stats**
> groups_students_stats(id, user_id)

Get statistics of a single student in a group

Get statistics of a single student in a group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the group
user_id = 'user_id_example' # str | Identifier of the student

try:
    # Get statistics of a single student in a group
    api_instance.groups_students_stats(id, user_id)
except ApiException as e:
    print("Exception when calling DefaultApi->groups_students_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the group | 
 **user_id** | **str**| Identifier of the student | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_subgroups**
> groups_subgroups(id)

Get a list of subgroups of a group

Get a list of subgroups of a group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the group

try:
    # Get a list of subgroups of a group
    api_instance.groups_subgroups(id)
except ApiException as e:
    print("Exception when calling DefaultApi->groups_subgroups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the group | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_unlock_student**
> groups_unlock_student(id, user_id)

Unlock a student currently locked in a group.

Unlock a student currently locked in a group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the group
user_id = 'user_id_example' # str | Identifier of the student

try:
    # Unlock a student currently locked in a group.
    api_instance.groups_unlock_student(id, user_id)
except ApiException as e:
    print("Exception when calling DefaultApi->groups_unlock_student: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the group | 
 **user_id** | **str**| Identifier of the student | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_update_group**
> groups_update_group(id, body=body)

Update group info

Update group info

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | An identifier of the updated group
body = swagger_client.GroupsIdBody() # GroupsIdBody |  (optional)

try:
    # Update group info
    api_instance.groups_update_group(id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->groups_update_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An identifier of the updated group | 
 **body** | [**GroupsIdBody**](GroupsIdBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **groups_validate_add_group_data**
> groups_validate_add_group_data(body=body)

Validate group creation data

Validate group creation data

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.GroupsValidateaddgroupdataBody() # GroupsValidateaddgroupdataBody |  (optional)

try:
    # Validate group creation data
    api_instance.groups_validate_add_group_data(body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->groups_validate_add_group_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GroupsValidateaddgroupdataBody**](GroupsValidateaddgroupdataBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **hardware_groups_default**
> hardware_groups_default()

Get a list of all hardware groups in system

Get a list of all hardware groups in system

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    # Get a list of all hardware groups in system
    api_instance.hardware_groups_default()
except ApiException as e:
    print("Exception when calling DefaultApi->hardware_groups_default: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instances_create_instance**
> instances_create_instance(body=body)

Create a new instance

Create a new instance

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.V1InstancesBody() # V1InstancesBody |  (optional)

try:
    # Create a new instance
    api_instance.instances_create_instance(body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->instances_create_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1InstancesBody**](V1InstancesBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instances_create_licence**
> instances_create_licence(id, body=body)

Create a new license for an instance

Create a new license for an instance

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | An identifier of the instance
body = swagger_client.IdLicencesBody() # IdLicencesBody |  (optional)

try:
    # Create a new license for an instance
    api_instance.instances_create_licence(id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->instances_create_licence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An identifier of the instance | 
 **body** | [**IdLicencesBody**](IdLicencesBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instances_default**
> instances_default()

Get a list of all instances

Get a list of all instances

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    # Get a list of all instances
    api_instance.instances_default()
except ApiException as e:
    print("Exception when calling DefaultApi->instances_default: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instances_delete_instance**
> instances_delete_instance(id)

Delete an instance

Delete an instance

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | An identifier of the instance to be deleted

try:
    # Delete an instance
    api_instance.instances_delete_instance(id)
except ApiException as e:
    print("Exception when calling DefaultApi->instances_delete_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An identifier of the instance to be deleted | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instances_delete_licence**
> instances_delete_licence(licence_id)

Remove existing license for an instance

Remove existing license for an instance

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
licence_id = 'licence_id_example' # str | Identifier of the licence

try:
    # Remove existing license for an instance
    api_instance.instances_delete_licence(licence_id)
except ApiException as e:
    print("Exception when calling DefaultApi->instances_delete_licence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **licence_id** | **str**| Identifier of the licence | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instances_detail**
> instances_detail(id)

Get details of an instance

Get details of an instance

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | An identifier of the instance

try:
    # Get details of an instance
    api_instance.instances_detail(id)
except ApiException as e:
    print("Exception when calling DefaultApi->instances_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An identifier of the instance | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instances_licences**
> instances_licences(id)

Get a list of licenses associated with an instance

Get a list of licenses associated with an instance

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | An identifier of the instance

try:
    # Get a list of licenses associated with an instance
    api_instance.instances_licences(id)
except ApiException as e:
    print("Exception when calling DefaultApi->instances_licences: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An identifier of the instance | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instances_update_instance**
> instances_update_instance(id, body=body)

Update an instance

Update an instance

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | An identifier of the updated instance
body = swagger_client.InstancesIdBody() # InstancesIdBody |  (optional)

try:
    # Update an instance
    api_instance.instances_update_instance(id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->instances_update_instance: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An identifier of the updated instance | 
 **body** | [**InstancesIdBody**](InstancesIdBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **instances_update_licence**
> instances_update_licence(licence_id, body=body)

Update an existing license for an instance

Update an existing license for an instance

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
licence_id = 'licence_id_example' # str | Identifier of the licence
body = swagger_client.LicencesLicenceIdBody() # LicencesLicenceIdBody |  (optional)

try:
    # Update an existing license for an instance
    api_instance.instances_update_licence(licence_id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->instances_update_licence: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **licence_id** | **str**| Identifier of the licence | 
 **body** | [**LicencesLicenceIdBody**](LicencesLicenceIdBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_default**
> login_default(body=body)

Log in using user credentials

Log in using user credentials

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.V1LoginBody() # V1LoginBody |  (optional)

try:
    # Log in using user credentials
    api_instance.login_default(body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->login_default: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1LoginBody**](V1LoginBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_external**
> login_external(authenticator_name, body=body)

Log in using an external authentication service

Log in using an external authentication service

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
authenticator_name = 'authenticator_name_example' # str | Identifier of the external authenticator
body = swagger_client.LoginAuthenticatorNameBody() # LoginAuthenticatorNameBody |  (optional)

try:
    # Log in using an external authentication service
    api_instance.login_external(authenticator_name, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->login_external: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authenticator_name** | **str**| Identifier of the external authenticator | 
 **body** | [**LoginAuthenticatorNameBody**](LoginAuthenticatorNameBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_issue_restricted_token**
> login_issue_restricted_token(body=body)

Issue a new access token with a restricted set of scopes

Issue a new access token with a restricted set of scopes

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.LoginIssuerestrictedtokenBody() # LoginIssuerestrictedtokenBody |  (optional)

try:
    # Issue a new access token with a restricted set of scopes
    api_instance.login_issue_restricted_token(body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->login_issue_restricted_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LoginIssuerestrictedtokenBody**](LoginIssuerestrictedtokenBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_refresh**
> login_refresh()

Refresh the access token of current user

Refresh the access token of current user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    # Refresh the access token of current user
    api_instance.login_refresh()
except ApiException as e:
    print("Exception when calling DefaultApi->login_refresh: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_take_over**
> login_take_over(user_id)

Takeover user account with specified user identification.

Takeover user account with specified user identification.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
user_id = 'user_id_example' # str | 

try:
    # Takeover user account with specified user identification.
    api_instance.login_take_over(user_id)
except ApiException as e:
    print("Exception when calling DefaultApi->login_take_over: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notifications_all**
> notifications_all()

Get all notifications in the system.

Get all notifications in the system.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    # Get all notifications in the system.
    api_instance.notifications_all()
except ApiException as e:
    print("Exception when calling DefaultApi->notifications_all: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notifications_create**
> notifications_create(body=body)

Create notification with given attributes

Create notification with given attributes

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.V1NotificationsBody() # V1NotificationsBody |  (optional)

try:
    # Create notification with given attributes
    api_instance.notifications_create(body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->notifications_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1NotificationsBody**](V1NotificationsBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notifications_default**
> notifications_default(groups_ids=groups_ids)

Get all notifications which are currently active. If groupsIds is given returns only the ones from given groups (and their ancestors) and global ones (without group).

Get all notifications which are currently active. If groupsIds is given returns only the ones from given groups (and their ancestors) and global ones (without group).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
groups_ids = NULL # list[object] | identifications of groups (optional)

try:
    # Get all notifications which are currently active. If groupsIds is given returns only the ones from given groups (and their ancestors) and global ones (without group).
    api_instance.notifications_default(groups_ids=groups_ids)
except ApiException as e:
    print("Exception when calling DefaultApi->notifications_default: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **groups_ids** | [**list[object]**](object.md)| identifications of groups | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notifications_remove**
> notifications_remove(id)

Delete a notification

Delete a notification

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | 

try:
    # Delete a notification
    api_instance.notifications_remove(id)
except ApiException as e:
    print("Exception when calling DefaultApi->notifications_remove: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **notifications_update**
> notifications_update(id, body=body)

Update notification

Update notification

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | 
body = swagger_client.NotificationsIdBody() # NotificationsIdBody |  (optional)

try:
    # Update notification
    api_instance.notifications_update(id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->notifications_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**NotificationsIdBody**](NotificationsIdBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipelines_create_pipeline**
> pipelines_create_pipeline(body=body)

Create a brand new pipeline.

Create a brand new pipeline.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.V1PipelinesBody() # V1PipelinesBody |  (optional)

try:
    # Create a brand new pipeline.
    api_instance.pipelines_create_pipeline(body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->pipelines_create_pipeline: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1PipelinesBody**](V1PipelinesBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipelines_default**
> pipelines_default(offset=offset, limit=limit, order_by=order_by, filters=filters, locale=locale)

Get a list of pipelines with an optional filter, ordering, and pagination pruning. The result conforms to pagination protocol.

Get a list of pipelines with an optional filter, ordering, and pagination pruning. The result conforms to pagination protocol.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
offset = 56 # int | Index of the first result. (optional)
limit = 56 # int | Maximal number of results returned. (optional)
order_by = 'order_by_example' # str | Name of the column (column concept). The '!' prefix indicate descending order. (optional)
filters = NULL # list[object] | Named filters that prune the result. (optional)
locale = 'locale_example' # str | Currently set locale (used to augment order by clause if necessary), (optional)

try:
    # Get a list of pipelines with an optional filter, ordering, and pagination pruning. The result conforms to pagination protocol.
    api_instance.pipelines_default(offset=offset, limit=limit, order_by=order_by, filters=filters, locale=locale)
except ApiException as e:
    print("Exception when calling DefaultApi->pipelines_default: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Index of the first result. | [optional] 
 **limit** | **int**| Maximal number of results returned. | [optional] 
 **order_by** | **str**| Name of the column (column concept). The &#x27;!&#x27; prefix indicate descending order. | [optional] 
 **filters** | [**list[object]**](object.md)| Named filters that prune the result. | [optional] 
 **locale** | **str**| Currently set locale (used to augment order by clause if necessary), | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipelines_delete_supplementary_file**
> pipelines_delete_supplementary_file(id, file_id)

Delete supplementary pipeline file with given id

Delete supplementary pipeline file with given id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | identification of pipeline
file_id = 'file_id_example' # str | identification of file

try:
    # Delete supplementary pipeline file with given id
    api_instance.pipelines_delete_supplementary_file(id, file_id)
except ApiException as e:
    print("Exception when calling DefaultApi->pipelines_delete_supplementary_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identification of pipeline | 
 **file_id** | **str**| identification of file | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipelines_fork_pipeline**
> pipelines_fork_pipeline(id, body=body)

Create a complete copy of given pipeline.

Create a complete copy of given pipeline.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | identification of pipeline to be copied
body = swagger_client.IdForkBody1() # IdForkBody1 |  (optional)

try:
    # Create a complete copy of given pipeline.
    api_instance.pipelines_fork_pipeline(id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->pipelines_fork_pipeline: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identification of pipeline to be copied | 
 **body** | [**IdForkBody1**](IdForkBody1.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipelines_get_default_boxes**
> pipelines_get_default_boxes()

Get a list of default boxes which might be used in pipeline.

Get a list of default boxes which might be used in pipeline.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    # Get a list of default boxes which might be used in pipeline.
    api_instance.pipelines_get_default_boxes()
except ApiException as e:
    print("Exception when calling DefaultApi->pipelines_get_default_boxes: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipelines_get_pipeline**
> pipelines_get_pipeline(id)

Get pipeline based on given identification.

Get pipeline based on given identification.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the pipeline

try:
    # Get pipeline based on given identification.
    api_instance.pipelines_get_pipeline(id)
except ApiException as e:
    print("Exception when calling DefaultApi->pipelines_get_pipeline: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the pipeline | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipelines_get_pipeline_exercises**
> pipelines_get_pipeline_exercises(id)

Get all exercises that use given pipeline. Only bare minimum is retrieved for each exercise (localized name and author).

Get all exercises that use given pipeline. Only bare minimum is retrieved for each exercise (localized name and author).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the pipeline

try:
    # Get all exercises that use given pipeline. Only bare minimum is retrieved for each exercise (localized name and author).
    api_instance.pipelines_get_pipeline_exercises(id)
except ApiException as e:
    print("Exception when calling DefaultApi->pipelines_get_pipeline_exercises: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the pipeline | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipelines_get_supplementary_files**
> pipelines_get_supplementary_files(id)

Get list of all supplementary files for a pipeline

Get list of all supplementary files for a pipeline

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | identification of pipeline

try:
    # Get list of all supplementary files for a pipeline
    api_instance.pipelines_get_supplementary_files(id)
except ApiException as e:
    print("Exception when calling DefaultApi->pipelines_get_supplementary_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identification of pipeline | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipelines_remove_pipeline**
> pipelines_remove_pipeline(id)

Delete an pipeline

Delete an pipeline

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | 

try:
    # Delete an pipeline
    api_instance.pipelines_remove_pipeline(id)
except ApiException as e:
    print("Exception when calling DefaultApi->pipelines_remove_pipeline: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipelines_update_pipeline**
> pipelines_update_pipeline(id, body=body)

Update pipeline with given data.

Update pipeline with given data.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the pipeline
body = swagger_client.PipelinesIdBody() # PipelinesIdBody |  (optional)

try:
    # Update pipeline with given data.
    api_instance.pipelines_update_pipeline(id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->pipelines_update_pipeline: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the pipeline | 
 **body** | [**PipelinesIdBody**](PipelinesIdBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipelines_update_runtime_environments**
> pipelines_update_runtime_environments(id)

Set runtime environments associated with given pipeline.

Set runtime environments associated with given pipeline.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the pipeline

try:
    # Set runtime environments associated with given pipeline.
    api_instance.pipelines_update_runtime_environments(id)
except ApiException as e:
    print("Exception when calling DefaultApi->pipelines_update_runtime_environments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the pipeline | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipelines_upload_supplementary_files**
> pipelines_upload_supplementary_files(id, body=body)

Associate supplementary files with a pipeline and upload them to remote file server

Associate supplementary files with a pipeline and upload them to remote file server

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | identification of pipeline
body = swagger_client.IdSupplementaryfilesBody1() # IdSupplementaryfilesBody1 |  (optional)

try:
    # Associate supplementary files with a pipeline and upload them to remote file server
    api_instance.pipelines_upload_supplementary_files(id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->pipelines_upload_supplementary_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identification of pipeline | 
 **body** | [**IdSupplementaryfilesBody1**](IdSupplementaryfilesBody1.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **pipelines_validate_pipeline**
> pipelines_validate_pipeline(id, body=body)

Check if the version of the pipeline is up-to-date.

Check if the version of the pipeline is up-to-date.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the pipeline
body = swagger_client.IdValidateBody2() # IdValidateBody2 |  (optional)

try:
    # Check if the version of the pipeline is up-to-date.
    api_instance.pipelines_validate_pipeline(id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->pipelines_validate_pipeline: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the pipeline | 
 **body** | [**IdValidateBody2**](IdValidateBody2.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **plagiarism_add_similarities**
> plagiarism_add_similarities(id, solution_id, body=body)

Appends one detected similarity record (similarities associated with one file and one other author) into a detected batch. This division was selected to make the appends relatively small and managable.

Appends one detected similarity record (similarities associated with one file and one other author) into a detected batch. This division was selected to make the appends relatively small and managable.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | 
solution_id = 'solution_id_example' # str | 
body = swagger_client.IdSolutionIdBody() # IdSolutionIdBody |  (optional)

try:
    # Appends one detected similarity record (similarities associated with one file and one other author) into a detected batch. This division was selected to make the appends relatively small and managable.
    api_instance.plagiarism_add_similarities(id, solution_id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->plagiarism_add_similarities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **solution_id** | **str**|  | 
 **body** | [**IdSolutionIdBody**](IdSolutionIdBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **plagiarism_batch_detail**
> plagiarism_batch_detail(id)

Fetch a detail of a particular batch record.

Fetch a detail of a particular batch record.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | 

try:
    # Fetch a detail of a particular batch record.
    api_instance.plagiarism_batch_detail(id)
except ApiException as e:
    print("Exception when calling DefaultApi->plagiarism_batch_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **plagiarism_create_batch**
> plagiarism_create_batch(body=body)

Create new detection batch record

Create new detection batch record

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.V1PlagiarismBody() # V1PlagiarismBody |  (optional)

try:
    # Create new detection batch record
    api_instance.plagiarism_create_batch(body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->plagiarism_create_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1PlagiarismBody**](V1PlagiarismBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **plagiarism_get_similarities**
> plagiarism_get_similarities(id, solution_id)

Retrieve detected plagiarism records from a specific batch related to one solution. Returns a list of detected similarities entities (similar file records are nested within).

Retrieve detected plagiarism records from a specific batch related to one solution. Returns a list of detected similarities entities (similar file records are nested within).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | 
solution_id = 'solution_id_example' # str | 

try:
    # Retrieve detected plagiarism records from a specific batch related to one solution. Returns a list of detected similarities entities (similar file records are nested within).
    api_instance.plagiarism_get_similarities(id, solution_id)
except ApiException as e:
    print("Exception when calling DefaultApi->plagiarism_get_similarities: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **solution_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **plagiarism_list_batches**
> plagiarism_list_batches(detection_tool=detection_tool, solution_id=solution_id)

Get a list of all batches, optionally filtered by query params.

Get a list of all batches, optionally filtered by query params.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
detection_tool = 'detection_tool_example' # str | Requests only batches created by a particular detection tool. (optional)
solution_id = 'solution_id_example' # str | Requests only batches where particular solution has detected similarities. (optional)

try:
    # Get a list of all batches, optionally filtered by query params.
    api_instance.plagiarism_list_batches(detection_tool=detection_tool, solution_id=solution_id)
except ApiException as e:
    print("Exception when calling DefaultApi->plagiarism_list_batches: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **detection_tool** | **str**| Requests only batches created by a particular detection tool. | [optional] 
 **solution_id** | **str**| Requests only batches where particular solution has detected similarities. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **plagiarism_update_batch**
> plagiarism_update_batch(id, body=body)

Update dectection bath record. At the momeny, only the uploadCompletedAt can be changed.

Update dectection bath record. At the momeny, only the uploadCompletedAt can be changed.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | 
body = swagger_client.PlagiarismIdBody() # PlagiarismIdBody |  (optional)

try:
    # Update dectection bath record. At the momeny, only the uploadCompletedAt can be changed.
    api_instance.plagiarism_update_batch(id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->plagiarism_update_batch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**PlagiarismIdBody**](PlagiarismIdBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reference_exercise_solutions_delete_reference_solution**
> reference_exercise_solutions_delete_reference_solution(solution_id)

Delete reference solution with given identification.

Delete reference solution with given identification.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
solution_id = 'solution_id_example' # str | identifier of reference solution

try:
    # Delete reference solution with given identification.
    api_instance.reference_exercise_solutions_delete_reference_solution(solution_id)
except ApiException as e:
    print("Exception when calling DefaultApi->reference_exercise_solutions_delete_reference_solution: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **solution_id** | **str**| identifier of reference solution | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reference_exercise_solutions_delete_submission**
> reference_exercise_solutions_delete_submission(submission_id)

Remove reference solution evaluation (submission) permanently.

Remove reference solution evaluation (submission) permanently.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
submission_id = 'submission_id_example' # str | Identifier of the reference solution submission

try:
    # Remove reference solution evaluation (submission) permanently.
    api_instance.reference_exercise_solutions_delete_submission(submission_id)
except ApiException as e:
    print("Exception when calling DefaultApi->reference_exercise_solutions_delete_submission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submission_id** | **str**| Identifier of the reference solution submission | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reference_exercise_solutions_detail**
> reference_exercise_solutions_detail(solution_id)

Get details of a reference solution

Get details of a reference solution

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
solution_id = 'solution_id_example' # str | An identifier of the solution

try:
    # Get details of a reference solution
    api_instance.reference_exercise_solutions_detail(solution_id)
except ApiException as e:
    print("Exception when calling DefaultApi->reference_exercise_solutions_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **solution_id** | **str**| An identifier of the solution | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reference_exercise_solutions_download_result_archive**
> reference_exercise_solutions_download_result_archive(submission_id)

Download result archive from backend for a reference solution evaluation

Download result archive from backend for a reference solution evaluation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
submission_id = 'submission_id_example' # str | 

try:
    # Download result archive from backend for a reference solution evaluation
    api_instance.reference_exercise_solutions_download_result_archive(submission_id)
except ApiException as e:
    print("Exception when calling DefaultApi->reference_exercise_solutions_download_result_archive: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submission_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reference_exercise_solutions_download_solution_archive**
> reference_exercise_solutions_download_solution_archive(solution_id)

Download archive containing all solution files for particular reference solution.

Download archive containing all solution files for particular reference solution.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
solution_id = 'solution_id_example' # str | of reference solution

try:
    # Download archive containing all solution files for particular reference solution.
    api_instance.reference_exercise_solutions_download_solution_archive(solution_id)
except ApiException as e:
    print("Exception when calling DefaultApi->reference_exercise_solutions_download_solution_archive: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **solution_id** | **str**| of reference solution | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reference_exercise_solutions_evaluation_score_config**
> reference_exercise_solutions_evaluation_score_config(submission_id)

Get score configuration associated with given submission evaluation

Get score configuration associated with given submission evaluation

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
submission_id = 'submission_id_example' # str | identifier of the reference exercise submission

try:
    # Get score configuration associated with given submission evaluation
    api_instance.reference_exercise_solutions_evaluation_score_config(submission_id)
except ApiException as e:
    print("Exception when calling DefaultApi->reference_exercise_solutions_evaluation_score_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submission_id** | **str**| identifier of the reference exercise submission | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reference_exercise_solutions_files**
> reference_exercise_solutions_files(id)

Get the list of submitted files of the solution.

Get the list of submitted files of the solution.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | of reference solution

try:
    # Get the list of submitted files of the solution.
    api_instance.reference_exercise_solutions_files(id)
except ApiException as e:
    print("Exception when calling DefaultApi->reference_exercise_solutions_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| of reference solution | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reference_exercise_solutions_pre_submit**
> reference_exercise_solutions_pre_submit(exercise_id, body=body)

Pre submit action which will, based on given files, detect possible runtime environments for the exercise. Also it can be further used for entry points and other important things that should be provided by user during submit.

Pre submit action which will, based on given files, detect possible runtime environments for the exercise. Also it can be further used for entry points and other important things that should be provided by user during submit.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
exercise_id = 'exercise_id_example' # str | identifier of exercise
body = swagger_client.ExerciseIdPresubmitBody() # ExerciseIdPresubmitBody |  (optional)

try:
    # Pre submit action which will, based on given files, detect possible runtime environments for the exercise. Also it can be further used for entry points and other important things that should be provided by user during submit.
    api_instance.reference_exercise_solutions_pre_submit(exercise_id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->reference_exercise_solutions_pre_submit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exercise_id** | **str**| identifier of exercise | 
 **body** | [**ExerciseIdPresubmitBody**](ExerciseIdPresubmitBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reference_exercise_solutions_resubmit**
> reference_exercise_solutions_resubmit(id, body=body)

Evaluate a single reference exercise solution for all configured hardware groups

Evaluate a single reference exercise solution for all configured hardware groups

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the reference solution
body = swagger_client.IdResubmitBody() # IdResubmitBody |  (optional)

try:
    # Evaluate a single reference exercise solution for all configured hardware groups
    api_instance.reference_exercise_solutions_resubmit(id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->reference_exercise_solutions_resubmit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the reference solution | 
 **body** | [**IdResubmitBody**](IdResubmitBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reference_exercise_solutions_resubmit_all**
> reference_exercise_solutions_resubmit_all(exercise_id, body=body)

Evaluate all reference solutions for an exercise (and for all configured hardware groups).

Evaluate all reference solutions for an exercise (and for all configured hardware groups).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
exercise_id = 'exercise_id_example' # str | Identifier of the exercise
body = swagger_client.ExerciseIdResubmitallBody() # ExerciseIdResubmitallBody |  (optional)

try:
    # Evaluate all reference solutions for an exercise (and for all configured hardware groups).
    api_instance.reference_exercise_solutions_resubmit_all(exercise_id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->reference_exercise_solutions_resubmit_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exercise_id** | **str**| Identifier of the exercise | 
 **body** | [**ExerciseIdResubmitallBody**](ExerciseIdResubmitallBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reference_exercise_solutions_set_visibility**
> reference_exercise_solutions_set_visibility(solution_id, body=body)

Set visibility of given reference solution.

Set visibility of given reference solution.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
solution_id = 'solution_id_example' # str | of reference solution
body = swagger_client.SolutionIdVisibilityBody() # SolutionIdVisibilityBody |  (optional)

try:
    # Set visibility of given reference solution.
    api_instance.reference_exercise_solutions_set_visibility(solution_id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->reference_exercise_solutions_set_visibility: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **solution_id** | **str**| of reference solution | 
 **body** | [**SolutionIdVisibilityBody**](SolutionIdVisibilityBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reference_exercise_solutions_solutions**
> reference_exercise_solutions_solutions(exercise_id)

Get reference solutions for an exercise

Get reference solutions for an exercise

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
exercise_id = 'exercise_id_example' # str | Identifier of the exercise

try:
    # Get reference solutions for an exercise
    api_instance.reference_exercise_solutions_solutions(exercise_id)
except ApiException as e:
    print("Exception when calling DefaultApi->reference_exercise_solutions_solutions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exercise_id** | **str**| Identifier of the exercise | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reference_exercise_solutions_submission**
> reference_exercise_solutions_submission(submission_id)

Get reference solution evaluation (i.e., submission) for an exercise solution.

Get reference solution evaluation (i.e., submission) for an exercise solution.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
submission_id = 'submission_id_example' # str | identifier of the reference exercise submission

try:
    # Get reference solution evaluation (i.e., submission) for an exercise solution.
    api_instance.reference_exercise_solutions_submission(submission_id)
except ApiException as e:
    print("Exception when calling DefaultApi->reference_exercise_solutions_submission: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **submission_id** | **str**| identifier of the reference exercise submission | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reference_exercise_solutions_submissions**
> reference_exercise_solutions_submissions(solution_id)

Get a list of submissions for given reference solution.

Get a list of submissions for given reference solution.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
solution_id = 'solution_id_example' # str | identifier of the reference exercise solution

try:
    # Get a list of submissions for given reference solution.
    api_instance.reference_exercise_solutions_submissions(solution_id)
except ApiException as e:
    print("Exception when calling DefaultApi->reference_exercise_solutions_submissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **solution_id** | **str**| identifier of the reference exercise solution | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reference_exercise_solutions_submit**
> reference_exercise_solutions_submit(exercise_id, body=body)

Add new reference solution to an exercise

Add new reference solution to an exercise

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
exercise_id = 'exercise_id_example' # str | Identifier of the exercise
body = swagger_client.ExerciseIdSubmitBody() # ExerciseIdSubmitBody |  (optional)

try:
    # Add new reference solution to an exercise
    api_instance.reference_exercise_solutions_submit(exercise_id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->reference_exercise_solutions_submit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **exercise_id** | **str**| Identifier of the exercise | 
 **body** | [**ExerciseIdSubmitBody**](ExerciseIdSubmitBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reference_exercise_solutions_update**
> reference_exercise_solutions_update(solution_id, body=body)

Update details about the ref. solution (note, etc...)

Update details about the ref. solution (note, etc...)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
solution_id = 'solution_id_example' # str | Identifier of the solution
body = swagger_client.ReferencesolutionsSolutionIdBody() # ReferencesolutionsSolutionIdBody |  (optional)

try:
    # Update details about the ref. solution (note, etc...)
    api_instance.reference_exercise_solutions_update(solution_id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->reference_exercise_solutions_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **solution_id** | **str**| Identifier of the solution | 
 **body** | [**ReferencesolutionsSolutionIdBody**](ReferencesolutionsSolutionIdBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registration_accept_invitation**
> registration_accept_invitation(body=body)

Accept invitation and create corresponding user account.

Accept invitation and create corresponding user account.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.UsersAcceptinvitationBody() # UsersAcceptinvitationBody |  (optional)

try:
    # Accept invitation and create corresponding user account.
    api_instance.registration_accept_invitation(body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->registration_accept_invitation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UsersAcceptinvitationBody**](UsersAcceptinvitationBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registration_create_account**
> registration_create_account(body=body)

Create a user account

Create a user account

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.V1UsersBody() # V1UsersBody |  (optional)

try:
    # Create a user account
    api_instance.registration_create_account(body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->registration_create_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1UsersBody**](V1UsersBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registration_create_invitation**
> registration_create_invitation(body=body)

Create an invitation for a user and send it over via email

Create an invitation for a user and send it over via email

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.UsersInviteBody() # UsersInviteBody |  (optional)

try:
    # Create an invitation for a user and send it over via email
    api_instance.registration_create_invitation(body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->registration_create_invitation: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UsersInviteBody**](UsersInviteBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registration_debug**
> registration_debug(c, param, body=body, b=b)

Debug endpoint.

Debug endpoint.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
c = 1.2 # float | c
param = 'param_example' # str | param
body = swagger_client.DebugParamBody() # DebugParamBody |  (optional)
b = true # bool | b (optional)

try:
    # Debug endpoint.
    api_instance.registration_debug(c, param, body=body, b=b)
except ApiException as e:
    print("Exception when calling DefaultApi->registration_debug: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **c** | **float**| c | 
 **param** | **str**| param | 
 **body** | [**DebugParamBody**](DebugParamBody.md)|  | [optional] 
 **b** | **bool**| b | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **registration_validate_registration_data**
> registration_validate_registration_data(body=body)

Check if the registered E-mail isn't already used and if the password is strong enough

Check if the registered E-mail isn't already used and if the password is strong enough

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.UsersValidateregistrationdataBody() # UsersValidateregistrationdataBody |  (optional)

try:
    # Check if the registered E-mail isn't already used and if the password is strong enough
    api_instance.registration_validate_registration_data(body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->registration_validate_registration_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UsersValidateregistrationdataBody**](UsersValidateregistrationdataBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **runtime_environments_default**
> runtime_environments_default()

Get a list of all runtime environments

Get a list of all runtime environments

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    # Get a list of all runtime environments
    api_instance.runtime_environments_default()
except ApiException as e:
    print("Exception when calling DefaultApi->runtime_environments_default: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **security_check**
> security_check(body=body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.SecurityCheckBody() # SecurityCheckBody |  (optional)

try:
    api_instance.security_check(body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->security_check: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SecurityCheckBody**](SecurityCheckBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shadow_assignments_create**
> shadow_assignments_create(body=body)

Create new shadow assignment in given group.

Create new shadow assignment in given group.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.V1ShadowassignmentsBody() # V1ShadowassignmentsBody |  (optional)

try:
    # Create new shadow assignment in given group.
    api_instance.shadow_assignments_create(body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->shadow_assignments_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**V1ShadowassignmentsBody**](V1ShadowassignmentsBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shadow_assignments_create_points**
> shadow_assignments_create_points(id, body=body)

Create new points for shadow assignment and user.

Create new points for shadow assignment and user.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the shadow assignment
body = swagger_client.IdCreatepointsBody() # IdCreatepointsBody |  (optional)

try:
    # Create new points for shadow assignment and user.
    api_instance.shadow_assignments_create_points(id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->shadow_assignments_create_points: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the shadow assignment | 
 **body** | [**IdCreatepointsBody**](IdCreatepointsBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shadow_assignments_detail**
> shadow_assignments_detail(id)

Get details of a shadow assignment

Get details of a shadow assignment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the assignment

try:
    # Get details of a shadow assignment
    api_instance.shadow_assignments_detail(id)
except ApiException as e:
    print("Exception when calling DefaultApi->shadow_assignments_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the assignment | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shadow_assignments_remove**
> shadow_assignments_remove(id)

Delete shadow assignment

Delete shadow assignment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the assignment to be removed

try:
    # Delete shadow assignment
    api_instance.shadow_assignments_remove(id)
except ApiException as e:
    print("Exception when calling DefaultApi->shadow_assignments_remove: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the assignment to be removed | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shadow_assignments_remove_points**
> shadow_assignments_remove_points(points_id)

Remove points of shadow assignment.

Remove points of shadow assignment.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
points_id = 'points_id_example' # str | Identifier of the shadow assignment points

try:
    # Remove points of shadow assignment.
    api_instance.shadow_assignments_remove_points(points_id)
except ApiException as e:
    print("Exception when calling DefaultApi->shadow_assignments_remove_points: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **points_id** | **str**| Identifier of the shadow assignment points | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shadow_assignments_update_detail**
> shadow_assignments_update_detail(id, body=body)

Update details of an shadow assignment

Update details of an shadow assignment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the updated assignment
body = swagger_client.ShadowassignmentsIdBody() # ShadowassignmentsIdBody |  (optional)

try:
    # Update details of an shadow assignment
    api_instance.shadow_assignments_update_detail(id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->shadow_assignments_update_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the updated assignment | 
 **body** | [**ShadowassignmentsIdBody**](ShadowassignmentsIdBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shadow_assignments_update_points**
> shadow_assignments_update_points(points_id, body=body)

Update detail of shadow assignment points.

Update detail of shadow assignment points.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
points_id = 'points_id_example' # str | Identifier of the shadow assignment points
body = swagger_client.PointsPointsIdBody() # PointsPointsIdBody |  (optional)

try:
    # Update detail of shadow assignment points.
    api_instance.shadow_assignments_update_points(points_id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->shadow_assignments_update_points: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **points_id** | **str**| Identifier of the shadow assignment points | 
 **body** | [**PointsPointsIdBody**](PointsPointsIdBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shadow_assignments_validate**
> shadow_assignments_validate(id, body=body)

Check if the version of the shadow assignment is up-to-date.

Check if the version of the shadow assignment is up-to-date.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the shadow assignment
body = swagger_client.IdValidateBody3() # IdValidateBody3 |  (optional)

try:
    # Check if the version of the shadow assignment is up-to-date.
    api_instance.shadow_assignments_validate(id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->shadow_assignments_validate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the shadow assignment | 
 **body** | [**IdValidateBody3**](IdValidateBody3.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sis_bind_group**
> sis_bind_group(course_id, body=body)

Bind an existing local group to a SIS group

Bind an existing local group to a SIS group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
course_id = 'course_id_example' # str | 
body = swagger_client.CourseIdBindBody() # CourseIdBindBody |  (optional)

try:
    # Bind an existing local group to a SIS group
    api_instance.sis_bind_group(course_id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->sis_bind_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **body** | [**CourseIdBindBody**](CourseIdBindBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sis_create_group**
> sis_create_group(course_id, body=body)

Create a new group based on a SIS group

Create a new group based on a SIS group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
course_id = 'course_id_example' # str | 
body = swagger_client.CourseIdCreateBody() # CourseIdCreateBody |  (optional)

try:
    # Create a new group based on a SIS group
    api_instance.sis_create_group(course_id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->sis_create_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 
 **body** | [**CourseIdCreateBody**](CourseIdCreateBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sis_delete_term**
> sis_delete_term(id)

Delete a term

Delete a term

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | 

try:
    # Delete a term
    api_instance.sis_delete_term(id)
except ApiException as e:
    print("Exception when calling DefaultApi->sis_delete_term: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sis_edit_term**
> sis_edit_term(id, body=body)

Set details of a term

Set details of a term

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | 
body = swagger_client.TermsIdBody() # TermsIdBody |  (optional)

try:
    # Set details of a term
    api_instance.sis_edit_term(id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->sis_edit_term: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**TermsIdBody**](TermsIdBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sis_get_terms**
> sis_get_terms()

Get a list of all registered SIS terms

Get a list of all registered SIS terms

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    # Get a list of all registered SIS terms
    api_instance.sis_get_terms()
except ApiException as e:
    print("Exception when calling DefaultApi->sis_get_terms: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sis_possible_parents**
> sis_possible_parents(course_id)

Find groups that can be chosen as parents of a group created from given SIS group by current user

Find groups that can be chosen as parents of a group created from given SIS group by current user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
course_id = 'course_id_example' # str | 

try:
    # Find groups that can be chosen as parents of a group created from given SIS group by current user
    api_instance.sis_possible_parents(course_id)
except ApiException as e:
    print("Exception when calling DefaultApi->sis_possible_parents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sis_register_term**
> sis_register_term(body=body)

Register a new term

Register a new term

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.SisTermsBody() # SisTermsBody |  (optional)

try:
    # Register a new term
    api_instance.sis_register_term(body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->sis_register_term: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SisTermsBody**](SisTermsBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sis_status**
> sis_status()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    api_instance.sis_status()
except ApiException as e:
    print("Exception when calling DefaultApi->sis_status: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sis_subscribed_courses**
> sis_subscribed_courses(user_id, year, term)

Get all courses subscirbed by a student and corresponding ReCodEx groups. Organizational and archived groups are filtered out from the result. Each course holds bound group IDs and group objects are returned in a separate array. Whole ancestral closure of groups is returned, so the webapp may properly assemble hiarichial group names.

Get all courses subscirbed by a student and corresponding ReCodEx groups. Organizational and archived groups are filtered out from the result. Each course holds bound group IDs and group objects are returned in a separate array. Whole ancestral closure of groups is returned, so the webapp may properly assemble hiarichial group names.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
user_id = 'user_id_example' # str | 
year = 56 # int | 
term = 56 # int | 

try:
    # Get all courses subscirbed by a student and corresponding ReCodEx groups. Organizational and archived groups are filtered out from the result. Each course holds bound group IDs and group objects are returned in a separate array. Whole ancestral closure of groups is returned, so the webapp may properly assemble hiarichial group names.
    api_instance.sis_subscribed_courses(user_id, year, term)
except ApiException as e:
    print("Exception when calling DefaultApi->sis_subscribed_courses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **year** | **int**|  | 
 **term** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sis_supervised_courses**
> sis_supervised_courses(user_id, year, term)

Get supervised SIS courses and corresponding ReCodEx groups. Each course holds bound group IDs and group objects are returned in a separate array. Whole ancestral closure of groups is returned, so the webapp may properly assemble hiarichial group names.

Get supervised SIS courses and corresponding ReCodEx groups. Each course holds bound group IDs and group objects are returned in a separate array. Whole ancestral closure of groups is returned, so the webapp may properly assemble hiarichial group names.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
user_id = 'user_id_example' # str | 
year = 56 # int | 
term = 56 # int | 

try:
    # Get supervised SIS courses and corresponding ReCodEx groups. Each course holds bound group IDs and group objects are returned in a separate array. Whole ancestral closure of groups is returned, so the webapp may properly assemble hiarichial group names.
    api_instance.sis_supervised_courses(user_id, year, term)
except ApiException as e:
    print("Exception when calling DefaultApi->sis_supervised_courses: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 
 **year** | **int**|  | 
 **term** | **int**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sis_unbind_group**
> sis_unbind_group(course_id, group_id)

Delete a binding between a local group and a SIS group

Delete a binding between a local group and a SIS group

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
course_id = 'course_id_example' # str | an identifier of a SIS course
group_id = 'group_id_example' # str | an identifier of a local group

try:
    # Delete a binding between a local group and a SIS group
    api_instance.sis_unbind_group(course_id, group_id)
except ApiException as e:
    print("Exception when calling DefaultApi->sis_unbind_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **str**| an identifier of a SIS course | 
 **group_id** | **str**| an identifier of a local group | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submission_failures_default**
> submission_failures_default()

List all submission failures, ever

List all submission failures, ever

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    # List all submission failures, ever
    api_instance.submission_failures_default()
except ApiException as e:
    print("Exception when calling DefaultApi->submission_failures_default: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submission_failures_detail**
> submission_failures_detail(id)

Get details of a failure

Get details of a failure

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | An identifier of the failure

try:
    # Get details of a failure
    api_instance.submission_failures_detail(id)
except ApiException as e:
    print("Exception when calling DefaultApi->submission_failures_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An identifier of the failure | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submission_failures_resolve**
> submission_failures_resolve(id, body=body)

Mark a submission failure as resolved

Mark a submission failure as resolved

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | An identifier of the failure
body = swagger_client.IdResolveBody() # IdResolveBody |  (optional)

try:
    # Mark a submission failure as resolved
    api_instance.submission_failures_resolve(id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->submission_failures_resolve: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| An identifier of the failure | 
 **body** | [**IdResolveBody**](IdResolveBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submission_failures_unresolved**
> submission_failures_unresolved()

List all unresolved submission failures

List all unresolved submission failures

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    # List all unresolved submission failures
    api_instance.submission_failures_unresolved()
except ApiException as e:
    print("Exception when calling DefaultApi->submission_failures_unresolved: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_can_submit**
> submit_can_submit(id, user_id=user_id)

Check if the given user can submit solutions to the assignment

Check if the given user can submit solutions to the assignment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the assignment
user_id = 'user_id_example' # str | Identification of the user (optional)

try:
    # Check if the given user can submit solutions to the assignment
    api_instance.submit_can_submit(id, user_id=user_id)
except ApiException as e:
    print("Exception when calling DefaultApi->submit_can_submit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the assignment | 
 **user_id** | **str**| Identification of the user | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_pre_submit**
> submit_pre_submit(id, body=body, user_id=user_id)

Pre submit action which will, based on given files, detect possible runtime environments for the assignment. Also it can be further used for entry points and other important things that should be provided by user during submit.

Pre submit action which will, based on given files, detect possible runtime environments for the assignment. Also it can be further used for entry points and other important things that should be provided by user during submit.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | identifier of assignment
body = swagger_client.IdPresubmitBody() # IdPresubmitBody |  (optional)
user_id = 'user_id_example' # str | Identifier of the submission author (optional)

try:
    # Pre submit action which will, based on given files, detect possible runtime environments for the assignment. Also it can be further used for entry points and other important things that should be provided by user during submit.
    api_instance.submit_pre_submit(id, body=body, user_id=user_id)
except ApiException as e:
    print("Exception when calling DefaultApi->submit_pre_submit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of assignment | 
 **body** | [**IdPresubmitBody**](IdPresubmitBody.md)|  | [optional] 
 **user_id** | **str**| Identifier of the submission author | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_resubmit**
> submit_resubmit(id, body=body)

Resubmit a solution (i.e., create a new submission)

Resubmit a solution (i.e., create a new submission)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the solution
body = swagger_client.IdResubmitBody1() # IdResubmitBody1 |  (optional)

try:
    # Resubmit a solution (i.e., create a new submission)
    api_instance.submit_resubmit(id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->submit_resubmit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the solution | 
 **body** | [**IdResubmitBody1**](IdResubmitBody1.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_resubmit_all**
> submit_resubmit_all(id)

Start async job that resubmits all submissions of an assignment. No job is started when there are pending resubmit jobs for the selected assignment. Returns list of pending async jobs (same as GET call)

Start async job that resubmits all submissions of an assignment. No job is started when there are pending resubmit jobs for the selected assignment. Returns list of pending async jobs (same as GET call)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the assignment

try:
    # Start async job that resubmits all submissions of an assignment. No job is started when there are pending resubmit jobs for the selected assignment. Returns list of pending async jobs (same as GET call)
    api_instance.submit_resubmit_all(id)
except ApiException as e:
    print("Exception when calling DefaultApi->submit_resubmit_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the assignment | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_resubmit_all_async_job_status**
> submit_resubmit_all_async_job_status(id)

Return a list of all pending resubmit async jobs associated with given assignment. Under normal circumstances, the list shoul be either empty, or contian only one job.

Return a list of all pending resubmit async jobs associated with given assignment. Under normal circumstances, the list shoul be either empty, or contian only one job.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the assignment

try:
    # Return a list of all pending resubmit async jobs associated with given assignment. Under normal circumstances, the list shoul be either empty, or contian only one job.
    api_instance.submit_resubmit_all_async_job_status(id)
except ApiException as e:
    print("Exception when calling DefaultApi->submit_resubmit_all_async_job_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the assignment | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_submit**
> submit_submit(id, body=body)

Submit a solution of an assignment

Submit a solution of an assignment

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the assignment
body = swagger_client.IdSubmitBody() # IdSubmitBody |  (optional)

try:
    # Submit a solution of an assignment
    api_instance.submit_submit(id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->submit_submit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the assignment | 
 **body** | [**IdSubmitBody**](IdSubmitBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **uploaded_files_append_partial**
> uploaded_files_append_partial(id, offset)

Add another chunk to partial upload.

Add another chunk to partial upload.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the file
offset = 56 # int | Offset of the chunk for verification

try:
    # Add another chunk to partial upload.
    api_instance.uploaded_files_append_partial(id, offset)
except ApiException as e:
    print("Exception when calling DefaultApi->uploaded_files_append_partial: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the file | 
 **offset** | **int**| Offset of the chunk for verification | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **uploaded_files_cancel_partial**
> uploaded_files_cancel_partial(id)

Cancel partial upload and remove all uploaded chunks.

Cancel partial upload and remove all uploaded chunks.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | 

try:
    # Cancel partial upload and remove all uploaded chunks.
    api_instance.uploaded_files_cancel_partial(id)
except ApiException as e:
    print("Exception when calling DefaultApi->uploaded_files_cancel_partial: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **uploaded_files_complete_partial**
> uploaded_files_complete_partial(id)

Finalize partial upload and convert the partial file into UploadFile. All data chunks are extracted from the store, assembled into one file, and is moved back into the store.

Finalize partial upload and convert the partial file into UploadFile. All data chunks are extracted from the store, assembled into one file, and is moved back into the store.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | 

try:
    # Finalize partial upload and convert the partial file into UploadFile. All data chunks are extracted from the store, assembled into one file, and is moved back into the store.
    api_instance.uploaded_files_complete_partial(id)
except ApiException as e:
    print("Exception when calling DefaultApi->uploaded_files_complete_partial: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **uploaded_files_content**
> uploaded_files_content(id, entry=entry, similar_solution_id=similar_solution_id)

Get the contents of a file

Get the contents of a file

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the file
entry = 'entry_example' # str | Name of the entry in the ZIP archive (if the target file is ZIP) (optional)
similar_solution_id = 'similar_solution_id_example' # str | Id of an assignment solution which has detected possible plagiarism in this file. This is basically a shortcut (hint) for ACLs. (optional)

try:
    # Get the contents of a file
    api_instance.uploaded_files_content(id, entry=entry, similar_solution_id=similar_solution_id)
except ApiException as e:
    print("Exception when calling DefaultApi->uploaded_files_content: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the file | 
 **entry** | **str**| Name of the entry in the ZIP archive (if the target file is ZIP) | [optional] 
 **similar_solution_id** | **str**| Id of an assignment solution which has detected possible plagiarism in this file. This is basically a shortcut (hint) for ACLs. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **uploaded_files_detail**
> uploaded_files_detail(id)

Get details of a file

Get details of a file

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the uploaded file

try:
    # Get details of a file
    api_instance.uploaded_files_detail(id)
except ApiException as e:
    print("Exception when calling DefaultApi->uploaded_files_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the uploaded file | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **uploaded_files_digest**
> uploaded_files_digest(id)

Compute a digest using a hashing algorithm. This feature is intended for upload checksums only. In the future, we might want to add algorithm selection via query parameter (default is SHA1).

Compute a digest using a hashing algorithm. This feature is intended for upload checksums only. In the future, we might want to add algorithm selection via query parameter (default is SHA1).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the file

try:
    # Compute a digest using a hashing algorithm. This feature is intended for upload checksums only. In the future, we might want to add algorithm selection via query parameter (default is SHA1).
    api_instance.uploaded_files_digest(id)
except ApiException as e:
    print("Exception when calling DefaultApi->uploaded_files_digest: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the file | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **uploaded_files_download**
> uploaded_files_download(id, entry=entry, similar_solution_id=similar_solution_id)

Download a file

Download a file

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the file
entry = 'entry_example' # str | Name of the entry in the ZIP archive (if the target file is ZIP) (optional)
similar_solution_id = 'similar_solution_id_example' # str | Id of an assignment solution which has detected possible plagiarism in this file. This is basically a shortcut (hint) for ACLs. (optional)

try:
    # Download a file
    api_instance.uploaded_files_download(id, entry=entry, similar_solution_id=similar_solution_id)
except ApiException as e:
    print("Exception when calling DefaultApi->uploaded_files_download: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the file | 
 **entry** | **str**| Name of the entry in the ZIP archive (if the target file is ZIP) | [optional] 
 **similar_solution_id** | **str**| Id of an assignment solution which has detected possible plagiarism in this file. This is basically a shortcut (hint) for ACLs. | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **uploaded_files_download_supplementary_file**
> uploaded_files_download_supplementary_file(id)

Download supplementary file

Download supplementary file

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the file

try:
    # Download supplementary file
    api_instance.uploaded_files_download_supplementary_file(id)
except ApiException as e:
    print("Exception when calling DefaultApi->uploaded_files_download_supplementary_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the file | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **uploaded_files_start_partial**
> uploaded_files_start_partial(body=body)

Start new upload per-partes. This process expects the file is uploaded as a sequence of PUT requests, each one carrying a chunk of data. Once all the chunks are in place, the complete request assembles them together in one file and transforms UploadPartialFile into UploadFile entity.

Start new upload per-partes. This process expects the file is uploaded as a sequence of PUT requests, each one carrying a chunk of data. Once all the chunks are in place, the complete request assembles them together in one file and transforms UploadPartialFile into UploadFile entity.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.UploadedfilesPartialBody() # UploadedfilesPartialBody |  (optional)

try:
    # Start new upload per-partes. This process expects the file is uploaded as a sequence of PUT requests, each one carrying a chunk of data. Once all the chunks are in place, the complete request assembles them together in one file and transforms UploadPartialFile into UploadFile entity.
    api_instance.uploaded_files_start_partial(body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->uploaded_files_start_partial: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UploadedfilesPartialBody**](UploadedfilesPartialBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **uploaded_files_upload**
> uploaded_files_upload()

Upload a file

Upload a file

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    # Upload a file
    api_instance.uploaded_files_upload()
except ApiException as e:
    print("Exception when calling DefaultApi->uploaded_files_upload: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_calendars_create_calendar**
> user_calendars_create_calendar(id)

Create new iCal token for a particular user.

Create new iCal token for a particular user.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | of the user

try:
    # Create new iCal token for a particular user.
    api_instance.user_calendars_create_calendar(id)
except ApiException as e:
    print("Exception when calling DefaultApi->user_calendars_create_calendar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| of the user | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_calendars_default**
> user_calendars_default(id)

Get calendar values in iCal format that correspond to given token.

Get calendar values in iCal format that correspond to given token.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | the iCal token

try:
    # Get calendar values in iCal format that correspond to given token.
    api_instance.user_calendars_default(id)
except ApiException as e:
    print("Exception when calling DefaultApi->user_calendars_default: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| the iCal token | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_calendars_expire_calendar**
> user_calendars_expire_calendar(id)

Set given iCal token to expired state. Expired tokens cannot be used to retrieve calendars.

Set given iCal token to expired state. Expired tokens cannot be used to retrieve calendars.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | the iCal token

try:
    # Set given iCal token to expired state. Expired tokens cannot be used to retrieve calendars.
    api_instance.user_calendars_expire_calendar(id)
except ApiException as e:
    print("Exception when calling DefaultApi->user_calendars_expire_calendar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| the iCal token | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_calendars_user_calendars**
> user_calendars_user_calendars(id)

Get all iCal tokens of one user (including expired ones).

Get all iCal tokens of one user (including expired ones).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | of the user

try:
    # Get all iCal tokens of one user (including expired ones).
    api_instance.user_calendars_user_calendars(id)
except ApiException as e:
    print("Exception when calling DefaultApi->user_calendars_user_calendars: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| of the user | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_all_groups**
> users_all_groups(id)

Get a list of all groups for a user

Get a list of all groups for a user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the user

try:
    # Get a list of all groups for a user
    api_instance.users_all_groups(id)
except ApiException as e:
    print("Exception when calling DefaultApi->users_all_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the user | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_create_local_account**
> users_create_local_account(id)

If user is registered externally, add local account as another login method. Created password is empty and has to be changed in order to use it.

If user is registered externally, add local account as another login method. Created password is empty and has to be changed in order to use it.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | 

try:
    # If user is registered externally, add local account as another login method. Created password is empty and has to be changed in order to use it.
    api_instance.users_create_local_account(id)
except ApiException as e:
    print("Exception when calling DefaultApi->users_create_local_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_default**
> users_default(offset=offset, limit=limit, order_by=order_by, filters=filters, locale=locale)

Get a list of all users matching given filters in given pagination rage. The result conforms to pagination protocol.

Get a list of all users matching given filters in given pagination rage. The result conforms to pagination protocol.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
offset = 56 # int | Index of the first result. (optional)
limit = 56 # int | Maximal number of results returned. (optional)
order_by = 'order_by_example' # str | Name of the column (column concept). The '!' prefix indicate descending order. (optional)
filters = NULL # list[object] | Named filters that prune the result. (optional)
locale = 'locale_example' # str | Currently set locale (used to augment order by clause if necessary), (optional)

try:
    # Get a list of all users matching given filters in given pagination rage. The result conforms to pagination protocol.
    api_instance.users_default(offset=offset, limit=limit, order_by=order_by, filters=filters, locale=locale)
except ApiException as e:
    print("Exception when calling DefaultApi->users_default: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| Index of the first result. | [optional] 
 **limit** | **int**| Maximal number of results returned. | [optional] 
 **order_by** | **str**| Name of the column (column concept). The &#x27;!&#x27; prefix indicate descending order. | [optional] 
 **filters** | [**list[object]**](object.md)| Named filters that prune the result. | [optional] 
 **locale** | **str**| Currently set locale (used to augment order by clause if necessary), | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_delete**
> users_delete(id)

Delete a user account

Delete a user account

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the user

try:
    # Delete a user account
    api_instance.users_delete(id)
except ApiException as e:
    print("Exception when calling DefaultApi->users_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the user | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_detail**
> users_detail(id)

Get details of a user account

Get details of a user account

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the user

try:
    # Get details of a user account
    api_instance.users_detail(id)
except ApiException as e:
    print("Exception when calling DefaultApi->users_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the user | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_groups**
> users_groups(id)

Get a list of non-archived groups for a user

Get a list of non-archived groups for a user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the user

try:
    # Get a list of non-archived groups for a user
    api_instance.users_groups(id)
except ApiException as e:
    print("Exception when calling DefaultApi->users_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the user | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_instances**
> users_instances(id)

Get a list of instances where a user is registered

Get a list of instances where a user is registered

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the user

try:
    # Get a list of instances where a user is registered
    api_instance.users_instances(id)
except ApiException as e:
    print("Exception when calling DefaultApi->users_instances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the user | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_invalidate_tokens**
> users_invalidate_tokens(id)

Invalidate all existing tokens issued for given user

Invalidate all existing tokens issued for given user

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the user

try:
    # Invalidate all existing tokens issued for given user
    api_instance.users_invalidate_tokens(id)
except ApiException as e:
    print("Exception when calling DefaultApi->users_invalidate_tokens: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the user | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_list_by_ids**
> users_list_by_ids(body=body)

Get a list of users based on given ids.

Get a list of users based on given ids.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.UsersListBody() # UsersListBody |  (optional)

try:
    # Get a list of users based on given ids.
    api_instance.users_list_by_ids(body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->users_list_by_ids: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UsersListBody**](UsersListBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_remove_external_login**
> users_remove_external_login(id, service)

Remove external ID of given authentication service.

Remove external ID of given authentication service.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | identifier of the user
service = 'service_example' # str | identifier of the authentication service (login type)

try:
    # Remove external ID of given authentication service.
    api_instance.users_remove_external_login(id, service)
except ApiException as e:
    print("Exception when calling DefaultApi->users_remove_external_login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of the user | 
 **service** | **str**| identifier of the authentication service (login type) | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_set_role**
> users_set_role(id, body=body)

Set a given role to the given user.

Set a given role to the given user.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the user
body = swagger_client.IdRoleBody() # IdRoleBody |  (optional)

try:
    # Set a given role to the given user.
    api_instance.users_set_role(id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->users_set_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the user | 
 **body** | [**IdRoleBody**](IdRoleBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_update_external_login**
> users_update_external_login(id, service, body=body)

Add or update existing external ID of given authentication service.

Add or update existing external ID of given authentication service.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | identifier of the user
service = 'service_example' # str | identifier of the authentication service (login type)
body = swagger_client.ExternalloginServiceBody() # ExternalloginServiceBody |  (optional)

try:
    # Add or update existing external ID of given authentication service.
    api_instance.users_update_external_login(id, service, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->users_update_external_login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| identifier of the user | 
 **service** | **str**| identifier of the authentication service (login type) | 
 **body** | [**ExternalloginServiceBody**](ExternalloginServiceBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_update_profile**
> users_update_profile(id, body=body)

Update the profile associated with a user account

Update the profile associated with a user account

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the user
body = swagger_client.UsersIdBody() # UsersIdBody |  (optional)

try:
    # Update the profile associated with a user account
    api_instance.users_update_profile(id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->users_update_profile: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the user | 
 **body** | [**UsersIdBody**](UsersIdBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_update_settings**
> users_update_settings(id, body=body)

Update the profile settings

Update the profile settings

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the user
body = swagger_client.IdSettingsBody() # IdSettingsBody |  (optional)

try:
    # Update the profile settings
    api_instance.users_update_settings(id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->users_update_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the user | 
 **body** | [**IdSettingsBody**](IdSettingsBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **users_update_ui_data**
> users_update_ui_data(id, body=body)

Update the user-specific structured UI data

Update the user-specific structured UI data

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
id = 'id_example' # str | Identifier of the user
body = swagger_client.IdUidataBody() # IdUidataBody |  (optional)

try:
    # Update the user-specific structured UI data
    api_instance.users_update_ui_data(id, body=body)
except ApiException as e:
    print("Exception when calling DefaultApi->users_update_ui_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Identifier of the user | 
 **body** | [**IdUidataBody**](IdUidataBody.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **worker_files_download_supplementary_file**
> worker_files_download_supplementary_file(hash)

Sends over an exercise supplementary file (a data file required by the tests).

Sends over an exercise supplementary file (a data file required by the tests).

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
hash = 'hash_example' # str | identification of the supplementary file

try:
    # Sends over an exercise supplementary file (a data file required by the tests).
    api_instance.worker_files_download_supplementary_file(hash)
except ApiException as e:
    print("Exception when calling DefaultApi->worker_files_download_supplementary_file: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hash** | **str**| identification of the supplementary file | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

