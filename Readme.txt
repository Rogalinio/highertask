App on heroku:
https://higherweb.herokuapp.com/



At first, if the task seems too complicated, don’t worry – you’ll find tips at the bottom. The task is to write a web API that will allow grading and listing Tasks given by a Recruiter to the Candidate.

    Below is the suggested Django Models structure. Decide by yourself about fields and relation details (on_delete, blank, null, related_name, unique etc.).

+---------------+      +-------------+
|   Candidate   |      |  Recruiter  |
+---------------+      +-------------+
|pk             |      |pk           |
|first_name     |      |first_name   |
|last_name      |      |last_name    |
+-------+-------+      +------+------+
        ^                     ^
        |                     |
        |                     |
        |                     |
+-------+------+              |
|    Grade     +--------------+
+--------------+
|pk            |          +----------+
|value         |          |   Task   |
|task          |          +----------+
|candidate     +--------->+pk        |
|recruiter     |          |title     |
+--------------+          +----------+

    After you’ve created models, add Django Admin functionality to them.
    Create a view that will allow grading Candidates’ tasks by Recruiters.
        The view should be accessed via /api/add-mark url
        The view should check if a particular Task was already graded. If so, it should refuse adding a new Grade to the Task.
        You can either create a FormView or accept JSON object in body (don’t care about how it looks ;) ).
    Create a view that will return a list of Candidates, their average grade and a list of Grades per Candidate. The view should return a JSON response — you’ll find the expected data format below.

{
 "data": [
  {
   "pk": 1,
   "full_name": "Jan Kowalski",
   "avg_grade": 4.25,
   "grades": [
    4,
    5,
    5,
    3
   ]
  }
 ]
}

    Create a Github repository and push the code there.
    Bonus points Publish the working version on Heroku.
    Send us back a link to the newly created repository and published page.
