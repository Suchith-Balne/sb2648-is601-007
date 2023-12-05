<table><tr><td> <em>Assignment: </em> IS601 Milestone 2 API Project</td></tr>
<tr><td> <em>Student: </em> Suchith Sameeri Balne (sb2648)</td></tr>
<tr><td> <em>Generated: </em> 12/5/2023 2:23:54 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-milestone-2-api-project/grade/sb2648" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Checkout Milestone2 branch</li><li>Create a new markdown file called milestone2.md</li><li>git add/commit/push immediate</li><li>Fill in the below deliverables</li><li>At the end copy the markdown and paste it into milestone2.md</li><li>Add/commit/push the changes to Milestone2</li><li>PR Milestone2 to dev and verify</li><li>PR dev to prod and verify</li><li>Checkout dev locally and pull changes to get ready for Milestone 3</li><li>Submit the direct link to this new milestone2.md file from your GitHub prod branch to Canvas</li></ol><p>Note: Ensure all images appear properly on github and everywhere else. Images are only accepted from dev or prod, not local host. All website links must be from prod (you can assume/infer this by getting your dev URL and changing dev to prod).</p></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> API Details </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Which API did you choose?</td></tr>
<tr><td> <em>Response:</em> <div>API name: Watchmode</div><div>API base url: https://watchmode.p.rapidapi.com</div><div>API link: https://rapidapi.com/meteoric-llc-meteoric-llc-default/api/watchmode/</div><div>API Documentation link: https://api.watchmode.com/docs/</div><div><br></div><div><br></div><div><br></div><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Which endpoints will be used?</td></tr>
<tr><td> <em>Response:</em> <p><a href="https://watchmode.p.rapidapi.com/title/3173903/episodes/">https://watchmode.p.rapidapi.com/title/3173903/episodes/</a><br><a href="https://watchmode.p.rapidapi.com/title/3173903/seasons">https://watchmode.p.rapidapi.com/title/3173903/seasons</a><br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> What pieces of data will be used in your app?</td></tr>
<tr><td> <em>Response:</em> <div>I'm designing a application with seasons and their episodes data and to perform<br>CRUD on the episodes and Seasons database.<br><br></div><div><b>Response for Title episodes:</b></div><div><b><br></b></div><div>id:6088251<br>name:"Winter Is Coming"<br>episode_number:1<br>season_number:1<br>season_id:2<br>tmdb_id:63056<br>imdb_id:"tt1480055"<br>thumbnail_url:"https://cdn.watchmode.com/episode_thumbnails/036088251_thumb_208.jpg"<br>release_date:"2011-04-17"<br>runtime_minutes:62<br>overview:"Jon Arryn,<br>the Hand of the King, is dead. King Robert Baratheon plans to ask<br>his oldest friend, Eddard Stark, to take Jon's place. Across the sea, Viserys<br>Targaryen plans to wed his sister to a nomadic warlord in exchange for<br>an army."</div><div><br></div><div>From this data , fileds: (name, episode_number, season_number, season_id,thumbnail_url,&nbsp;release_date,&nbsp; runtime_minutes, overview) will<br>be shown to the user for each episodes.</div><div><br></div><div><b>Response for Title seasons:</b></div><div>id:91910<br>poster_url:"https://cdn.watchmode.com/posters/0391910_season_poster_342.jpg"<br>name:"Season 5"<br>overview:"In season<br>five, Walt is faced with the prospect of moving on in a world<br>without his enemy. As the pressure of a criminal life starts to build,<br>Skyler struggles to keep Walt’s terrible secrets. Facing resistance from sometime adversary and<br>former Fring lieutenant Mike, Walt tries to keep his world from falling apart<br>even as his DEA Agent brother in law, Hank, finds numerous leads that<br>could blaze a path straight to Walt.&nbsp; All bad things must come to<br>an end."<br>number:5<br>air_date:"2012-07-15"<br>episode_count:16</div><div><br></div><div>From this response, fields such as poster_url, name, overview, number air_date and<br>episode_count is shown to the user.</div><div>Using season ID to retrieve all the episodes<br>for a season using a DB query. <br></div><div><b><br></b></div><div><b><br></b></div><div><br></div><div><br></div><div><br></div><br></td></tr>
<tr><td> <em>Sub-Task 4: </em> How will you use the mapped data?</td></tr>
<tr><td> <em>Response:</em> <div><ul><li>The mapped data from the Json response is inserted to the database.</li><li>Once the<br>data is available in the database.Data retrieval is done to show the data<br>to the user under /list rest call for the seasons.</li><li>Whenever the user clicks<br>on the particular season then all the episodes for that season are displayed<br>in episodes screen</li><li>User will be able to edit and delete both the seasons<br>and episodes records.</li><li>Season_id is present in both the tables so to retrieve episodes<br>by seasons a custom db query is made to get the relevant information</li></ul></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Create Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show the create page</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-12-05T17.53.27image.png.webp?alt=media&token=519e6171-5c09-4341-a011-132809d3e6b6"/></td></tr>
<tr><td> <em>Caption:</em> <p>Create Season and add the data to database<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-12-05T17.52.53image.png.webp?alt=media&token=de2316e0-dd38-4b4b-afe5-ddb17b78a2f4"/></td></tr>
<tr><td> <em>Caption:</em> <p>Validation error for the required field in season form<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-12-05T17.54.24image.png.webp?alt=media&token=cd4b4d88-c265-4b2e-836d-4b6057c7dd7e"/></td></tr>
<tr><td> <em>Caption:</em> <p>Created episode with success flash message in season form<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-12-05T17.57.27image.png.webp?alt=media&token=7a575534-0c53-401a-b381-f51206b996aa"/></td></tr>
<tr><td> <em>Caption:</em> <p>Added episode is displayed in views page in season form<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-12-05T18.00.12image.png.webp?alt=media&token=f7e653cb-4261-4b4f-a131-7d3be1351f2c"/></td></tr>
<tr><td> <em>Caption:</em> <p>Duplicate data is not added to the database in season form<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-12-05T18.03.16image.png.webp?alt=media&token=78e8be5e-63c9-4469-b375-ac4ba4bf98b6"/></td></tr>
<tr><td> <em>Caption:</em> <p>Add Episodes to the database form<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-12-05T18.04.00image.png.webp?alt=media&token=f34d1fc2-e216-490d-a0c2-86212e89c6a0"/></td></tr>
<tr><td> <em>Caption:</em> <p>Episode Form validation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-12-05T18.04.48image.png.webp?alt=media&token=083c734b-86f3-4c89-941e-8c302afaeee4"/></td></tr>
<tr><td> <em>Caption:</em> <p>Flash message with success message upon adding new episodes to database<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-12-05T18.05.36image.png.webp?alt=media&token=93cfda72-2066-48b4-b4dd-5962163d6050"/></td></tr>
<tr><td> <em>Caption:</em> <p>New episode is added to the database <br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-12-05T18.07.02image.png.webp?alt=media&token=66cdd57f-3dc2-4390-9226-ac23727cbb96"/></td></tr>
<tr><td> <em>Caption:</em> <p>HTML code for add season<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-12-05T18.07.32image.png.webp?alt=media&token=7ead1b7b-ca5f-45d6-8035-47165e8f6f2e"/></td></tr>
<tr><td> <em>Caption:</em> <p>HTML code for add season<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-12-05T18.08.01image.png.webp?alt=media&token=d21849ec-1696-4aed-96ed-852c5e9eaeed"/></td></tr>
<tr><td> <em>Caption:</em> <p>HTML code for add episode<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-12-05T18.08.54image.png.webp?alt=media&token=c2e5e4af-8cb0-46ce-af2a-2c9d25666e11"/></td></tr>
<tr><td> <em>Caption:</em> <p>HTML code for Add episode<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-12-05T18.09.43image.png.webp?alt=media&token=a980c3a1-12fe-49bf-bba2-3b422c3af73e"/></td></tr>
<tr><td> <em>Caption:</em> <p>Python code for add episode<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-12-05T18.10.15image.png.webp?alt=media&token=c8533531-5b68-47e5-83ca-c2f34a4f0fb7"/></td></tr>
<tr><td> <em>Caption:</em> <p>Python code for add episode<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-12-05T18.10.56image.png.webp?alt=media&token=1d75fd8f-0801-4fc9-a392-d1fd8eb43ba1"/></td></tr>
<tr><td> <em>Caption:</em> <p>Python code for add season<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-12-05T18.11.10image.png.webp?alt=media&token=ff3c55d7-7fd8-4463-af04-9cc1e65d38eb"/></td></tr>
<tr><td> <em>Caption:</em> <p>Python code for add season<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Show the new data in the database</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-12-05T18.13.03image.png.webp?alt=media&token=7b65908f-7702-47e4-bd8d-8727eb330190"/></td></tr>
<tr><td> <em>Caption:</em> <p>New data was added to the episodes database<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-12-05T18.14.14image.png.webp?alt=media&token=7418455e-28e5-4aa6-b4b7-0e6730b90882"/></td></tr>
<tr><td> <em>Caption:</em> <p>New data was added to the seasons database<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Include related pull request(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Suchith-Balne/sb2648-is601-007/pull/29">https://github.com/Suchith-Balne/sb2648-is601-007/pull/29</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> List Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Have a page that lists the application entities (both API and custom)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-12-05T18.16.00image.png.webp?alt=media&token=56a8421e-c68e-4525-b45b-a459843870b2"/></td></tr>
<tr><td> <em>Caption:</em> <p>Seasons list view<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-12-05T18.16.24image.png.webp?alt=media&token=1e3f2d27-e1d7-4a6d-8175-6cc1411ad9db"/></td></tr>
<tr><td> <em>Caption:</em> <p>Episodes list view<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-12-05T18.28.49image.png.webp?alt=media&token=c91435bf-2292-4c01-89df-2059702bf7e4"/></td></tr>
<tr><td> <em>Caption:</em> <p>No matching filter message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-12-05T18.32.16image.png.webp?alt=media&token=e474aca2-3826-41d1-9ea9-d3259bd4b3d1"/></td></tr>
<tr><td> <em>Caption:</em> <p>Highlighted data is custom data and other episodes are api based records<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-12-05T18.34.34image.png.webp?alt=media&token=49df1edf-bf87-4a08-a95b-74aae0ea5d64"/></td></tr>
<tr><td> <em>Caption:</em> <p>Link to view episodes for this season<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-12-05T19.11.51image.png.webp?alt=media&token=ed11af58-ea1d-42b9-ab3b-8871d5db4b86"/></td></tr>
<tr><td> <em>Caption:</em> <p>List seasons python code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-12-05T19.12.45image.png.webp?alt=media&token=6470f6b8-cfdd-418a-95a2-0973e5005e3b"/></td></tr>
<tr><td> <em>Caption:</em> <p>List episodes python code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Include related pull request(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Suchith-Balne/sb2648-is601-007/pull/28">https://github.com/Suchith-Balne/sb2648-is601-007/pull/28</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> View Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Have a page showing a single entity with more details shown</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-12-05T18.35.39image.png.webp?alt=media&token=a95d3453-ebd0-4dd3-9605-4e3d0238329f"/></td></tr>
<tr><td> <em>Caption:</em> <p>View episodes by season ID<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-12-05T18.36.10image.png.webp?alt=media&token=ce539f78-cb5d-45b1-9aba-d984b68edfce"/></td></tr>
<tr><td> <em>Caption:</em> <p>No episodes available for invalid id message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Include related pull request(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Suchith-Balne/sb2648-is601-007/pull/28">https://github.com/Suchith-Balne/sb2648-is601-007/pull/28</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Edit Page </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Have a page to edit a single entity</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-12-05T18.37.11image.png.webp?alt=media&token=4ffc85fb-dd83-4fda-b55b-59601579353a"/></td></tr>
<tr><td> <em>Caption:</em> <p>Edit screen of Seasons<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-12-05T18.38.28image.png.webp?alt=media&token=26bb3aab-a82e-49ae-9289-fb3f4769327e"/></td></tr>
<tr><td> <em>Caption:</em> <p>Flash message and redirected to view when Invalid ID is given<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-12-05T18.39.19image.png.webp?alt=media&token=49ccf7e3-2348-4797-978e-469a1aa4ba41"/></td></tr>
<tr><td> <em>Caption:</em> <p>Validation message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-12-05T18.42.26image.png.webp?alt=media&token=f427ab2a-ba61-44cc-b45a-714f8b06da0d"/></td></tr>
<tr><td> <em>Caption:</em> <p>Updated tmdbid field<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-12-05T18.42.44image.png.webp?alt=media&token=ae7c2823-7248-4a44-b630-790b5cee681f"/></td></tr>
<tr><td> <em>Caption:</em> <p>Successfully updated<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Database</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-12-05T18.43.25image.png.webp?alt=media&token=7f0b1fe9-92e1-4b8e-a3cc-60d067dee034"/></td></tr>
<tr><td> <em>Caption:</em> <p>After the update of record in database<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-12-05T18.44.48image.png.webp?alt=media&token=dbc1ebf5-9297-47c2-9224-24049e7e9d10"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before the update in Database<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Include related pull request(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Suchith-Balne/sb2648-is601-007/pull/30">https://github.com/Suchith-Balne/sb2648-is601-007/pull/30</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Delete </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Have a route for deletion logic</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-12-05T18.47.55image.png.webp?alt=media&token=fd198b6e-f636-45c1-9fa3-a568366cce77"/></td></tr>
<tr><td> <em>Caption:</em> <p>Deleting last record<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-12-05T18.48.11image.png.webp?alt=media&token=a48b7a0d-cfb0-4b3f-a198-e683973e7d17"/></td></tr>
<tr><td> <em>Caption:</em> <p>Record deleted successfully<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-12-05T19.13.59image.png.webp?alt=media&token=3bc0d7e8-a8a8-48b2-8b8c-1e9240195e2c"/></td></tr>
<tr><td> <em>Caption:</em> <p>Delete episode python code<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-12-05T19.14.54image.png.webp?alt=media&token=cef7aa8a-1afc-4a2f-a745-99f94077a1c6"/></td></tr>
<tr><td> <em>Caption:</em> <p>Delete season python code<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Database</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-12-05T18.47.21image.png.webp?alt=media&token=db0aa31b-3288-419c-8737-e7c3bb8cd200"/></td></tr>
<tr><td> <em>Caption:</em> <p>Database records before delete<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-12-05T18.48.52image.png.webp?alt=media&token=4c11b77f-da32-43c2-9048-36c0c3f54a19"/></td></tr>
<tr><td> <em>Caption:</em> <p>Database records after delete<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Include related pull request(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Suchith-Balne/sb2648-is601-007/pull/31">https://github.com/Suchith-Balne/sb2648-is601-007/pull/31</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> API Data Loading </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Show information related to API data loading</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-12-05T18.52.32image.png.webp?alt=media&token=99ed0e8c-7013-4499-bf70-6f29d91a2e88"/></td></tr>
<tr><td> <em>Caption:</em> <p>When /update_data is called episodes and seasons data gets updated to database<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-12-05T18.53.26image.png.webp?alt=media&token=2b0be255-89d5-4c33-8eca-d8490e9f2dd7"/></td></tr>
<tr><td> <em>Caption:</em> <p>Duplicate records are handled by &quot;ON DUPLICATE KEY UPDATE&quot; in sql command<br><br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-12-05T18.54.23image.png.webp?alt=media&token=d7ae787d-49e9-43b0-8253-55547ae538ed"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for handling episodes data<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-12-05T18.54.49image.png.webp?alt=media&token=72bb2d5c-1504-437d-b1c0-eecf2db3e964"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for handling seasons data<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-12-05T18.55.19image.png.webp?alt=media&token=6613f6e2-e930-4012-9d71-c182851b93a4"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for handling seasons data from the api and instering records to the<br>database<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Describe the process</td></tr>
<tr><td> <em>Response:</em> <p>&nbsp;def get(url, params=None, API_REF=&quot;API&quot;):<br><div>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; return API._fetch(url, params, API_REF, HTTP.GET)</div><div><ul><li>This method from the API<br>class helps to trigger the rest call and to get the JSON response<br>from the API in the list form</li></ul></div><div><ul><li>So, by calling this method API.get(url), we<br>can collect the JSON response and we can retrieve the response list and<br>by writing python logic we can get the attribute values.</li></ul></div><div><ul><li>After getting those values<br>we can insert this data to the database using those values Using INSERT<br>INTO database command<br></li></ul></div><br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Include related pull request(s)</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Suchith-Balne/sb2648-is601-007/pull/31">https://github.com/Suchith-Balne/sb2648-is601-007/pull/31</a> </td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Describe any issues and learnings throughout this milestone</td></tr>
<tr><td> <em>Response:</em> <div>Faced few issues while retrieving the rest api and inserting to the database<br>but solved after watching tutorials and referring to the sample projects.</div><div>This milestone helped<br>me to get the data from the api and insert that data to<br>database and perform CRUD on the database.</div><div><br></div><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a link to your herok prod project's login page</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://is601-sb2648-prod-2beda061efe9.herokuapp.com">https://is601-sb2648-prod-2beda061efe9.herokuapp.com</a> </td></tr>
<tr><td> <em>Sub-Task 3: </em> Include Screenshots from Wakatime</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-12-05T18.58.22image.png.webp?alt=media&token=423b7eb2-c5f6-42b8-ae34-ebceb7becd78"/></td></tr>
<tr><td> <em>Caption:</em> <p>Milestone2 wakatime graph<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-12-05T18.58.37image.png.webp?alt=media&token=ddbb2a42-98d9-4381-87e5-65241d7c2ec0"/></td></tr>
<tr><td> <em>Caption:</em> <p>Milestone2 with various branches and there time<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-milestone-2-api-project/grade/sb2648" target="_blank">Grading</a></td></tr></table>