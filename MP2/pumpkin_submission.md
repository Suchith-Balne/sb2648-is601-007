<table><tr><td> <em>Assignment: </em> IS601 - Mini Project 2 - Pumpkins</td></tr>
<tr><td> <em>Student: </em> Suchith Sameeri Balne (sb2648)</td></tr>
<tr><td> <em>Generated: </em> 10/23/2023 8:42:34 PM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-mini-project-2-pumpkins/grade/sb2648" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <ol><li>Create a new branch per the desired branch name below</li><li>Add the baseline files from the following link:&nbsp;<a href="https://gist.github.com/MattToegel/bb0d25257414c7154267baf0931dbef4">https://gist.github.com/MattToegel/bb0d25257414c7154267baf0931dbef4</a></li><li>Put them into a subfolder in your repository folder (I called my folder MP2)</li><li>Create a test folder as a subdirectory of MP2</li><li>git add .</li><li>git commit -m "baseline files"</li><li>git push origin (name of desired branch below)</li><li>You can go to github and open the pull request for evidence capturing later (don't close/merge the pull request until you're done with the assignment)</li><li>Do the below tasks and fill in the below entries</li><ol><li>git add/commit after any significant changes to build up history</li></ol><li>Save the below input and generate the submission markdown file (copy to clipboard or download the file)</li><li>Name it something relevant to the assignment if it's not named already</li><li>git add the submission file</li><li>git commit the submission file</li><li>git push the submission file</li><li>Complete the pull request to dev</li><li>Create a pull request from dev to prod</li><li>Go to the prod branch on github, navigate to the submission file</li><li>Paste that link to Canvas</li></ol></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Code Changes - Add the calculate_cost() implementation </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of the updated method calculate_cost()</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-10-23T22.48.55image.png.webp?alt=media&token=55f64248-9bd4-496b-a964-9c5ef06e6598"/></td></tr>
<tr><td> <em>Caption:</em> <p>Method for calculating total cost for all the products in the inprogress_pumkin array<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-10-23T22.29.15image.png.webp?alt=media&token=be4e789e-a126-477c-84f5-859af7ae03a9"/></td></tr>
<tr><td> <em>Caption:</em> <p>Output of the calculate_cost method showing total amount including $ sign.<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-10-23T23.14.03image.png.webp?alt=media&token=c34de571-fc4a-472d-b9ee-6fb0d13365f5"/></td></tr>
<tr><td> <em>Caption:</em> <p>Handling floating point in currency format<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain the approach to implementing the calculation</td></tr>
<tr><td> <em>Response:</em> <ul><li>This method takes care of cost calculation for the products present in inprogress_pumpkin<br>array depending on the category and returns the total cost of all the<br>products.</li><li>Currency formatting can be handled using a simple float formatting in the print<br>statement like {:.2f}, this displays the numbers in floats with two decimal places.<br></li></ul><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Exception Handling </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of adjusted code to handle exceptions</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-10-23T23.17.27image.png.webp?alt=media&token=e660c51c-78c4-405a-ba16-0eea38fc069c"/></td></tr>
<tr><td> <em>Caption:</em> <p>This screenshot shows the code implementation for handling all the exceptions <br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-10-23T23.39.53Exceptions.jpeg.webp?alt=media&token=7f222cbf-a305-4b12-b9d6-663d52ef5592"/></td></tr>
<tr><td> <em>Caption:</em> <p>NeedsCleaningException, OutOfStock, InvalidChoice, ExceededRemaining exceptions output<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-10-23T23.42.17image.png.webp?alt=media&token=67ae1921-45b6-401e-9661-2d9191b2e474"/></td></tr>
<tr><td> <em>Caption:</em> <p>Payment Exception<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each exception handling process</td></tr>
<tr><td> <em>Response:</em> <ul><li><b>OutOfStockException </b>is handled here, and a message to the user is displayed showing<br>a valid out of stock message in particular they are trying to add<br>category.</li><li>Whenever the array is filled with items, it needs to be cleaned in<br>order to accommodate the products for the next customers. This is handled in<br><b>NeedsCleaningException</b> and cleaning can be performed by giving a "clean" keyword and prints<br>the message after cleaning.</li><li><b>InvalidChoiceException</b> is raised whenever user tries to enter a invalid<br>item which is not present in the pumpkins list. Also, message is displayed<br>in which category this exception is occurred.</li><li><b>ExceededRemainingChoicesException</b>&nbsp; is raised when user tries to<br>add products more than the maximum allowed range defined for the each category<br>and we make user to follow selection for next categories by changing the<br>current selection to next category.</li><li><b>InvalidPaymentException </b>is raised when a user tries to enter<br>the amount other than the displayed total and an appropriate message is shown<br>to the user to enter total amount to complete payment.</li></ul>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <br><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Test Cases </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot(s) of test cases per the checklist</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-10-23T23.53.35image.png.webp?alt=media&token=ea15686c-8b94-48da-91b9-fcb9fa3ec2df"/></td></tr>
<tr><td> <em>Caption:</em> <p>Test pumpkin must be first selection<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-10-23T23.58.21image.png.webp?alt=media&token=6fc74aa2-a141-496f-bf26-78e2c5968888"/></td></tr>
<tr><td> <em>Caption:</em> <p>Can add stencils only when they are in stock, can add extras only<br>in stock<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-10-24T00.00.31image.png.webp?alt=media&token=81f9cbc2-d216-44c4-8e4c-72b4ff58c7bd"/></td></tr>
<tr><td> <em>Caption:</em> <p>Can add 3 stencils and extras in any order<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-10-24T00.03.42image.png.webp?alt=media&token=ce52f184-3df8-4a30-9fca-0a977de56e27"/></td></tr>
<tr><td> <em>Caption:</em> <p>Cost calculation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-10-24T00.05.59image.png.webp?alt=media&token=f80649e1-aa64-489d-b544-1a7d3add95fc"/></td></tr>
<tr><td> <em>Caption:</em> <p>Total sales calculation<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-10-24T00.07.35image.png.webp?alt=media&token=a3bbc84d-adda-4fb7-8fde-bb04cfb146a6"/></td></tr>
<tr><td> <em>Caption:</em> <p>Total products increment<br></p>
</td></tr>
<tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-10-24T00.09.38image.png.webp?alt=media&token=ae2fe921-d72f-48a2-87eb-ab69e8c260a6"/></td></tr>
<tr><td> <em>Caption:</em> <p>All tests<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Summarize each test case logic</td></tr>
<tr><td> <em>Response:</em> <div>Test 1 - pumpkin must be the first selection (can't add face stencils<br>or extras without a pumpkin choice)</div><div>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; In this test case we test for<br>the exception if face stencils can be added without pumpkin<br></div><div>Test 2 - can<br>only add face stencils if they're in stock</div><div>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; In this test case we<br>test whether en exception is raised if more than recommended stencils are added<br></div><div>Test<br>3 - can only add extras if they're in stock</div><div>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  In this<br>test case we test whether en exception is raised if more than recommended<br>extras are added</div><div>Test 4 - Can add up to 3 face stencils of<br>any combination</div><div>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; In this test case we check if 3 face stencils can<br>be added in any combination<br></div><div>Test 5 - Can add up to 3 extras<br>of any combination</div><div>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; In this test case we check if 3 extras can<br>be added in any combination.</div><div>Test 6 - cost must be calculated properly based<br>on the choices (check for currency format as part of this) (test case<br>should have a few permutations of at least 3 valid pumpkins [hint parameterized<br>tests])</div><div>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; In this test case, we check for the total calculation of all<br>the products are done properly.<br></div><div>Test 7 - Total Sales (sum of costs) must<br>be calculated properly (test case should have a few permutations of at least<br>3 valid pumpkins [hint parameterized tests])</div><div>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; In this test case, we check for<br>the Total sales value is calculated properly.<br></div><div>Test 8 - Total products variable should<br>properly increment for each purchase</div><div>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; In this test case, we check for product<br>update is done properly or not.<br></div><br></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add pull request for the assignment</td></tr>
<tr><td> <a rel="noreferrer noopener" target="_blank" href="https://github.com/Suchith-Balne/sb2648-is601-007/pull/10">https://github.com/Suchith-Balne/sb2648-is601-007/pull/10</a> </td></tr>
<tr><td> <em>Sub-Task 2: </em> Explain any issues/difficulties or something you learned while doing this assignment</td></tr>
<tr><td> <em>Response:</em> <p>Faced issue in one test case with InvalidStageSelection but later resolved it by<br>adding Pumpkins, stencils and extras <br><br></p><br></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of successful output</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://firebasestorage.googleapis.com/v0/b/learn-e1de9.appspot.com/o/assignments%2Fsb2648%2F2023-10-24T00.41.56image.png.webp?alt=media&token=d3653f30-088e-4030-aec8-d8f7f3e153ae"/></td></tr>
<tr><td> <em>Caption:</em> <p>Added few products and calculated price<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-007-F23/is601-mini-project-2-pumpkins/grade/sb2648" target="_blank">Grading</a></td></tr></table>