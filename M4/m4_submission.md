<table><tr><td> <em>Assignment: </em> M4-Simple-Calc</td></tr>
<tr><td> <em>Student: </em> Suchith Sameeri Balne (sb2648)</td></tr>
<tr><td> <em>Generated: </em> 10/16/2023 7:04:35 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/m4-simple-calc/grade/sb2648" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <p>Make sure you're working in an up to date branch</p><ul><li><code>git checkout dev</code></li><li><code>git pull origin dev</code></li><li><code>git checkout -b M4-Simple-Calc</code></li></ul><p>This will likely be started in class.</p><p>Steps:</p><ol><li>Create a new Folder called M4</li><li>Create a new file called MyCalc.py inside this folder</li><li>Create a MyCalc Class</li><li>Define basic addition / subtraction / multiplication / division functions<ol><li>These functions should update an internal variable as a running total/value called&nbsp;<code><b>ans</b></code></li><li>All functions must properly handle the math given standard math scenarios (i.e., show proper messages when trying to divide by zero for example)</li><li>Since you'll likely be taking screenshots of the code, make sure you add a comment with your ucid and the date</li></ol></li><li>Define a "main" logic to run when the program runs</li><li>This logic should ask for user input<ol><li>The input can be any valid number, any valid math operator, and any valid number (i.e., 2 * 2)<ol><li>This will do an immediate calculation, print it, and store the answer in the&nbsp;<code>ans</code>&nbsp;variable</li></ol></li><li>Alternatively, the input can be&nbsp;<code>ans</code>, any valid math operator, any valid number (i.e.,&nbsp;<code>ans</code>&nbsp;* 2)<ol><li>This will use the previous answer (or 0 if not set) as part of the calculation, print it, and will store the new answer in the&nbsp;<code>ans</code>&nbsp;variable</li></ol></li></ol></li><li>Create a test case for each scenario that utilize functions to have expected input and compare against expected output, all cases should pass (test cases should have a series of data passed into them)<ol><li>Test number-add-number</li><li>Test ans-add-number</li><li>Test number-sub-number</li><li>Test ans-sub-number</li><li>Test number-mult-number</li><li>Test ans-mult-number</li><li>Test number-div-number</li><li>Test ans-div-number</li></ol></li><li>Create a new file called m4_submission.md inside the M4 folder</li><li>Fill out the below deliverables</li><li>Generate the markdown and paste it into the m4_submission.md</li><li><code>git add .</code></li><li><code>git commit -m "adding m4 hw"</code></li><li><code>git push origin M4-Simple-Calc</code></li><li>Create a pull request M4-Simple-Calc to dev</li><li>Create a pull request dev to prod (after the previous one is merged)</li><li>Navigate to the prod branch on github, go to the M4 folder, click the m4_submission.md</li><li>Submit this link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Snippets (Make sure each screenshot has a comment showing your ucid and the date it was written) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of valid Addition Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-10-16T22.16.28image.png.webp?alt=media&token=61a367d6-bdda-4f1f-add9-d01e30c914c3"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for addition of two numbers<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-10-16T22.25.00image.png.webp?alt=media&token=c8cd2ce9-7645-445c-85f5-336cfbc1c663"/></td></tr>
<tr><td> <em>Caption:</em> <p>Addition of two numbers<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshot of valid Subtraction Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-10-16T22.24.33image.png.webp?alt=media&token=d2a16e4e-305a-412e-96e2-051ef76ffb26"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code for subtraction of two numbers<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-10-16T22.26.53image.png.webp?alt=media&token=a556fcbf-de3d-438a-9246-eb9a94234e62"/></td></tr>
<tr><td> <em>Caption:</em> <p>Subtraction of two numbers<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of valid Multiplication Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-10-16T22.28.10image.png.webp?alt=media&token=083254dd-7e67-4052-9771-225f90cd4fd1"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code and result for Multiplication of two numbers<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshot of valid division Function</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-10-16T22.29.38image.png.webp?alt=media&token=2d96edaa-a270-4b73-911b-068fd2ea1ebd"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code and result for division of two numbers. This also includes result for<br>Divide by zero error.<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Test Case Validations </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of passing number-add-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-10-16T22.33.49image.png.webp?alt=media&token=e6a31dbd-5099-427b-9d74-d53ffd94c3f2"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code snippet for number-add-number testcase<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-10-16T22.34.44image.png.webp?alt=media&token=44242c76-8ccf-4eb1-8d8f-cae8e920579b"/></td></tr>
<tr><td> <em>Caption:</em> <p>Result of pytest for number-add-number<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of passing ans-add-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-10-16T22.39.13image.png.webp?alt=media&token=fe02bfc4-6677-4f9e-b931-7367874e4ab0"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code snippet  and result for ans-add-number testcase<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of passing number-sub-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-10-16T22.41.32image.png.webp?alt=media&token=2c6e66a0-5ef7-47b1-88a1-495bc93a1aba"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code snippet  and result for number-sub-number testcase<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Screenshots of passing ans-sub-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-10-16T22.43.04image.png.webp?alt=media&token=de5b950b-692b-4195-a450-2b7d00cb1bca"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code snippet  and result for ans-sub-number  testcase<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 5: </em> Screenshots of passing number-mult-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-10-16T22.45.09image.png.webp?alt=media&token=20cbf054-a338-4f91-8a9c-a97388708380"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code snippet  and result for number-mult-number testcase<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 6: </em> Screenshots of passing ans-multi-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-10-16T22.47.14image.png.webp?alt=media&token=321e81aa-f818-4f3f-879f-b85981461749"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code snippet  and result for ans-multi-number testcase<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 7: </em> Screenshots of passing number-div-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-10-16T22.48.13image.png.webp?alt=media&token=b7382854-a80b-415f-944a-0e519405979f"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code snippet  and result for number-div-number testcase<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 8: </em> Screenshots of passing ans-div-number Test Case and code snippet</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-10-16T22.49.27image.png.webp?alt=media&token=01ac5350-d859-4d4e-a529-1513cc109b11"/></td></tr>
<tr><td> <em>Caption:</em> <p>Code snippet  and result for ans-div-number testcase<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-10-16T22.51.53image.png.webp?alt=media&token=b4e6f8a3-99d8-4834-986a-8800e92d3a66"/></td></tr>
<tr><td> <em>Caption:</em> <p>Screenshot for all passed testcases<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Briefly talk about anything you learn during this assignment/module</td></tr>
<tr><td> <em>Response:</em> <ul><li>Learned how to use pytest and it's interesting to write testcases for each<br>function.</li><li>Pytest fixtures are very helpful in maintaining state <br></li></ul><br></td></tr>
<tr><td> <em>Sub-Task 2: </em> Discuss how test cases work and anything new you learned about them while doing this assignment, specially include how fixtures and parameterized tests work</td></tr>
<tr><td> <em>Response:</em> <ul><li>Learned how to use pytest and it's interesting to write testcases for each<br>function.</li><li>Learned how to use Pytest fixtures.</li></ul><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Add the pull request of M4-Simple-Calc to Dev link</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Suchith-Balne/sb2648-is601-007/pull/8">https://github.com/Suchith-Balne/sb2648-is601-007/pull/8</a> </td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/m4-simple-calc/grade/sb2648" target="_blank">Grading</a></td></tr></table>