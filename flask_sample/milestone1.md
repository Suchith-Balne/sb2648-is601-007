<table><tr><td> <em>Assignment: </em> IS601 Milestone1 Deliverable</td></tr>
<tr><td> <em>Student: </em> Suchith Sameeri Balne (sb2648)</td></tr>
<tr><td> <em>Generated: </em> 11/13/2023 8:37:11 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-milestone1-deliverable/grade/sb2648" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone1 branch</li><li>Create a milestone1.md file in your Project folder</li><li>Git add/commit/push this empty file to Milestone1 (you'll need the link later)</li><li>Ensure your images display correctly in the sample markdown at the bottom</li><ol><li>NOTE: You may want to try to capture as much checklist evidence in your screenshots as possible, you do not need individual screenshots and are recommended to combine things when possible. Also, some screenshots may be reused if applicable.</li></ol><li>Save the submission items</li><li>Copy/paste the markdown from the "Copy markdown to clipboard link" or via the download button</li><li>Paste the code into the milestone1.md file or overwrite the file</li><li>Git add/commit/push the md file to Milestone1</li><li>Double check the images load when viewing the markdown file (points will be lost for invalid/non-loading images)</li><li>Make a pull request from Milestone1 to dev and merge it (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku dev</li></ol></li><li>Make a pull request from dev to prod (resolve any conflicts)<ol><li>Make sure everything looks ok on heroku prod</li></ol></li><li>Submit the direct link from github prod branch to the milestone1.md file (no other links will be accepted and will result in 0)</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Feature: User will be able to register a new account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-13T18.34.14image.png.webp?alt=media&token=d5b071d9-a859-4b8c-82da-dea075d9d03e"/></td></tr>
<tr><td> <em>Caption:</em> <p>User Registration <br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-13T18.40.58image.png.webp?alt=media&token=0ebb069b-822b-4da4-9bac-64e22c9af4fa"/></td></tr>
<tr><td> <em>Caption:</em> <p>Invalid email <br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-13T18.41.47image.png.webp?alt=media&token=248d8e7d-118a-42d9-b26e-2be1db51570f"/></td></tr>
<tr><td> <em>Caption:</em> <p>Password not matched<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-13T18.43.19image.png.webp?alt=media&token=590047b0-07d2-4edf-afa7-b17e4f571c5d"/></td></tr>
<tr><td> <em>Caption:</em> <p>Invalid password validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-13T18.44.21image.png.webp?alt=media&token=627d6f53-b2e9-4ec7-8c9a-dac692a251d5"/></td></tr>
<tr><td> <em>Caption:</em> <p>username already taken validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-13T18.46.00image.png.webp?alt=media&token=7c697f44-2151-4e80-81f8-e02d35b8e5ac"/></td></tr>
<tr><td> <em>Caption:</em> <p>Email not available validation<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of the Users table with data in it</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-13T18.49.36image.png.webp?alt=media&token=3ac4e1f4-ba6a-40a2-98e8-2a68aa45d2df"/></td></tr>
<tr><td> <em>Caption:</em> <p>Validation testing is performed on user3<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Suchith-Balne/sb2648-is601-007/pull/22">https://github.com/Suchith-Balne/sb2648-is601-007/pull/22</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <ul><li>The RegisterForm is a subclass of AuthForm, which handles common form fields and<br>validations.</li></ul><ul><li>The form is validated on submission (form.validate_on_submit()).</li></ul><ul><li>If the form is valid, it extracts<br>data (email, password, username) and hashes the password using bcrypt.</li></ul><ul><li>It then inserts the<br>user data into the database (IS601_Users table).</li></ul><ul><li>Flash messages are used to provide feedback<br>to the user.</li></ul><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Feature: User will be able to login to their account </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add one or more screenshots of the application showing the form and validation errors per the feature requirements</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-13T19.32.48image.png.webp?alt=media&token=3105a238-85a8-4fab-8dd8-64d718b879c0"/></td></tr>
<tr><td> <em>Caption:</em> <p>Password mismatch<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-13T19.33.31image.png.webp?alt=media&token=e278db26-e423-4cc0-861b-d04ede3a2a20"/></td></tr>
<tr><td> <em>Caption:</em> <p>Invalid User<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot of successful login</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-13T19.31.42image.png.webp?alt=media&token=d00a3a7d-8f23-4c8d-aa47-1a0d287ed0cb"/></td></tr>
<tr><td> <em>Caption:</em> <p>User logged in successfully<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Suchith-Balne/sb2648-is601-007/pull/22">https://github.com/Suchith-Balne/sb2648-is601-007/pull/22</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <ul><li>The LoginForm is a subclass of AuthForm.</li></ul><ul><li>The form is validated on submission.</li></ul><ul><li>If the<br>form is valid, it checks the database for the user based on the<br>provided email or username.</li></ul><ul><li>If the user is found, it checks the hashed password<br>using bcrypt.</li></ul><ul><li>If the password is valid, the user is logged in using login_user.</li></ul><ul><li>User<br>roles are loaded from the database.</li></ul><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Feat: Users will be able to logout </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the successful logout message</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-13T19.34.28image.png.webp?alt=media&token=182e44ad-948a-4f83-b0bc-f5bc2af5ea5c"/></td></tr>
<tr><td> <em>Caption:</em> <p>User Logged out<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing the logged out user can't access a login-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-13T19.35.13image.png.webp?alt=media&token=a435627a-03c1-46ce-a5d2-df766e91c76e"/></td></tr>
<tr><td> <em>Caption:</em> <p>Unauthorized error<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Suchith-Balne/sb2648-is601-007/pull/22">https://github.com/Suchith-Balne/sb2648-is601-007/pull/22</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works</td></tr>
<tr><td> <em>Response:</em> <p>Login<br><ul><li>The LoginForm is a subclass of AuthForm.</li></ul><ul><li>The form is validated on submission.</li></ul><ul><li>If the<br>form is valid, it checks the database for the user based on the<br>provided email or username.</li></ul><ul><li>If the user is found, it checks the hashed password<br>using bcrypt.</li></ul><ul><li>If the password is valid, the user is logged in using login_user.</li></ul><ul><li>User<br>roles are loaded from the database.</li></ul>Logout<br><ul><li>The logout route logs the user out using<br>logout_user.</li></ul><ul><li>Session keys related to Flask-Principal are removed.</li></ul><ul><li>Flask-Principal is informed that the user is<br>anonymous.</li></ul><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Feature: Basic Security Rules Implemented / Basic Roles Implemented </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add a screenshot showing the logged out user can't access a login-protected page (may be the same as similar request)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-13T19.37.17image.png.webp?alt=media&token=02c3f9e9-333d-42cf-a40a-f496fc632e06"/></td></tr>
<tr><td> <em>Caption:</em> <p>Logged out user not able to access protected pages<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a screenshot showing a user without an appropriate role can't access the role-protected page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-13T19.38.26image.png.webp?alt=media&token=bad21e01-73e8-4319-b8dc-e9637c6d1343"/></td></tr>
<tr><td> <em>Caption:</em> <p>Permission Denied as user doesn&#39;t have desired role<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the Roles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-14T00.24.41image.png.webp?alt=media&token=cbec27cb-ca78-409d-8eb0-c99fb48a25aa"/></td></tr>
<tr><td> <em>Caption:</em> <p>Roles table with Admin record<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a screenshot of the UserRoles table with valid data</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-13T19.44.54image.png.webp?alt=media&token=228d41b9-7360-410a-97e5-73e1b429bb6b"/></td></tr>
<tr><td> <em>Caption:</em> <p>User 1 has admin role<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add the related pull request(s) for these features</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Suchith-Balne/sb2648-is601-007/pull/22">https://github.com/Suchith-Balne/sb2648-is601-007/pull/22</a> </td></tr>
<tr><td> <em>Sub-Task 6: </em> Explain briefly how the process/code works for login-protected pages</td></tr>
<tr><td> <em>Response:</em> <ul><li>check_duplicate helper function is called when there is an exception related to database<br>operations. It checks whether the exception is related to a duplicate entry in<br>the IS601_Users table and displays an appropriate flash message. This function indirectly contributes<br>to the feedback provided to the user.</li></ul><ul><li>JsonSerializable provides a toJson method that converts<br>an object's attributes to a dictionary. It is used in the User class<br>to convert a user object to JSON before storing it in the session.<br>This simplifies the serialization process.</li></ul><ul><li>The session object is a critical component for maintaining<br>user state across different requests in a Flask application. It is used here<br>to store user information such as username, email, and roles, making it accessible<br>during the user's session. The session is updated as needed, ensuring that it<br>reflects the latest user information. The use of helper functions and mixin classes<br>contributes to code organization and reusability.</li></ul><br></td></tr>
<tr><td> <em>Sub-Task 7: </em> Explain briefly how the process/code works for role-protected pages</td></tr>
<tr><td> <em>Response:</em> <p>permission_denied function is a custom error handler for handling permission denied (403) errors.<br>It returns a rendered template for a custom 403 error page and sets<br>the HTTP status code to 403. So role protected pages will not get<br>accessed if user doesn&#39;t have the specific role for that resource.<br><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Feature: Site should have basic styles/theme applied; everything should be styled </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots to show examples of your site's styles/theme</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-13T19.46.34image.png.webp?alt=media&token=ec5537a5-6693-402b-81bd-1c20416433ae"/></td></tr>
<tr><td> <em>Caption:</em> <p>Homepage with Nav bar styled<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-13T19.47.19image.png.webp?alt=media&token=d5dc9e70-3405-45c2-9499-b257a5e21464"/></td></tr>
<tr><td> <em>Caption:</em> <p>Add Sample form<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-13T19.48.41image.png.webp?alt=media&token=914b738c-8ad1-4550-bffb-640495ac2554"/></td></tr>
<tr><td> <em>Caption:</em> <p>List Samples<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-13T20.04.10image.png.webp?alt=media&token=8e3f6e48-7ef0-4d9c-b422-b1acc63e9aa4"/></td></tr>
<tr><td> <em>Caption:</em> <p>Create role form<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-13T20.04.57image.png.webp?alt=media&token=98cb4ff6-0aa5-489f-9223-f9897d3dda9f"/></td></tr>
<tr><td> <em>Caption:</em> <p>list roles form<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-13T20.05.31image.png.webp?alt=media&token=304f964e-83c8-4ed5-91de-f9db4da69130"/></td></tr>
<tr><td> <em>Caption:</em> <p>Assign roles form<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Suchith-Balne/sb2648-is601-007/pull/22">https://github.com/Suchith-Balne/sb2648-is601-007/pull/22</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain your CSS at a high level</td></tr>
<tr><td> <em>Response:</em> <p>CSS is a style sheet language used for describing the look and formatting<br>of a document written in HTML or XML. It enables the separation of<br>document content and presentation, allowing developers to control the appearance of web pages.<br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Feature: Any output messages/errors should be "user friendly" </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of some examples of errors/messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-13T23.47.49image.png.webp?alt=media&token=edaa5b0c-7e6f-44f8-992b-0e5ec5a96a9f"/></td></tr>
<tr><td> <em>Caption:</em> <p>Permission Denied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-13T23.52.44image.png.webp?alt=media&token=66cdcbbb-9d15-4a04-9786-392b3fa4fa9a"/></td></tr>
<tr><td> <em>Caption:</em> <p>Login without any credentials<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-14T00.23.06image.png.webp?alt=media&token=b5fd3aef-f19a-44a9-b98b-d363e8f8d0a2"/></td></tr>
<tr><td> <em>Caption:</em> <p>User without login error<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a related pull request</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Suchith-Balne/sb2648-is601-007/pull/22">https://github.com/Suchith-Balne/sb2648-is601-007/pull/22</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Briefly explain how you made messages user friendly</td></tr>
<tr><td> <em>Response:</em> <div><b>Permission Denied, you don't have sufficient permissions</b>: Occurs when user tries to access<br>a resource which he is not allowed to use as the resource is<br>not specified for the role.</div><div><b>Please fill this field</b>: This occurs when no credentials<br>are supplied and trying to login.</div><div><b>Sorry, you don't have permissions to access this<br>resource. Please try after login</b>: This occurs when user is trying to access<br>resources without login.<br></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Feature: Users will be able to see their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-13T23.57.08image.png.webp?alt=media&token=54f1b7e5-5670-4f99-9608-eae505173de4"/></td></tr>
<tr><td> <em>Caption:</em> <p>Email and username prefilled<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Suchith-Balne/sb2648-is601-007/pull/22">https://github.com/Suchith-Balne/sb2648-is601-007/pull/22</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Explain briefly how the process/code works (view only)</td></tr>
<tr><td> <em>Response:</em> <ul><li>A new instance of the ProfileForm class is created. This form likely contains<br>fields such as email, username, current password, new password, and password confirmation.</li></ul><ul><li>The code<br>attempts to retrieve the user's information (email and username) from the IS601_Users table<br>in the database based on the user_id. If successful, a new User instance<br>is created with the retrieved data, and the form fields are populated with<br>the existing values.</li></ul><ul><li>After updating the form fields, the code updates the current_user object<br>and the user data stored in the session. This ensures that any changes<br>made during the profile editing process are reflected in the current user session.</li></ul><ul><li>Finally,<br>the template profile.html is rendered, passing the populated form to be displayed.</li></ul><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Feature: User will be able to edit their profile </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the User Profile page validation messages and success messages</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-13T23.59.44image.png.webp?alt=media&token=08731eab-0946-45ae-9b3c-d72d904615d1"/></td></tr>
<tr><td> <em>Caption:</em> <p>Email validation on profile page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-14T00.04.00image.png.webp?alt=media&token=f72c21f5-ecf4-479e-b0bf-85eba3e1c7ec"/></td></tr>
<tr><td> <em>Caption:</em> <p>invalid password<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-14T00.06.03image.png.webp?alt=media&token=76665f76-2ee5-44f0-9ed0-918ac7835a48"/></td></tr>
<tr><td> <em>Caption:</em> <p>Password mismatch<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-14T00.07.49image.png.webp?alt=media&token=45f700e3-850f-4a67-a4b1-d9a4c35ab869"/></td></tr>
<tr><td> <em>Caption:</em> <p>user already in use<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add before and after screenshots of the Users table when a user edits their profile</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-13T22.07.43image.png.webp?alt=media&token=7fc94864-24fa-414d-8646-b12432a8d5cf"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before database screenshot<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-13T22.41.05image.png.webp?alt=media&token=2c5d9a6b-96a1-4f2f-8d58-964f2dd812d3"/></td></tr>
<tr><td> <em>Caption:</em> <p>After database screenshot<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the related pull request(s) for this feature</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Suchith-Balne/sb2648-is601-007/pull/22">https://github.com/Suchith-Balne/sb2648-is601-007/pull/22</a> </td></tr>
<tr><td> <em>Sub-Task 4: </em> Explain briefly how the process/code works (edit only)</td></tr>
<tr><td> <em>Response:</em> <ul><li>The form, ProfileForm, is validated using the validate_on_submit() method. This method triggers the<br>validation of all form fields. If the form passes validation, the logic inside<br>the conditional block is executed.</li></ul><ul><li>The code retrieves the current password, new password, and<br>password confirmation from the form</li></ul><ul><li>If the current password, new password, and password confirmation<br>are provided, the code attempts to retrieve the current hashed password from the<br>database. It then checks if the entered current password matches the stored hash.<br>If the check is successful, a new hash for the new password is<br>generated and updated in the database.</li></ul><ul><li>The email and username are updated in the<br>database. If successful, a success flash message is displayed. The check_duplicate function is<br>used to handle any potential duplicate key violations during the update.</li></ul><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707834-bf5a5b13-ec36-4597-9741-aa830c195be2.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <div>Faced issue while running app with Build Error later after debug fixed the<br>issue as few routes were missing in sample.py file.</div><div>It's interesting to learn how<br>data is added to database and front end rendering.<br></div><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Prod Application Link to Login Page</td></tr>
<tr><td>Not provided</td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-milestone1-deliverable/grade/sb2648" target="_blank">Grading</a></td></tr></table>