<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 1 - Tracker App</td></tr>
<tr><td> <em>Student: </em> Suchith Sameeri Balne (sb2648)</td></tr>
<tr><td> <em>Generated: </em> 10/9/2023 4:12:52 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-mini-project-1-tracker-app/grade/sb2648" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout dev branch and pull any pending changes&nbsp;</li><ol><li>&nbsp;git checkout dev</li><li>&nbsp;git pull origin dev</li></ol><li>Create a new branch for this assignment (see Desired Branch Name)</li><ol><li>git checkout -b MP1-Tracker</li></ol><li>Create a new folder called MP1 in your local repository</li><li>Create a new file called tracker.py</li><li>Copy/paste the content from this template:&nbsp;&nbsp;<a href="https://gist.github.com/MattToegel/380e6baa24f6c25b74bf2ce99ccba6da">https://gist.github.com/MattToegel/380e6baa24f6c25b74bf2ce99ccba6da</a></li><li>Add/commit/push the template file</li><ol><li>git add --all</li><li>git commit -m "adding template"</li><li>git push origin MP1-Tracker</li></ol><li>Create a pull request from MP1-Tracker to dev (keep it open, do not close it until you're done)</li><li>Solve the various todo items (also noted below in the deliverables) and fill in the evidence</li><ol><li>Periodically add/commit; recommended after each solved item or every few items</li></ol><li>Save and copy/download the markdown</li><li>Create a new file mp1-submission.md in the MP1 folder</li><li>Add the markdown content</li><li>add/commit/push all the pending files for this assignment (tracker.py and mp1-submission.md)</li><li>If everything looks good on the pull request complete the merge</li><li>Create a new pull request from dev to prod and merge it to update prod (not used yet but you want to keep this up to date)</li><li>checkout dev locally and pull the changes to be up to date</li><li>Navigate to the prod branch on github and find the mp1-submission.md file and get the link to the file to submit to canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Add Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited add_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-10-09T15.57.19image.png.webp?alt=media&token=2c277e88-402b-4786-a795-cc8b9a09840f"/></td></tr>
<tr><td> <em>Caption:</em> <p>In the above screenshot code for add_task() method is shown which covers all<br>the mandatory checklist <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of add_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-10-09T15.45.39image.png.webp?alt=media&token=73f3c4c8-ec58-46fe-8674-234755f7c9dd"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows that task is added successfully<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-10-09T15.48.10image.png.webp?alt=media&token=d86455d4-c9c1-4a2c-bd29-bc6cc758f089"/></td></tr>
<tr><td> <em>Caption:</em> <p>Failed to add task is shown due to missing values in the input<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-10-09T15.58.30image.png.webp?alt=media&token=c17ef8a4-80b6-4aa2-a788-8333cc8728ad"/></td></tr>
<tr><td> <em>Caption:</em> <p>Failed to add task due to invalid date format<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for add_task()</td></tr>
<tr><td> <em>Response:</em> <div style="color: #cccccc;background-color: #1f1f1f;font-family: 'Droid Sans Mono', 'monospace', monospace;font-weight: normal;font-size: 14px;line-height: 19px;white-space: pre;"><div>#1<br>update lastActivity with the current datetime value</div><div><span style="color: #9cdcfe;">task</span><span style="color: #cccccc;">[</span><span style="color: #ce9178;">"lastActivity"</span><span<br>style="color: #cccccc;">] </span><span style="color: #d4d4d4;">=</span><span style="color: #cccccc;"> </span><span style="color: #4ec9b0;">datetime</span><span style="color: #cccccc;">.</span><span style="color:<br>#dcdcaa;">now</span><span style="color: #cccccc;">().</span><span style="color: #dcdcaa;">strftime</span><span style="color: #cccccc;">(</span><span style="color: #ce9178;">'%m/</span><span style="color: #569cd6;">%d</span><span style="color: #ce9178;">/%y<br>%H:%M:%S'</span><span style="color: #cccccc;">)     </span><span style="color: #6a9955;"># Last activity update<br>with current time.</span></div><div><span style="color: #6a9955;"></span>#2 set the name, description, and due date (all<br>must be provided)</div><div><span style="color: #9cdcfe;">task</span><span style="color: #cccccc;">[</span><span style="color: #ce9178;">"name"</span><span style="color: #cccccc;">] </span><span style="color:<br>#d4d4d4;">=</span><span style="color: #cccccc;"> </span><span style="color: #9cdcfe;">name</span><span style="color: #cccccc;">     </span><span<br>style="color: #6a9955;"># Sets the Name attribute.</span></div><div><span style="color: #9cdcfe;">task</span><span style="color: #cccccc;">[</span><span style="color: #ce9178;">"description"</span><span style="color:<br>#cccccc;">] </span><span style="color: #d4d4d4;">=</span><span style="color: #cccccc;"> </span><span style="color: #9cdcfe;">description</span><span style="color: #cccccc;">  <br></span><span style="color: #6a9955;"># Sets the Description attribute.</span></div><div>#3 due date must match one of<br>the formats mentioned in str_to_datetime()</div><div><span style="color: #9cdcfe;">task</span><span style="color: #cccccc;">[</span><span style="color: #ce9178;">"due"</span><span style="color: #cccccc;">]<br></span><span style="color: #d4d4d4;">=</span><span style="color: #cccccc;"> </span><span style="color: #dcdcaa;">str_to_datetime</span><span style="color: #cccccc;">(</span><span style="color: #9cdcfe;">due</span><span style="color:<br>#cccccc;">).</span><span style="color: #dcdcaa;">strftime</span><span style="color: #cccccc;">(</span><span style="color: #ce9178;">'%m/</span><span style="color: #569cd6;">%d</span><span style="color: #ce9178;">/%y %H:%M:%S'</span><span style="color:<br>#cccccc;">)    </span><span style="color: #6a9955;"># Sets the Due date attribute in<br>date format.</span></div><div>#4 add the new task to the tasks list</div><div><span style="color: #9cdcfe;">tasks</span><span style="color:<br>#cccccc;">.</span><span style="color: #dcdcaa;">append</span><span style="color: #cccccc;">(</span><span style="color: #9cdcfe;">task</span><span style="color: #cccccc;">)    <br>   </span><span style="color: #6a9955;"># Task will be added to task list<br>if inputs are valid.</span></div><div>#5 output a message confirming the new task was added<br>or if the addition was rejected due to missing data</div><div><span style="color: #dcdcaa;">print</span><span style="color:<br>#cccccc;">(</span><span style="color: #ce9178;">"</span><span style="color: #d7ba7d;">\n</span><span style="color: #ce9178;">*** Task has been added successfully! ***</span><span<br>style="color: #d7ba7d;">\n</span><span style="color: #ce9178;">"</span><span style="color: #cccccc;">)</span></div><div><span style="color: #cccccc;">    </span></div><div><ul><li><span style="color:<br>#ce9178;">Here, New task will be added to the task list. </span></li></ul></div><div><ul><li><span style="color: #ce9178;">For<br>this we have set name, description and due date attributes to the task<br>instance and added this dictionary to the tasks list and finally save method<br>is called.</span></li></ul></div><div><ul><li><span style="color: #ce9178;">Task will not be added if any of the invalid<br>inputs are provided to this method. </span></li></ul></div><div><span style="color: #ce9178;"><br></span></div></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Process Update Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited process_update() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-10-09T17.32.21image.png.webp?alt=media&token=fbd960f7-8583-464a-9efe-544b2899501d"/></td></tr>
<tr><td> <em>Caption:</em> <p>Above screenshot shows the code for process_update based on the provided index<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-10-09T16.41.22image.png.webp?alt=media&token=018eb438-10fb-4e2a-bd44-54dbcc4bd951"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing existing values and Handled out of bound exception<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Briefly explain the solutions to the checklist items for process_update()</td></tr>
<tr><td> <em>Response:</em> <div style="color: #cccccc;background-color: #1f1f1f;font-family: 'Droid Sans Mono', 'monospace', monospace;font-weight: normal;font-size: 14px;line-height: 19px;white-space: pre;"><div><ul><li><span<br>style="color: #ce9178;">Here, in this method if the given index is greater than or<br>equals to zero and less than length of the tasks list then we<br>retrieve the current task details and the information is shown to the user.</span></li></ul></div><div><ul><li><span<br>style="color: #ce9178;">User is prompted to enter name, description and Due date details for<br>the task update. Provided information is given to update_task function to update the<br>task in task list.</span></li></ul></div><div><ul><li><span style="color: #ce9178;">In case, the index is invalid then a<br>message is shown to user to select valid index to perform task update.</span></li></ul></div></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Update Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited update_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-10-09T17.12.54image.png.webp?alt=media&token=fa4967cb-519d-4065-85e0-7c209bc316a2"/></td></tr>
<tr><td> <em>Caption:</em> <p>Above screenshot shows the update logic code which satisfies all the checklist<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of update_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-10-09T17.18.09image.png.webp?alt=media&token=531319ca-d08d-4c26-9b17-7835bcb66c99"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows a message as updated if any of the attribute is updated<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-10-09T17.18.50image.png.webp?alt=media&token=a0aee459-759c-46be-827d-69432b55366f"/></td></tr>
<tr><td> <em>Caption:</em> <p>Above screenshot shows a message as no updates provided if no updates are<br>given by the user<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-10-09T17.33.27image.png.webp?alt=media&token=b943b84c-e908-4bbd-a25c-9bd9fdcca805"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot shows unable to update if no task is found at the provided<br>index<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for update_task()</td></tr>
<tr><td> <em>Response:</em> <div style="color: #cccccc;background-color: #1f1f1f;font-family: 'Droid Sans Mono', 'monospace', monospace;font-weight: normal;font-size: 14px;line-height: 19px;white-space: pre;"><div><ul><li><span<br>style="color: #ce9178;">Retrieved the task for the provided index and the update of new<br>attributes are performed if new values are provided.</span></li></ul></div><div><ul><li><span style="color: #ce9178;">If no updates are<br>provided then last activity is updated with current date and time.</span></li></ul></div><div><ul><li><span style="color: #ce9178;">Prints<br>a valid message for an exception if any invalid information is provided for<br>the update task.</span></li></ul></div></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Mark Task Done/Complete Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited mark_done() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-10-09T17.53.01image.png.webp?alt=media&token=d288519c-a8af-4298-8045-a9510697c461"/></td></tr>
<tr><td> <em>Caption:</em> <p>Above screenshot shows the code for mark_done() with all the checklist covered.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of mark_done()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-10-09T17.56.53Screenshot%20from%202023-10-09%2013-54-58.png.webp?alt=media&token=7b1b0b51-7278-4901-be89-4ba8592c68b5"/></td></tr>
<tr><td> <em>Caption:</em> <p>In the above screenshot, I&#39;m showing output for the incomplete task marked as<br>done with current date and time and also the output if task already<br>marked as done<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-10-09T17.59.29image.png.webp?alt=media&token=ed02e34f-5d3c-45ae-adc4-2b9911992f68"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing invalid index case where a message is shown to the user to<br>select valid input.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for mark_done()</td></tr>
<tr><td> <em>Response:</em> <div style="color: #cccccc;background-color: #1f1f1f;font-family: 'Droid Sans Mono', 'monospace', monospace;font-weight: normal;font-size: 14px;line-height: 19px;white-space: pre;"><div><ul><li><span<br>style="color: #ce9178;">In this function, task at given index is retrieved and if the<br>task is already completed then we print a message to the user saying<br>that task is already completed.</span></li></ul></div><div><ul><li><span style="color: #ce9178;">If the task is not completed then<br>we mark the task as done by updating done attribute with current date<br>and time. </span></li></ul></div><div><ul><li><span style="color: #ce9178;">Index out of bounds is handled and a message<br>is shown to user to select a valid task.</span></li></ul></div></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> View Task Logic (and list) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited view_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-10-09T18.12.23image.png.webp?alt=media&token=ca9b49e9-5bd8-4475-abf4-092f936f58b8"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot for view_task() which satisfies all the checklist activities<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of view_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-10-09T18.09.49image.png.webp?alt=media&token=aea3f9ba-96d1-40bf-b368-1b786df1c647"/></td></tr>
<tr><td> <em>Caption:</em> <p>View task showing the task details for the provided index which is a<br>success scenario<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-10-09T18.11.13image.png.webp?alt=media&token=e8ea4662-fcb2-45d3-adc7-e64de673110c"/></td></tr>
<tr><td> <em>Caption:</em> <p>View task for an invalid index<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshot(s) of list_tasks() output showing a few examples</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-10-09T18.17.31image.png.webp?alt=media&token=49db28c1-a667-44b3-bb19-5423e0693875"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the list of tasks with complete and incomplete tasks<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Delete Task Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited delete_task() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-10-09T18.24.26image.png.webp?alt=media&token=fbc93a1c-7362-498d-803d-17097c2f18e8"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing delete_task() with all the related checklist items covered in the code.<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of delete_task()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-10-09T18.22.49image.png.webp?alt=media&token=14c1823c-c804-4711-af2c-46030d91abee"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing success case for task deletion from the list for the given index<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-10-09T18.25.38image.png.webp?alt=media&token=94e8f3f5-632d-4177-a0d4-6a164d609f2a"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing negative case where task cannot be deleted as there is no task<br>available at provided index<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for delete_task()</td></tr>
<tr><td> <em>Response:</em> <div style="color: #cccccc;background-color: #1f1f1f;font-family: 'Droid Sans Mono', 'monospace', monospace;font-weight: normal;font-size: 14px;line-height: 19px;white-space: pre;"><div><ul><li><span<br>style="color: #ce9178;">Task for the given index is deleted from the list.</span></li><li><div style="color: #cccccc;background-color:<br>#1f1f1f;font-family: 'Droid Sans Mono', 'monospace', monospace;font-weight: normal;font-size: 14px;line-height: 19px;white-space: pre;"><div><span style="color: #cccccc;"> </span><span<br>style="color: #c586c0;">del</span><span style="color: #cccccc;"> </span><span style="color: #9cdcfe;">tasks</span><span style="color: #cccccc;">[</span><span style="color: #9cdcfe;">index</span><span style="color: #cccccc;">]<br>   </span><span style="color: #6a9955;"># Deletes selected task form the task list.</span></div></div></li></ul></div><div><ul><li><span<br>style="color: #ce9178;">Index out of bound exception is handled and a message is shown<br>to select a valid input to delete the task from the list.</span></li></ul></div></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Get Incomplete Tasks Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_incomplete_tasks() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-10-09T18.34.45image.png.webp?alt=media&token=7d697e4f-9528-41dc-b037-7a56fbfd6e13"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the code for incomplete tasks which are not marked as done<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_incomplete_tasks()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-10-09T18.31.44image.png.webp?alt=media&token=eca9a597-c07d-4531-88ec-172eda49b246"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing incomplete tasks from the list<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-10-09T18.38.36image.png.webp?alt=media&token=11a087d0-990d-4a0b-a217-9ec760cbd19d"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing negative scenario where there are no incomplete tasks<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_incomplete_tasks()</td></tr>
<tr><td> <em>Response:</em> <div style="color: #cccccc;background-color: #1f1f1f;font-family: 'Droid Sans Mono', 'monospace', monospace;font-weight: normal;font-size: 14px;line-height: 19px;white-space: pre;"><div><ul><li><span<br>style="color: #c586c0;">if</span><span style="color: #cccccc;"> </span><span style="color: #569cd6;">not</span><span style="color: #cccccc;"> </span><span style="color: #9cdcfe;">each_task</span><span style="color:<br>#cccccc;">[</span><span style="color: #ce9178;">"done"</span><span style="color: #cccccc;">]: # Checks for tasks which are marked as<br>false for done attribute.</span></li><li><div style="color: #cccccc;background-color: #1f1f1f;font-family: 'Droid Sans Mono', 'monospace', monospace;font-weight: normal;font-size:<br>14px;line-height: 19px;white-space: pre;"><div><span style="color: #9cdcfe;">_tasks</span><span style="color: #cccccc;">.</span><span style="color: #dcdcaa;">append</span><span style="color: #cccccc;">(</span><span style="color: #9cdcfe;">each_task</span><span<br>style="color: #cccccc;">) # Appends the incomplete tasks to the _task list</span></div></div></li><li><div style="color: #cccccc;background-color:<br>#1f1f1f;font-family: 'Droid Sans Mono', 'monospace', monospace;font-weight: normal;font-size: 14px;line-height: 19px;white-space: pre;"><div><span style="color: #dcdcaa;">list_tasks</span><span style="color:<br>#cccccc;">(</span><span style="color: #9cdcfe;">_tasks</span><span style="color: #cccccc;">) # Adds the _tasks to list_task()</span></div></div></li><li><div style="color: #cccccc;background-color:<br>#1f1f1f;font-family: 'Droid Sans Mono', 'monospace', monospace;font-weight: normal;font-size: 14px;line-height: 19px;white-space: pre;"><div><span style="color: #ce9178;">We get<br>the tasks which are not marked as done i.e, marked as False and<br>those tasks are added to _tasks list and this list is given to<br>list_task()function.</span></div></div></li></ul></div><div><span style="color: #cccccc;"><br></span></div></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Get Over Due Tasks Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_overdue_tasks() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-10-09T19.34.00image.png.webp?alt=media&token=bfcf65eb-5162-42af-825d-82e293f8a6df"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the code for get_overdue_tasks() where tasks are retrieved if the due date<br>is completed but the task is not completed<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_overdue_tasks()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-10-09T19.37.38image.png.webp?alt=media&token=db39812b-6559-4499-a806-4a23c6b5644a"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing the output for the overdue tasks<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-10-09T19.39.18image.png.webp?alt=media&token=df835316-58c0-444a-876c-834ab3a98320"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing output for the negative scenario where no tasks are overdue<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_overdue_tasks()</td></tr>
<tr><td> <em>Response:</em> <div style="color: #cccccc;background-color: #1f1f1f;font-family: 'Droid Sans Mono', 'monospace', monospace;font-weight: normal;font-size: 14px;line-height: 19px;white-space: pre;"><div><ul><li><span<br>style="color: #ce9178;">Here, we are iterating over the list of tasks and we consider<br>the tasks which are not marked as done and which are older than<br>the current date and time. </span></li></ul></div><div><ul><li><div style="color: #cccccc;background-color: #1f1f1f;font-family: 'Droid Sans Mono', 'monospace',<br>monospace;font-weight: normal;font-size: 14px;line-height: 19px;white-space: pre;"><div><span style="color: #c586c0;">if</span><span style="color: #cccccc;"> (</span><span style="color: #9cdcfe;">current_datetime</span><span style="color:<br>#cccccc;"> </span><span style="color: #dcdcaa;">-</span><span style="color: #cccccc;"> </span><span style="color: #dcdcaa;">str_to_datetime</span><span style="color: #cccccc;">(</span><span style="color: #9cdcfe;">each_task</span><span<br>style="color: #cccccc;">[</span><span style="color: #ce9178;">"due"</span><span style="color: #cccccc;">]) </span><span style="color: #dcdcaa;">&gt;</span><span style="color: #cccccc;"> </span><span style="color:<br>#4ec9b0;">timedelta</span><span style="color: #cccccc;">(</span><span style="color: #b5cea8;">0</span><span style="color: #cccccc;">)) </span><span style="color: #569cd6;">and</span><span style="color: #cccccc;"> (</span><span<br>style="color: #9cdcfe;">each_task</span><span style="color: #cccccc;">[</span><span style="color: #ce9178;">"done"</span><span style="color: #cccccc;">] </span><span style="color: #d4d4d4;">==</span><span style="color: #cccccc;"><br></span><span style="color: #569cd6;">False</span><span style="color: #cccccc;">): # logic for above line</span></div></div><span style="color: #ce9178;"></span></li><li><span style="color:<br>#ce9178;">For this we take the difference of current time and due date for<br>the task.</span></li></ul></div><div><ul><li><span style="color: #ce9178;">These tasks are added to a list and are passed<br>to the list_tasks().</span></li></ul></div></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Get Time Remaining Logic </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of the edited get_time_remaining() function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-10-09T19.44.26image.png.webp?alt=media&token=341e0a0b-6415-4304-80a4-09bfd5312525"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing code for get_time_remaining() which covers all the checklist items for this task<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) showing the success/failure of get_time_remaining()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-10-09T19.48.53image.png.webp?alt=media&token=29e3925c-a01f-4d38-a3b1-a5a51ba4d870"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing time remaining to complete the task which is not overdue and it<br>is a positive scenario<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-10-09T19.50.52image.png.webp?alt=media&token=5bfe20dd-d030-4153-b7f0-efc4d5277e6a"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing negative scenario for time remaining to finish the task<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain the solutions to the checklist items for get_time_remaining()</td></tr>
<tr><td> <em>Response:</em> <div style="color: #cccccc;background-color: #1f1f1f;font-family: 'Droid Sans Mono', 'monospace', monospace;font-weight: normal;font-size: 14px;line-height: 19px;white-space: pre;"><div><ul><li><span<br>style="color: #ce9178;">Here, in this function we get the task by index and we<br>calculate the time and date difference between current date and time to due<br>date mentioned of the task. </span></li><li><span style="color: #ce9178;">If it is overdue, we print<br>a message saying that the task is overdue by X days, X hours,<br>X minutes, X seconds overdue.</span></li><li><span style="color: #ce9178;"></span><span style="color: #ce9178;">Incase, it is not overdue<br>but it is still pending then we print a message saying X days,<br>X hours, X minutes, X seconds left remaining.</span></li></ul></div></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot(s) of program output generated from filling in this deliverable (or close to it)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-10-09T19.31.40image.png.webp?alt=media&token=e8c0fd44-58ff-48fc-8700-44500272e775"/></td></tr>
<tr><td> <em>Caption:</em> <p>Terminal output for few tasks<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-10-09T20.02.37image.png.webp?alt=media&token=64567412-ebdd-4802-a1f7-92d0db4056d9"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing terminal outputs<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot(s) of the saved JSON file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-10-09T19.55.05image.png.webp?alt=media&token=a5bc3934-7483-4b39-bd81-8eb5d1fe1c3b"/></td></tr>
<tr><td> <em>Caption:</em> <p>Showing my tracker.json file<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Discuss any issues and how they were overcome or learnings from this project</td></tr>
<tr><td> <em>Response:</em> <p>&nbsp;Initially, I haven&#39;t handled index out of bound exception in process_update() method but<br>later during testing I figured out the problem and updated the code accordingly.<br><br></p><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add pull request for this assignment (project branch to dev)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Suchith-Balne/sb2648-is601-007/pull/6">https://github.com/Suchith-Balne/sb2648-is601-007/pull/6</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-mini-project-1-tracker-app/grade/sb2648" target="_blank">Grading</a></td></tr></table>