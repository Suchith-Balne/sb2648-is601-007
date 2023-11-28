<table><tr><td> <em>Assignment: </em> IS601 Mini Project 3 - Thankful Giving</td></tr>
<tr><td> <em>Student: </em> Suchith Sameeri Balne (sb2648)</td></tr>
<tr><td> <em>Generated: </em> 11/27/2023 3:37:49 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-mini-project-3-thankful-giving/grade/sb2648" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <p><b>Initial Prep:</b><div><ol><li>Create a new app on heroku called course-section-ucid-td</li><ol><li>replace course, section, ucid accordingly</li></ol><li>Go to the Settings tab of the app and add the config var of DB_URL and your DB connection string<br></li><li>Go to your github repository and go to Settings and add a new repository secret called&nbsp;HEROKU_APP_NAME_MP3 and fill in your new app name as the value</li><li>Note: we will just have one instance</li><li>Grab the yml file from the shared branch containing the initial code templates and put it in your .github/workflows folder, you shouldn&#39;t need to edit it</li><li>Make sure Wakatime is setup correctly and recording time correctly</li></ol><div>Baseline code:&nbsp;<a href="https://github.com/MattToegel/IS601/tree/F23-MiniProject-3">https://github.com/MattToegel/IS601/tree/F23-MiniProject-3</a>&nbsp;</div><div>Example Site:&nbsp;<a href="https://is601-mt85-td-f7d7f9bec981.herokuapp.com">https://is601-mt85-td-f7d7f9bec981.herokuapp.com</a></div><div><br></div><div><b>Primary Instructions:</b></div></div><div><ol><li>Checkout any latest branch (dev is fine) and pull the latest changes</li><li>Create a new branch per the recommended name below</li><li>Copy the rest of the files from the shared branch containing the initial code templates</li><ol><li>It&#39;s important that you have just one folder for this project at the root level of your repository, in my example I called mine MP3 and it contains the entire app</li><li>Make sure the .csv files are copied as csv data and not html tables (github may try to render them so choose the &quot;Raw&quot; button of the file to get the raw text)</li></ol><li>Create a virtual environment inside the MP3 related folder and pip install the requirements.txt (you shouldn&#39;t need to manually add anything else)</li><li>Copy your .env file from flask_sample into MP3 (again this should gray out as it should be in the .gitignore files) but it&#39;s necessary for local development</li><li>Once everything is copied over immediately add/commit the changes and record the commit message as something similar to &quot;template files&quot;</li><li>Push the baseline and open a pull request from this branch to dev (don&#39;t merge it until you have the markdown file)</li><li>Execute the init_db.py file for this project to generate the two required tables</li><li>Proceed to solve/implement the missing pieces noted by &quot;TODO&quot; comments throughout the code (which are also shown below in the various deliverables)</li><li>As soon as you start working on an item add your ucid-date as a comment so you don&#39;t forget</li><li><b>Add and commit after each TODO item (or relatively frequently to build up a proper history; do not save this process for the end)</b></li><li>For the below deliverables, you&#39;ll be capturing screenshots from your new heroku app (ensure the url is clearly visible)</li><li>Once finished, copy the markdown or download the file and add it to your MP3 related folder as a .md file (don&#39;t forget the extension)</li><li>Do your final add/commit/push once satisfied that everything is all set</li><li>Merge the pull request that was opened in step 7</li><ol><li>This will trigger a deploy to dev (due to the original yml files) but this app won&#39;t be affected</li></ol><li>Create a pull request from dev to prod and merge it</li><ol><li>This will trigger a deploy to prod (due to the original yml files) but this app won&#39;t be affected</li></ol><li>From the prod branch on github, navigate to your submission.md file and grab that link to paste to Canvas</li></ol><div><b>Objective/Project Description:</b></div></div><div>You&#39;ll be implementing a cross-organization Thanksgiving Drive application.</div><div>There will be CRUD operations to manage organizations and CRUD operations to manage donations related to organizations as well as an import page to preload given data.</div><div>Some files are provided as fully working and should not be modified, typically they&#39;ll have comments like &quot;DO NOT EDIT&quot;.</div><div>Other files are basic skeleton files with a number of &quot;TODO&#39;s&quot; that you need to solve. It&#39;s best to make the code changes near where the particular TODO is (do not delete the TODO comments).</div><div>There are also provided test case files.</div><div>Between the TODOs and the tests you must implement the missing pieces to get all tests to pass for full credit.</div><div>Do not edit any of the test cases except for a caveat I&#39;ll mention in another paragraph below.</div><div><br></div><div><b>Caveat:</b><br>If you can&#39;t solve a test case first ensure you run <code>pytest -rA</code> locally to show and capture the test pass/fail summary, then for any of the cases you can&#39;t achieve add the word &quot;off_&quot; in front of the function name. (i.e., if a test is test_myfile() rename it to off_test_myfile()).</div><div>This will disable the test case allowing you to deploy to potentially receive partial credit.</div><div><br></div><div>Files you shouldn&#39;t edit:</div><div>layout.html</div><div>country_state_selector.html</div><div>flash.html</div><div>organization_dropdown.html</div><div>sort_filter.html</div><div>any test files (unless it&#39;s for the caveat)</div><div>requirements.txt</div><div>Dockerfile</div><div>any files in the sql folder</div><div>geography.py</div><div>index.py</div><div>main.py</div><div><br></div><div><br></div><div><br></div><div><br></div><div><br></div><div><br></div></p>
</td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Solving the index.html template </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of the index.html page being shown and of the code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-27T17.27.49image.png.webp?alt=media&token=77592b2c-98e4-4643-8eaf-75d305035fda"/></td></tr>
<tr><td> <em>Caption:</em> <p>Home screenshot i.e index.html<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-27T17.29.15image.png.webp?alt=media&token=90eacf22-8b24-401e-b05a-6a1e470e2d23"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot of index.html code<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Solving the nav.html template </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots showing the navbar and the edited code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-27T17.45.02image.png.webp?alt=media&token=27258ee9-d9be-47df-b247-670e5863759b"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code screenshot for the navigation bar<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-27T17.46.01image.png.webp?alt=media&token=01df847c-6987-4b31-b423-1535861ebce1"/></td></tr>
<tr><td> <em>Caption:</em> <p>Navbar screenshot<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Solving the admin upload </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots showing the code changes related to the checklist</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-27T17.48.37image.png.webp?alt=media&token=22021e51-2a44-4618-a733-7be43a33742e"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for Import CSV<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-27T17.50.40image.png.webp?alt=media&token=f8be4efa-fc16-4010-958b-5d52b453d35a"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for read csv as Dict, Organization and donation data extraction<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-27T17.53.48image.png.webp?alt=media&token=1e8792f3-3169-4ed0-810a-d6e4bf7d16c8"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for flash message with number of organizations, if no organizations were eligible/processed,number<br>of donations that were successfully processed,if no donations were eligible/processed<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Solve the donation related logic and requirements </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of create and edit views of donations (from the browser) and of the code of the html page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-27T18.02.30image.png.webp?alt=media&token=6a98af1c-3756-4f8d-b6c4-1ee318691bda"/></td></tr>
<tr><td> <em>Caption:</em> <p>Create view with all fields empty<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-27T18.19.51image.png.webp?alt=media&token=488a708d-cbf0-461f-a8cc-bd18ef55785f"/></td></tr>
<tr><td> <em>Caption:</em> <p>Edit view with pre-populated data<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-27T18.40.01image.png.webp?alt=media&token=4b9b7eeb-db7c-45b2-8cc7-1fbd26190141"/></td></tr>
<tr><td> <em>Caption:</em> <p>Todo items for edit 5- 11<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-27T18.41.43image.png.webp?alt=media&token=596add4f-4068-4557-94e5-bc1a91ecb2cc"/></td></tr>
<tr><td> <em>Caption:</em> <p>Todo items for edit 1- 5<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-27T18.43.04image.png.webp?alt=media&token=7504e12b-cf38-4221-a163-2ff7a6c6994a"/></td></tr>
<tr><td> <em>Caption:</em> <p>Todo items for edit 12-15<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-27T18.44.38image.png.webp?alt=media&token=6be199db-1d12-4e26-b4ed-2f60a56b7b36"/></td></tr>
<tr><td> <em>Caption:</em> <p>Todo items for add 1-4<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-27T18.45.33image.png.webp?alt=media&token=007473a8-6971-451b-9111-09f59cf3ca70"/></td></tr>
<tr><td> <em>Caption:</em> <p>Todo items for add 5-9<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-27T18.47.25image.png.webp?alt=media&token=4d257082-a064-4918-a9ce-510b40c471ef"/></td></tr>
<tr><td> <em>Caption:</em> <p>Todo items for add 10<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshots of the search page of donations (from the browser) and of the code of the html page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-27T18.34.53image.png.webp?alt=media&token=fbdba436-6a0a-488d-99d7-4c2aa8e40202"/></td></tr>
<tr><td> <em>Caption:</em> <p>Donations Search page with no filters applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-27T18.35.55image.png.webp?alt=media&token=25fd84e7-3904-452b-a02e-7634fa2cb56d"/></td></tr>
<tr><td> <em>Caption:</em> <p>Search donations with filter applied<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-27T19.07.33image.png.webp?alt=media&token=5226fdf5-a9de-428b-be3a-50b3d35f7872"/></td></tr>
<tr><td> <em>Caption:</em> <p>Search donations with organization name<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-27T19.15.32image.png.webp?alt=media&token=02391091-616b-417a-b7ac-33b3f0ea3e15"/></td></tr>
<tr><td> <em>Caption:</em> <p>Html code for search form <br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-27T19.15.56image.png.webp?alt=media&token=8f1140a1-beac-47c1-aa70-68df87c586bb"/></td></tr>
<tr><td> <em>Caption:</em> <p>Html code for search form <br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-27T19.16.20image.png.webp?alt=media&token=8a2c2c97-c3b5-491b-8ab7-0df6861e6da4"/></td></tr>
<tr><td> <em>Caption:</em> <p>Html code for search form <br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-27T19.16.35image.png.webp?alt=media&token=7d9719ff-a2c1-40c7-a630-2f590ef2a165"/></td></tr>
<tr><td> <em>Caption:</em> <p>Html code for search form <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshots of the donations search route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-27T19.17.46image.png.webp?alt=media&token=8577ff03-867a-4735-b291-7be98a15bf27"/></td></tr>
<tr><td> <em>Caption:</em> <p>Search donations todo 1-5<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-27T19.18.38image.png.webp?alt=media&token=5096322c-6d63-4bbe-90ce-3a920f92e6bb"/></td></tr>
<tr><td> <em>Caption:</em> <p>Search donations todo 6-10<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-27T19.19.47image.png.webp?alt=media&token=13153a36-5b23-4a71-921a-89e4c70733cd"/></td></tr>
<tr><td> <em>Caption:</em> <p>Search donations todo 11-13<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add screenshots of the donations add route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-27T19.20.45image.png.webp?alt=media&token=4cb424c1-fe67-47d6-9d05-40d29a75527e"/></td></tr>
<tr><td> <em>Caption:</em> <p>Add logic for donations Todo 1-4<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-27T19.21.07image.png.webp?alt=media&token=0dcf5880-3ffa-4517-ba46-faaf5e8d175c"/></td></tr>
<tr><td> <em>Caption:</em> <p>Add logic for donations Todo 5-10<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-27T19.21.38image.png.webp?alt=media&token=14b92aad-2e8f-4027-a695-52de573be70b"/></td></tr>
<tr><td> <em>Caption:</em> <p>Add logic for donations Todo 11-14<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add screenshots of donations edit route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-27T19.25.04image.png.webp?alt=media&token=4cfe28ac-6d76-4770-a581-f3e00b102c4d"/></td></tr>
<tr><td> <em>Caption:</em> <p>Edit logic for donations todo 1-5 <br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-27T19.26.02image.png.webp?alt=media&token=97616053-4eb1-4d1e-90c5-5bb08defa1f6"/></td></tr>
<tr><td> <em>Caption:</em> <p>Edit logic for donations todo 6-11<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-27T19.27.43image.png.webp?alt=media&token=45352ea3-754d-4f62-ad8b-4db838fe486c"/></td></tr>
<tr><td> <em>Caption:</em> <p>Edit logic for donations todo 11-13<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-27T19.28.37image.png.webp?alt=media&token=896902ff-2c0c-4497-9a99-eb8de7a09444"/></td></tr>
<tr><td> <em>Caption:</em> <p>Edit logic for donations todo 14-15<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add screenshots of the donation delete route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-27T19.30.16image.png.webp?alt=media&token=9a72e895-69b9-40e4-8954-f54aad178b2e"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for delete route<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-27T19.31.21image.png.webp?alt=media&token=a09792f1-0172-47e5-9b99-4643d9d12bdb"/></td></tr>
<tr><td> <em>Caption:</em> <p>Delete web application screenshot<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Solve the organization related logic and requirements </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of create and edit views of organizations (from the browser) and of the html code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-27T19.32.50image.png.webp?alt=media&token=6ad82d52-f9c8-4c3f-aeac-20765d757ae0"/></td></tr>
<tr><td> <em>Caption:</em> <p>Add  organization page with empty fields<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-27T19.47.15image.png.webp?alt=media&token=0a20bcfb-ea2b-404a-8ef0-89777122bed0"/></td></tr>
<tr><td> <em>Caption:</em> <p>Edit organization page with pre populated fields<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-27T19.52.43image.png.webp?alt=media&token=600afee4-4bc3-4d10-9482-a94b5d63d97f"/></td></tr>
<tr><td> <em>Caption:</em> <p>List_organizations page for add organizations<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-27T19.53.22image.png.webp?alt=media&token=f2147d4b-728d-4f0c-b778-5bc28d0f9b33"/></td></tr>
<tr><td> <em>Caption:</em> <p>list_organizations page for add organizations <br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-27T19.54.00image.png.webp?alt=media&token=898be86e-bddb-4fbe-aabc-5386ad670bc3"/></td></tr>
<tr><td> <em>Caption:</em> <p>list_organizations page for add organizations<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-27T19.54.45image.png.webp?alt=media&token=4992f612-35cb-45e7-beeb-2fc4992c5cef"/></td></tr>
<tr><td> <em>Caption:</em> <p>manage_organizations code for edit organizations<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-27T19.55.24image.png.webp?alt=media&token=d40d195e-f0c6-4747-8427-fc17291e1533"/></td></tr>
<tr><td> <em>Caption:</em> <p>Manage_organizations code for edit organizations<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshots of the search page of organizations (from the browser) and of the html code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-27T19.56.26image.png.webp?alt=media&token=ddc816dc-cc63-45c3-b18a-69b885cec598"/></td></tr>
<tr><td> <em>Caption:</em> <p>Search organizations without filters<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-27T19.58.03image.png.webp?alt=media&token=682bc58b-0f1f-40b8-ab9e-da33a1305dfc"/></td></tr>
<tr><td> <em>Caption:</em> <p>Search organizations with filter<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-27T20.00.22image.png.webp?alt=media&token=b5bcb16f-931c-4f70-8b4a-9883d9745a26"/></td></tr>
<tr><td> <em>Caption:</em> <p>Search organizations with multiple filters<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-27T20.02.00image.png.webp?alt=media&token=03276fb6-19a8-4376-88ff-2b1ee61f41b0"/></td></tr>
<tr><td> <em>Caption:</em> <p>Filter for organizations html code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of the organization search route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-27T20.03.34image.png.webp?alt=media&token=f27f4eca-dcbb-49fc-8967-027778c9b303"/></td></tr>
<tr><td> <em>Caption:</em> <p>Search organizations code for  todo 1-5<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-27T20.05.03image.png.webp?alt=media&token=9f6afd98-883c-40ca-9d9a-275f02ad2805"/></td></tr>
<tr><td> <em>Caption:</em> <p>Search organizations code for todo 6-9<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add screenshots of organization add route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-27T20.06.57image.png.webp?alt=media&token=7e27ba33-9677-41c9-bc92-1fc345bcef2b"/></td></tr>
<tr><td> <em>Caption:</em> <p>Add organization code todo 1-5<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-27T20.08.45image.png.webp?alt=media&token=07efb9eb-da9e-4683-a6e5-4d24b9d213bd"/></td></tr>
<tr><td> <em>Caption:</em> <p>Add organization code todo 5-8<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-27T20.09.54image.png.webp?alt=media&token=bdd4df5d-7491-4d6d-9778-66e6403e8f9e"/></td></tr>
<tr><td> <em>Caption:</em> <p>Add organization for description<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Add screenshots of organization edit route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-27T20.11.18image.png.webp?alt=media&token=fefe0c72-ff6e-4cdf-a2e1-0b6cb0400578"/></td></tr>
<tr><td> <em>Caption:</em> <p>Edit organization code for todo 1-6<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-27T20.13.00image.png.webp?alt=media&token=7f059d49-4f99-4b23-9949-af3c4d8cde09"/></td></tr>
<tr><td> <em>Caption:</em> <p>Edit organizations code for todo 6-9<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-27T20.13.21image.png.webp?alt=media&token=09791329-abc7-41c2-97b6-3969a04e369d"/></td></tr>
<tr><td> <em>Caption:</em> <p>Edit organizations code for todo 10-13<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Add screenshots of organization delete route code</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-27T20.14.57image.png.webp?alt=media&token=719951ef-c08b-4d93-8404-822e96b9983d"/></td></tr>
<tr><td> <em>Caption:</em> <p>Delete organizations code with all todos <br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-27T20.16.09image.png.webp?alt=media&token=1f25b534-b5df-439a-b9db-6d1f0394fc1f"/></td></tr>
<tr><td> <em>Caption:</em> <p>Organizations before delete<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-27T20.16.26image.png.webp?alt=media&token=65ca17b1-7e1b-465f-b16d-265f3627d788"/></td></tr>
<tr><td> <em>Caption:</em> <p>Organizations after delete<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Test cases </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of passing test_donations.py using -rA</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-27T20.21.28image.png.webp?alt=media&token=e984e7af-7b46-4357-bb70-b7c76dbe509c"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test cases output Pytest -rA<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot of passing test_organizations.py using -rA</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-27T20.22.03image.png.webp?alt=media&token=a89a537b-0074-4df8-8a7f-27863366ce73"/></td></tr>
<tr><td> <em>Caption:</em> <p>Pytest result for organizations<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add screenshot of passing test_upload.py using -rA</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-27T20.23.27image.png.webp?alt=media&token=130934d1-fca6-4045-aa12-19a9b89b1ad0"/></td></tr>
<tr><td> <em>Caption:</em> <p>pytest result for test_upload<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add screenshot of passing test_index.py using -rA</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-27T20.24.19image.png.webp?alt=media&token=b9362483-062b-4375-8fb3-11f54bc8149a"/></td></tr>
<tr><td> <em>Caption:</em> <p>pytest result for test_index<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Did all tests pass? If no, list which failed and explain why</td></tr>
<tr><td> <em>Response:</em> <p>PASSED test/test_upload.py::test_upload_csv<br><div>ERROR test/test_upload.py::test_upload_csv - Exception: Error while executing statement: Cannot delete or update<br>a parent row: a foreign key constraint fails</div><div><br></div><div>This test case failed due to<br>some foreign key constraint but this website is working fine for delete organization<br>and delete donations.<br></div><br></p><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add pull request link for this assignment branch</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Suchith-Balne/sb2648-is601-007/pull/26">https://github.com/Suchith-Balne/sb2648-is601-007/pull/26</a> </td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshots of your commit history</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-27T20.29.40image.png.webp?alt=media&token=532fc6da-4d4a-4fb4-94ae-a4d48a1a6d6c"/></td></tr>
<tr><td> <em>Caption:</em> <p>Commit history screenshot<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add a screenshot of your wakatime dashboard for this class/project</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-27T20.31.57image.png.webp?alt=media&token=2374514c-edb6-4b18-90ac-3721627d50d2"/></td></tr>
<tr><td> <em>Caption:</em> <p>Wakatime chart<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-27T20.35.30image.png.webp?alt=media&token=ae185cf4-b726-4bfe-ba12-c2f1b63219a8"/></td></tr>
<tr><td> <em>Caption:</em> <p>wakatime graph<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-11-27T20.36.00image.png.webp?alt=media&token=477b8d48-c3f2-4e38-a802-6f5a4b0a4611"/></td></tr>
<tr><td> <em>Caption:</em> <p>wakatime<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a link to the application from the new vm/app</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-007-sb2648-td-acf8f1202ceb.herokuapp.com/">https://is601-007-sb2648-td-acf8f1202ceb.herokuapp.com/</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-mini-project-3-thankful-giving/grade/sb2648" target="_blank">Grading</a></td></tr></table>