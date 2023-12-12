<table><tr><td> <em>Assignment: </em> IS601 Milestone 3 API Project</td></tr>
<tr><td> <em>Student: </em> Suchith Sameeri Balne (sb2648)</td></tr>
<tr><td> <em>Generated: </em> 12/12/2023 3:47:22 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-milestone-3-api-project/grade/sb2648" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone3 branch</li><li>Create a new markdown file called milestone3.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone3.md</li><li>Add/commit/push the changes to Milestone3</li><li>PR Milestone3 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 4</li><li>Submit the direct link to this new milestone3.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on GitHub and everywhere else. Images are only accepted from dev or prod, not localhost. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> API Data Association </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> How will this data relate to the User</td></tr>
<tr><td> <em>Response:</em> <ul><li>In this webiste, user can wishlist the episodes that he want to watch,<br>all the wishlisted episodes will be displayed on the watchlist screen</li><li>User can unfavourite<br>or favourite the episodes that he want to watch</li><li>He can clear all the<br>episodes from the watchlist screen</li><li>Admin can associate or unassociate specific episodes to the<br>users</li><li>Admin can view all the watchlist items per user<br></li></ul><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Data changes</td></tr>
<tr><td> <em>Response:</em> <ul><li>Database can be updated by the admin using the "Update database" available on<br>the Navbar. <br></li><li>In future is the api is updated then the latest data<br>can be sent to database using Update Database button and the functionality remains<br>same without any effects</li><li>It is a many to many relationship<br></li></ul><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Show how/where the user can associate the data with themselves</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-12-12T19.17.48image.png.webp?alt=media&token=73681081-c835-4e8e-8d1e-ae61d5a3d0d5"/></td></tr>
<tr><td> <em>Caption:</em> <p>Yellow button can help track/untrack the episodes <br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-12-12T19.19.39image.png.webp?alt=media&token=86491837-b580-4005-a1f2-8997a101f382"/></td></tr>
<tr><td> <em>Caption:</em> <p>Watchlisted the episode with a message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-12-12T20.04.17image.png.webp?alt=media&token=1e9d5dfd-c587-45ee-a2bb-460a237b8c5f"/></td></tr>
<tr><td> <em>Caption:</em> <p>Python code to associate or unassociate episodes to user<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> List Associated Entities to the logged in user </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show the page where a user can list related/associated entities</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-12-12T19.46.08image.png.webp?alt=media&token=34286ca8-341b-4782-b4f1-1217ac02c904"/></td></tr>
<tr><td> <em>Caption:</em> <p>Wishlist of the logged in user<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-12-12T19.22.15image.png.webp?alt=media&token=1c35d433-05b4-4d71-a3ae-7cbdffa6af9e"/></td></tr>
<tr><td> <em>Caption:</em> <p>Wishlist with filtering<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-12-12T20.10.58image.png.webp?alt=media&token=81b7dba5-189d-4c24-9f05-0223b4146844"/></td></tr>
<tr><td> <em>Caption:</em> <p>Python code for watchlist<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-12-12T20.11.33image.png.webp?alt=media&token=f8674b24-33bc-4d8b-a7b9-a09cb6039e97"/></td></tr>
<tr><td> <em>Caption:</em> <p>Python code for watchlist<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-12-12T20.14.30image.png.webp?alt=media&token=fef6a188-d351-44d3-a459-f0c00a50a2f7"/></td></tr>
<tr><td> <em>Caption:</em> <p>Python code to remove all wishlist items<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add pull request(s) url</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Suchith-Balne/sb2648-is601-007/pull/34">https://github.com/Suchith-Balne/sb2648-is601-007/pull/34</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> List entities associated with users </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show a page that lists entities that are associated with at least 1 user</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-12-12T20.17.06image.png.webp?alt=media&token=0508f204-206c-404c-ab0b-7cb9c5657916"/></td></tr>
<tr><td> <em>Caption:</em> <p>Episodes not associated with any user<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-12-12T20.17.43image.png.webp?alt=media&token=aab50978-a9f9-40de-ac65-4b9a0793aa21"/></td></tr>
<tr><td> <em>Caption:</em> <p>Python code for unwatched episodes<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-12-12T20.20.48image.png.webp?alt=media&token=21b1f198-0f30-4b3e-8b72-c1b0e34971c0"/></td></tr>
<tr><td> <em>Caption:</em> <p>Filtering for unwatched episodes<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-12-12T20.22.19image.png.webp?alt=media&token=cd0ffc5f-36b4-4ffa-be15-20f6482384a1"/></td></tr>
<tr><td> <em>Caption:</em> <p>All users association screen<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-12-12T20.23.11image.png.webp?alt=media&token=4c245efe-5bb7-411f-b59a-bf136c7dd61d"/></td></tr>
<tr><td> <em>Caption:</em> <p>All users association screen<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add pull request(s) url</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Suchith-Balne/sb2648-is601-007/pull/35">https://github.com/Suchith-Balne/sb2648-is601-007/pull/35</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Admin Association Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Admin page to search for users and entities</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-12-12T20.28.59image.png.webp?alt=media&token=c4214e0e-0d5e-44d0-bb95-d13ce9e17510"/></td></tr>
<tr><td> <em>Caption:</em> <p>Admin association page<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-12-12T20.29.23image.png.webp?alt=media&token=5427cb23-80bc-438c-b3ed-b4b7549ecd3b"/></td></tr>
<tr><td> <em>Caption:</em> <p>Association successful<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-12-12T20.30.03image.png.webp?alt=media&token=1e65c0f7-a982-40a9-8bd1-d7371411d5ca"/></td></tr>
<tr><td> <em>Caption:</em> <p>Manage admin associations python code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-12-12T20.30.28image.png.webp?alt=media&token=ebe13118-c61f-4156-ab07-945725e53873"/></td></tr>
<tr><td> <em>Caption:</em> <p>Manage admin associations python code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add pull request(s) url</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Suchith-Balne/sb2648-is601-007/pull/35">https://github.com/Suchith-Balne/sb2648-is601-007/pull/35</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Project Related Screens not yet shown </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshots of other pages not yet shown</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-12-12T20.32.43image.png.webp?alt=media&token=1ea7dc63-f905-4835-9b70-251348e2a575"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot with all the episodes in watchlist<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-12-12T20.32.59image.png.webp?alt=media&token=74482e6f-49ba-40d0-a381-0afff9e3bfa9"/></td></tr>
<tr><td> <em>Caption:</em> <p>Clear all watchlist episodes<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-12-12T20.33.32image.png.webp?alt=media&token=8776448e-4227-4ee0-9a8d-fc4186f162ac"/></td></tr>
<tr><td> <em>Caption:</em> <p>Home screen for the webiste<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain each screen shown above</td></tr>
<tr><td> <em>Response:</em> <div><ul><li>First two screenshots shows the clear all watchlist episodes for the user.</li><li>Second screenshot<br>shows the homescreen of the project where he can access episodes and seasons<br>from the home screen</li></ul></div><div><ul><li>In this webiste, user can wishlist the episodes that he<br>want to <br>watch, all the wishlisted episodes will be displayed on the watchlist<br><br>screen<br>https://is601-sb2648-dev-2beda061efe9.herokuapp.com/episodes/watchlist<br><br></li><li>User can unfavourite or favourite the episodes that he want to watch</li><li>He can<br>clear all the episodes from the watchlist screen<br><br></li><li>Admin can associate or unassociate specific<br>episodes to the users<br>https://is601-sb2648-dev-2beda061efe9.herokuapp.com/episodes/manage<br><br></li><li>Admin can view all the watchlist items per user<br>https://is601-sb2648-dev-2beda061efe9.herokuapp.com/episodes/associations<br></li></ul></div><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add pull request(s) url</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Suchith-Balne/sb2648-is601-007/pull/35">https://github.com/Suchith-Balne/sb2648-is601-007/pull/35</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <div>In this milestone, I have learned how to associate entities to the user<br>and manage resources as a admin.</div><div>Lecture videos and Milestone videos helped me in<br>developing this website <br></div><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-milestone-3-api-project/grade/sb2648" target="_blank">Grading</a></td></tr></table>