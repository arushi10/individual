{% include navigation.html %}

# Create Task

[Link to Video](https://drive.google.com/file/d/1HyN55DX2iZLsKuHZHSjRwV4LmbwRt5cQ/view)

3. a)i. The purpose of the program is to provide students with a quiz as a study tool to asses their knowledge of AP Computer Science Principles.
3. a)ii. The video demonstrates the user taking the quiz. To input their answer to the question, the user must select either the answer radio button. The program provides them with their score.
3. a) iii. The input is the button that the user clicks. The output is the score.

3. b) i. 
`        const myQuestions = [
            {
                question: "In which decade was the Internet first implemented?",
                answers: {
                    a: "1940s",
                    b: "1950s",
                    c: "1960s",
                    d: "1980s"
                },
                correctAnswer: "c"
            },
            {
                question: "Main circuit board in a computer is:",
                answers: {
                    a: "GPU",
                    b: "father board",
                    c: "mother board",
                    d: "CPU"
                },
                correctAnswer: "c"
            },
            {
                question: "What is Internet Explorer?",
                answers: {
                    a: "website",
                    b: "person who searches the internet",
                    c: "red page",
                    d: "web browser"
                },
                correctAnswer: "d"
            }
        ];
`

3. b) ii. 
`generateQuiz(myQuestions, quizContainer, resultsContainer, submitButton);`

3. b) iii. The list is called myQuestions

3. b) iv. The list contains the question bank

3. b) v. The list allows the questions to be displayed.

3. c) i.
`       function generateQuiz(questions, quizContainer, resultsContainer, submitButton){
            function showQuestions(questions, quizContainer){
                // place to store the output and the answer choices
                var output = [];
                var answers;

                // for each question...
                for(var i=0; i<questions.length; i++){

                    // reset the list of answers
                    answers = [];

                    // for each answer to this question...
                    for(letter in questions[i].answers){

                        // ...add an html radio button
                        answers.push(
                            '<label>'
                            + '<input type="radio" name="question'+i+'" value="'+letter+'">'
                            + letter + ': '
                            + questions[i].answers[letter]
                            + '</label>'
                        );
                    }

                    // add this question and its answers to the output
                    output.push(
                        '<div class="question">' + questions[i].question + '</div>'
                        + '<div class="answers">' + answers.join('') + '</div>'
                    );
                }

                // finally combine our output list into one string of html and put it on the page
                quizContainer.innerHTML = output.join('');
            }`

`            function showResults(questions, quizContainer, resultsContainer){

                // gather answer containers from our quiz
                var answerContainers = quizContainer.querySelectorAll('.answers');

                // keep track of user's answers
                var userAnswer = '';
                var score = 0;

                // for each question...
                for(var i=0; i<questions.length; i++){

                    // find selected answer
                    userAnswer = (answerContainers[i].querySelector('input[name=question'+i+']:checked')||{}).value;

                    if(userAnswer===questions[i].correctAnswer){
                        score++;

                        // color the answers green
                        answerContainers[i].style.color = 'lightgreen';
                    }
                    // if answer is wrong or blank
                    else{
                        // color the answers red
                        answerContainers[i].style.color = 'red';
                    }
                }

                resultsContainer.innerHTML = score + ' out of ' + questions.length;
            }`

3. c) ii. 
`// on submit, show results
            submitButton.onclick = function(){
                showResults(questions, quizContainer, resultsContainer);
            }
        }
`

3. c) iii. The procedure displays the quiz and shows the results.

3. c) iv. The event listener for the algorithm is the submit button. Once the button is clicked, the showResults function is called.

3. d) i. The call varies based on the answer choice button clicked.

3. d) ii.  Each call tests whether the answer is correct or incorrect.

3. d) iii. The result of the call is the score variable.

Original Plan:
Computer Science Quiz

Program Purpose: Create a multiple-choice quiz to test a student's computer science knowledge.

Input: Checkboxes (only one checkbox can be checked per question). Submit button at the end of the quiz.

Output: Display the text "correct" or "incorrect" based on which checkbox the user selected. Create a variable called "score" that temporarily stores the student's total score for that round.

Lists: Stores different questions and answers when querying from database. The rows in the database will be represented as lists in the program.

Procedure: Randomize the question order. Return "correct" or "incorrect" based on checkbox selected.

Parameters: The checkboxes that the user selected.

Sequencing: The steps of the algorithm are retrieve and display questions from database in a randomized order, user input (checkbox), procedure that gets answers from database, and return quiz score.

Selection: Return different outputs based on the checkboxes checked.

Iteration: Regenerate the test, so people can take it again.

Database: Store questions and answers as tables. The primary key is question number and answer number. Create a test table that generates a quiz, but does not randomize.

Current Project:
User input is selecting a checkbox. The program allows the users to see if they answered the questions correctly or incorrectly. We chose not to use databases but are still using data collection.
